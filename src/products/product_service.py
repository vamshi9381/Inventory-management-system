from ..config.database import get_connection


# ==================================================
# CREATE - Add Product
# ==================================================

def add_product(
    product_name,
    category_id,
    supplier_id,
    price,
    sku,
    description
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO products
            (
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        cursor.execute(
            query,
            (
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description
            )
        )

        connection.commit()

        print("Product added successfully.")

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        connection.close()


# ==================================================
# READ - View All Products
# ==================================================

def get_products():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                product_id,
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description
            FROM products
            ORDER BY product_id;
        """

        cursor.execute(query)

        products = cursor.fetchall()

        for product in products:
            print(product)

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()


# ==================================================
# READ - Search Product
# ==================================================

def search_product(product_name):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                product_id,
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description
            FROM products
            WHERE product_name ILIKE %s
            ORDER BY product_id;
        """

        cursor.execute(
            query,
            (f"%{product_name}%",)
        )

        products = cursor.fetchall()

        if not products:
            print("No products found.")
            return

        for product in products:
            print(product)

    except Exception as error:
        print("Error:", error)

    finally:
        connection.close()


# ==================================================
# UPDATE - Update Product Price
# ==================================================

def update_product_price(product_id, new_price):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            UPDATE products
            SET price = %s
            WHERE product_id = %s;
        """

        cursor.execute(
            query,
            (new_price, product_id)
        )

        if cursor.rowcount == 0:
            print("Product not found.")
            return

        connection.commit()

        print("Product price updated successfully.")

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        connection.close()


# ==================================================
# DELETE - Delete Product
# ==================================================

def delete_product(product_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM products
            WHERE product_id = %s;
        """

        cursor.execute(
            query,
            (product_id,)
        )

        if cursor.rowcount == 0:
            print("Product not found.")
            return

        connection.commit()

        print("Product deleted successfully.")

    except Exception as error:
        connection.rollback()
        print("Error:", error)

    finally:
        connection.close()