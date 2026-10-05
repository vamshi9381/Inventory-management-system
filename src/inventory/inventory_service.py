from config.database import get_connection


def get_inventory():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                p.product_name,
                i.quantity,
                i.reorder_level
            FROM inventory i
            JOIN products p
                ON i.product_id = p.product_id
            ORDER BY p.product_name;
        """)

        inventory = cursor.fetchall()

        for item in inventory:
            print(item)

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()


def get_low_stock_products():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                p.product_name,
                i.quantity,
                i.reorder_level
            FROM inventory i
            JOIN products p
                ON i.product_id = p.product_id
            WHERE i.quantity <= i.reorder_level;
        """)

        products = cursor.fetchall()

        for product in products:
            print(product)

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()