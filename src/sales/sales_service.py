from ..config.database import get_connection


# ============================================================
# CREATE ORDER
# ============================================================

def create_order(customer_id, product_id, quantity):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # 1. Check customer
        # ----------------------------------------------------

        customer_query = """
            SELECT customer_name
            FROM customers
            WHERE customer_id = %s;
        """

        cursor.execute(
            customer_query,
            (customer_id,)
        )

        customer = cursor.fetchone()

        if customer is None:

            print("\nCustomer not found.")

            return

        # ----------------------------------------------------
        # 2. Get product and inventory information
        # ----------------------------------------------------

        product_query = """
            SELECT
                p.product_name,
                p.price,
                i.quantity
            FROM products p
            INNER JOIN inventory i
                ON p.product_id = i.product_id
            WHERE p.product_id = %s
            FOR UPDATE OF i;
        """

        cursor.execute(
            product_query,
            (product_id,)
        )

        product = cursor.fetchone()

        if product is None:

            print(
                "\nProduct not found or "
                "inventory record does not exist."
            )

            return

        product_name = product[0]
        unit_price = product[1]
        available_quantity = product[2]

        # ----------------------------------------------------
        # 3. Validate quantity
        # ----------------------------------------------------

        if quantity <= 0:

            print("\nQuantity must be greater than 0.")

            return

        if quantity > available_quantity:

            print(
                f"\nInsufficient stock."
                f"\nAvailable quantity: {available_quantity}"
            )

            return

        # ----------------------------------------------------
        # 4. Calculate total
        # ----------------------------------------------------

        total_amount = unit_price * quantity

        print("\n========================================")
        print("             ORDER SUMMARY")
        print("========================================")
        print(f"Customer ID       : {customer_id}")
        print(f"Customer Name     : {customer[0]}")
        print(f"Product ID        : {product_id}")
        print(f"Product Name      : {product_name}")
        print(f"Quantity          : {quantity}")
        print(f"Unit Price        : {unit_price}")
        print(f"Total Amount      : {total_amount}")
        print(f"Available Stock   : {available_quantity}")
        print("========================================")

        # ----------------------------------------------------
        # 5. Create order
        # ----------------------------------------------------

        order_query = """
            INSERT INTO orders
            (
                customer_id,
                status
            )
            VALUES (%s, 'PENDING')
            RETURNING order_id;
        """

        cursor.execute(
            order_query,
            (customer_id,)
        )

        order_id = cursor.fetchone()[0]

        # ----------------------------------------------------
        # 6. Create order item
        # ----------------------------------------------------

        order_item_query = """
            INSERT INTO order_items
            (
                order_id,
                product_id,
                quantity,
                unit_price
            )
            VALUES (%s, %s, %s, %s);
        """

        cursor.execute(
            order_item_query,
            (
                order_id,
                product_id,
                quantity,
                unit_price
            )
        )

        # ----------------------------------------------------
        # 7. Reduce inventory
        # ----------------------------------------------------

        inventory_query = """
            UPDATE inventory
            SET
                quantity = quantity - %s,
                last_updated = CURRENT_TIMESTAMP
            WHERE product_id = %s;
        """

        cursor.execute(
            inventory_query,
            (
                quantity,
                product_id
            )
        )

        # ----------------------------------------------------
        # 8. Commit transaction
        # ----------------------------------------------------

        connection.commit()

        print("\n========================================")
        print("          ORDER CREATED SUCCESSFULLY")
        print("========================================")
        print(f"Order ID       : {order_id}")
        print(f"Customer       : {customer[0]}")
        print(f"Product        : {product_name}")
        print(f"Quantity       : {quantity}")
        print(f"Unit Price     : {unit_price}")
        print(f"Total Amount   : {total_amount}")
        print("Status         : PENDING")
        print("========================================")

    except Exception as error:

        connection.rollback()

        print("\nOrder creation failed.")
        print("Error:", error)

    finally:

        connection.close()


# ============================================================
# VIEW ALL ORDERS
# ============================================================

