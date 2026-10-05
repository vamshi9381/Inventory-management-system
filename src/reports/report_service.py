from config.database import get_connection


def inventory_report():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                p.product_name,
                c.category_name,
                i.quantity,
                p.price,
                i.quantity * p.price AS inventory_value
            FROM products p
            JOIN categories c
                ON p.category_id = c.category_id
            JOIN inventory i
                ON p.product_id = i.product_id
            ORDER BY inventory_value DESC;
        """)

        report = cursor.fetchall()

        print("\n===== INVENTORY REPORT =====")

        for row in report:
            print(row)

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()


def total_inventory_value():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                SUM(i.quantity * p.price)
            FROM inventory i
            JOIN products p
                ON i.product_id = p.product_id;
        """)

        result = cursor.fetchone()

        print("Total Inventory Value:", result[0])

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()