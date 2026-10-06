from ..config.database import get_connection


# ============================================================
# 1. INVENTORY REPORT
# ============================================================

def inventory_report():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                p.product_id,
                p.product_name,
                c.category_name,
                s.supplier_name,
                p.price,
                i.quantity,
                i.reorder_level,
                (p.price * i.quantity) AS inventory_value
            FROM products p
            INNER JOIN categories c
                ON p.category_id = c.category_id
            INNER JOIN suppliers s
                ON p.supplier_id = s.supplier_id
            INNER JOIN inventory i
                ON p.product_id = i.product_id
            ORDER BY p.product_id;
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:
            print("\nNo inventory records found.")
            return

        print("\n========================================")
        print("            INVENTORY REPORT")
        print("========================================")

        total_value = 0

        for record in records:

            inventory_value = record[7]

            total_value += inventory_value

            print(
                f"\nProduct ID      : {record[0]}"
                f"\nProduct Name    : {record[1]}"
                f"\nCategory        : {record[2]}"
                f"\nSupplier        : {record[3]}"
                f"\nPrice           : {record[4]}"
                f"\nQuantity        : {record[5]}"
                f"\nReorder Level   : {record[6]}"
                f"\nInventory Value : {record[7]}"
            )

        print("\n----------------------------------------")
        print(f"TOTAL INVENTORY VALUE: {total_value}")
        print("----------------------------------------")

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# 2. LOW STOCK REPORT
# ============================================================

def low_stock_report():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                p.product_id,
                p.product_name,
                c.category_name,
                i.quantity,
                i.reorder_level
            FROM products p
            INNER JOIN categories c
                ON p.category_id = c.category_id
            INNER JOIN inventory i
                ON p.product_id = i.product_id
            WHERE i.quantity <= i.reorder_level
            ORDER BY i.quantity;
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:

            print("\nNo low-stock products found.")

            return

        print("\n========================================")
        print("             LOW STOCK REPORT")
        print("========================================")

        for record in records:

            print(
                f"Product ID: {record[0]} | "
                f"Product: {record[1]} | "
                f"Category: {record[2]} | "
                f"Quantity: {record[3]} | "
                f"Reorder Level: {record[4]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# 3. SALES REPORT
# ============================================================

def sales_report():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                o.order_id,
                c.customer_name,
                o.order_date,
                o.status,
                SUM(oi.quantity * oi.unit_price) AS total_amount
            FROM orders o
            INNER JOIN customers c
                ON o.customer_id = c.customer_id
            INNER JOIN order_items oi
                ON o.order_id = oi.order_id
            GROUP BY
                o.order_id,
                c.customer_name,
                o.order_date,
                o.status
            ORDER BY o.order_id;
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:

            print("\nNo sales records found.")

            return

        print("\n========================================")
        print("              SALES REPORT")
        print("========================================")

        grand_total = 0

        for record in records:

            total_amount = record[4]

            grand_total += total_amount

            print(
                f"\nOrder ID     : {record[0]}"
                f"\nCustomer     : {record[1]}"
                f"\nOrder Date   : {record[2]}"
                f"\nStatus       : {record[3]}"
                f"\nOrder Total  : {record[4]}"
            )

        print("\n----------------------------------------")
        print(f"TOTAL SALES VALUE: {grand_total}")
        print("----------------------------------------")

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# 4. PRODUCT SALES REPORT
# ============================================================

def product_sales_report():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                p.product_id,
                p.product_name,
                SUM(oi.quantity) AS total_quantity_sold,
                SUM(
                    oi.quantity * oi.unit_price
                ) AS total_sales
            FROM order_items oi
            INNER JOIN products p
                ON oi.product_id = p.product_id
            INNER JOIN orders o
                ON oi.order_id = o.order_id
            WHERE o.status != 'CANCELLED'
            GROUP BY
                p.product_id,
                p.product_name
            ORDER BY total_sales DESC;
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:

            print("\nNo product sales found.")

            return

        print("\n========================================")
        print("          PRODUCT SALES REPORT")
        print("========================================")

        for record in records:

            print(
                f"Product ID: {record[0]} | "
                f"Product: {record[1]} | "
                f"Quantity Sold: {record[2]} | "
                f"Sales: {record[3]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# 5. CUSTOMER ORDER REPORT
# ============================================================

def customer_order_report():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                c.customer_id,
                c.customer_name,
                COUNT(DISTINCT o.order_id) AS total_orders,
                COALESCE(
                    SUM(
                        oi.quantity * oi.unit_price
                    ),
                    0
                ) AS total_spent
            FROM customers c
            LEFT JOIN orders o
                ON c.customer_id = o.customer_id
            LEFT JOIN order_items oi
                ON o.order_id = oi.order_id
            GROUP BY
                c.customer_id,
                c.customer_name
            ORDER BY total_spent DESC;
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:

            print("\nNo customer data found.")

            return

        print("\n========================================")
        print("         CUSTOMER ORDER REPORT")
        print("========================================")

        for record in records:

            print(
                f"Customer ID: {record[0]} | "
                f"Customer: {record[1]} | "
                f"Orders: {record[2]} | "
                f"Total Spent: {record[3]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# 6. CATEGORY SALES REPORT
# ============================================================

def category_sales_report():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                c.category_id,
                c.category_name,
                SUM(oi.quantity) AS quantity_sold,
                SUM(
                    oi.quantity * oi.unit_price
                ) AS total_sales
            FROM categories c
            INNER JOIN products p
                ON c.category_id = p.category_id
            INNER JOIN order_items oi
                ON p.product_id = oi.product_id
            INNER JOIN orders o
                ON oi.order_id = o.order_id
            WHERE o.status != 'CANCELLED'
            GROUP BY
                c.category_id,
                c.category_name
            ORDER BY total_sales DESC;
        """

        cursor.execute(query)

        records = cursor.fetchall()

        if not records:

            print("\nNo category sales found.")

            return

        print("\n========================================")
        print("          CATEGORY SALES REPORT")
        print("========================================")

        for record in records:

            print(
                f"Category ID: {record[0]} | "
                f"Category: {record[1]} | "
                f"Quantity Sold: {record[2]} | "
                f"Sales: {record[3]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()