def get_orders():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                o.order_id,
                c.customer_name,
                o.order_date,
                o.status,
                COALESCE(
                    SUM(oi.quantity * oi.unit_price),
                    0
                ) AS total_amount
            FROM orders o
            INNER JOIN customers c
                ON o.customer_id = c.customer_id
            LEFT JOIN order_items oi
                ON o.order_id = oi.order_id
            GROUP BY
                o.order_id,
                c.customer_name,
                o.order_date,
                o.status
            ORDER BY o.order_id;
        """

        cursor.execute(query)

        orders = cursor.fetchall()

        if not orders:

            print("\nNo orders found.")

            return

        print("\n========================================")
        print("               ALL ORDERS")
        print("========================================")

        for order in orders:

            print(
                f"Order ID: {order[0]} | "
                f"Customer: {order[1]} | "
                f"Date: {order[2]} | "
                f"Status: {order[3]} | "
                f"Total: {order[4]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# VIEW ORDER DETAILS
# ============================================================

def get_order_details(order_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # Order information
        # ----------------------------------------------------

        order_query = """
            SELECT
                o.order_id,
                c.customer_name,
                c.email,
                c.phone,
                o.order_date,
                o.status
            FROM orders o
            INNER JOIN customers c
                ON o.customer_id = c.customer_id
            WHERE o.order_id = %s;
        """

        cursor.execute(
            order_query,
            (order_id,)
        )

        order = cursor.fetchone()

        if order is None:

            print("\nOrder not found.")

            return

        print("\n========================================")
        print("             ORDER DETAILS")
        print("========================================")

        print(f"Order ID       : {order[0]}")
        print(f"Customer       : {order[1]}")
        print(f"Email          : {order[2]}")
        print(f"Phone          : {order[3]}")
        print(f"Order Date     : {order[4]}")
        print(f"Status         : {order[5]}")

        # ----------------------------------------------------
        # Order items
        # ----------------------------------------------------

        items_query = """
            SELECT
                p.product_name,
                oi.quantity,
                oi.unit_price,
                (oi.quantity * oi.unit_price) AS total
            FROM order_items oi
            INNER JOIN products p
                ON oi.product_id = p.product_id
            WHERE oi.order_id = %s
            ORDER BY oi.order_item_id;
        """

        cursor.execute(
            items_query,
            (order_id,)
        )

        items = cursor.fetchall()

        print("\n--------------- ITEMS ----------------")

        total_amount = 0

        for item in items:

            print(
                f"Product: {item[0]} | "
                f"Quantity: {item[1]} | "
                f"Unit Price: {item[2]} | "
                f"Total: {item[3]}"
            )

            total_amount += item[3]

        print("---------------------------------------")
        print(f"Total Amount: {total_amount}")

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# UPDATE ORDER STATUS
# ============================================================

def update_order_status(order_id, status):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # Validate status
        # ----------------------------------------------------

        allowed_statuses = [
            "PENDING",
            "CONFIRMED",
            "SHIPPED",
            "DELIVERED",
            "CANCELLED"
        ]

        status = status.upper()

        if status not in allowed_statuses:

            print("\nInvalid order status.")

            print("\nAllowed statuses:")

            for value in allowed_statuses:

                print(f"- {value}")

            return

        # ----------------------------------------------------
        # Check order
        # ----------------------------------------------------

        check_query = """
            SELECT order_id, status
            FROM orders
            WHERE order_id = %s;
        """

        cursor.execute(
            check_query,
            (order_id,)
        )

        order = cursor.fetchone()

        if order is None:

            print("\nOrder not found.")

            return

        old_status = order[1]

        # ----------------------------------------------------
        # Update status
        # ----------------------------------------------------

        update_query = """
            UPDATE orders
            SET status = %s
            WHERE order_id = %s;
        """

        cursor.execute(
            update_query,
            (
                status,
                order_id
            )
        )

        connection.commit()

        print("\nOrder status updated successfully.")
        print(f"Order ID   : {order_id}")
        print(f"Old Status : {old_status}")
        print(f"New Status : {status}")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# CANCEL ORDER
# ============================================================

def cancel_order(order_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # ----------------------------------------------------
        # Get order
        # ----------------------------------------------------

        order_query = """
            SELECT
                order_id,
                status
            FROM orders
            WHERE order_id = %s
            FOR UPDATE;
        """

        cursor.execute(
            order_query,
            (order_id,)
        )

        order = cursor.fetchone()

        if order is None:

            print("\nOrder not found.")

            return

        current_status = order[1]

        # ----------------------------------------------------
        # Check if already cancelled
        # ----------------------------------------------------

        if current_status == "CANCELLED":

            print("\nOrder is already cancelled.")

            return

        # ----------------------------------------------------
        # Don't cancel delivered order
        # ----------------------------------------------------

        if current_status == "DELIVERED":

            print(
                "\nDelivered orders cannot be cancelled."
            )

            return

        # ----------------------------------------------------
        # Get order items
        # ----------------------------------------------------

        items_query = """
            SELECT
                product_id,
                quantity
            FROM order_items
            WHERE order_id = %s;
        """

        cursor.execute(
            items_query,
            (order_id,)
        )

        items = cursor.fetchall()

        # ----------------------------------------------------
        # Restore inventory
        # ----------------------------------------------------

        for item in items:

            product_id = item[0]
            quantity = item[1]

            inventory_query = """
                UPDATE inventory
                SET
                    quantity = quantity + %s,
                    last_updated = CURRENT_TIMESTAMP
                WHERE product_id = %s;
            """

            cursor.execute(
                inventory_query,
                (
                    quantity,
                    product_id
                )
            )

        # ----------------------------------------------------
        # Update order status
        # ----------------------------------------------------

        update_query = """
            UPDATE orders
            SET status = 'CANCELLED'
            WHERE order_id = %s;
        """

        cursor.execute(
            update_query,
            (order_id,)
        )

        # ----------------------------------------------------
        # Commit
        # ----------------------------------------------------

        connection.commit()

        print("\n========================================")
        print("          ORDER CANCELLED")
        print("========================================")
        print(f"Order ID : {order_id}")
        print("Inventory restored successfully.")

    except Exception as error:

        connection.rollback()

        print("\nOrder cancellation failed.")
        print("Error:", error)

    finally:

        connection.close()