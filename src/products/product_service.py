from ..config.database import get_connection


# ============================================================
# CREATE - ADD PRODUCT
# ============================================================

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
            VALUES (%s, %s, %s, %s, %s, %s);
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


# ============================================================
# READ - GET ALL PRODUCTS
# ============================================================

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

        if not products:

            print("No products found.")

            return

        print("\n")

        for product in products:

            print(
                f"ID: {product[0]} | "
                f"Name: {product[1]} | "
                f"Category: {product[2]} | "
                f"Supplier: {product[3]} | "
                f"Price: {product[4]} | "
                f"SKU: {product[5]} | "
                f"Description: {product[6]}"
            )

    except Exception as error:

        print("Error:", error)

    finally:

        connection.close()


# ============================================================
# READ - SEARCH PRODUCT
# ============================================================

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

            print(
                f"ID: {product[0]} | "
                f"Name: {product[1]} | "
                f"Category: {product[2]} | "
                f"Supplier: {product[3]} | "
                f"Price: {product[4]} | "
                f"SKU: {product[5]} | "
                f"Description: {product[6]}"
            )

    except Exception as error:

        print("Error:", error)

    finally:

        connection.close()


# ============================================================
# UPDATE - UPDATE PRODUCT
# ============================================================

def update_product(product_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        # ----------------------------------------------------
        # STEP 1: GET EXISTING PRODUCT
        # ----------------------------------------------------

        query = """
            SELECT
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description
            FROM products
            WHERE product_id = %s;
        """

        cursor.execute(
            query,
            (product_id,)
        )

        product = cursor.fetchone()

        # ----------------------------------------------------
        # PRODUCT NOT FOUND
        # ----------------------------------------------------

        if product is None:

            print(
                "\nProduct not found."
            )

            return

        # ----------------------------------------------------
        # STORE CURRENT VALUES
        # ----------------------------------------------------

        old_product_name = product[0]
        old_category_id = product[1]
        old_supplier_id = product[2]
        old_price = product[3]
        old_sku = product[4]
        old_description = product[5]

        # ----------------------------------------------------
        # DISPLAY CURRENT VALUES
        # ----------------------------------------------------

        print("\n========================================")
        print("        CURRENT PRODUCT DETAILS")
        print("========================================")

        print(
            f"Product Name : {old_product_name}"
        )

        print(
            f"Category ID  : {old_category_id}"
        )

        print(
            f"Supplier ID  : {old_supplier_id}"
        )

        print(
            f"Price        : {old_price}"
        )

        print(
            f"SKU          : {old_sku}"
        )

        print(
            f"Description  : {old_description}"
        )

        print("\nEnter new values.")
        print("Press ENTER to keep the existing value.")
        print()

        # ----------------------------------------------------
        # PRODUCT NAME
        # ----------------------------------------------------

        product_name_input = input(
            f"Product name [{old_product_name}]: "
        ).strip()

        if product_name_input == "":
            product_name = old_product_name
        else:
            product_name = product_name_input

        # ----------------------------------------------------
        # CATEGORY ID
        # ----------------------------------------------------

        category_id_input = input(
            f"Category ID [{old_category_id}]: "
        ).strip()

        if category_id_input == "":
            category_id = old_category_id

        else:

            try:

                category_id = int(
                    category_id_input
                )

            except ValueError:

                print(
                    "Invalid Category ID."
                )

                return

        # ----------------------------------------------------
        # SUPPLIER ID
        # ----------------------------------------------------

        supplier_id_input = input(
            f"Supplier ID [{old_supplier_id}]: "
        ).strip()

        if supplier_id_input == "":
            supplier_id = old_supplier_id

        else:

            try:

                supplier_id = int(
                    supplier_id_input
                )

            except ValueError:

                print(
                    "Invalid Supplier ID."
                )

                return

        # ----------------------------------------------------
        # PRICE
        # ----------------------------------------------------

        price_input = input(
            f"Price [{old_price}]: "
        ).strip()

        if price_input == "":
            price = old_price

        else:

            try:

                price = float(
                    price_input
                )

            except ValueError:

                print(
                    "Invalid price."
                )

                return

        # ----------------------------------------------------
        # SKU
        # ----------------------------------------------------

        sku_input = input(
            f"SKU [{old_sku}]: "
        ).strip()

        if sku_input == "":
            sku = old_sku

        else:
            sku = sku_input

        # ----------------------------------------------------
        # DESCRIPTION
        # ----------------------------------------------------

        description_input = input(
            f"Description [{old_description}]: "
        ).strip()

        if description_input == "":
            description = old_description

        else:
            description = description_input

        # ----------------------------------------------------
        # UPDATE DATABASE
        # ----------------------------------------------------

        update_query = """
            UPDATE products
            SET
                product_name = %s,
                category_id = %s,
                supplier_id = %s,
                price = %s,
                sku = %s,
                description = %s
            WHERE product_id = %s;
        """

        cursor.execute(
            update_query,
            (
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description,
                product_id
            )
        )

        connection.commit()

        print(
            "\nProduct updated successfully."
        )

    except Exception as error:

        connection.rollback()

        print(
            "\nError:",
            error
        )

    finally:

        connection.close()


# ============================================================
# DELETE - DELETE PRODUCT
# ============================================================

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

            print(
                "Product not found."
            )

            return

        connection.commit()

        print(
            "Product deleted successfully."
        )

    except Exception as error:

        connection.rollback()

        if "foreign key constraint" in str(error).lower():

            print(
                "Cannot delete this product because "
                "it is being used by other records."
            )

        else:

            print(
                "Error:",
                error
            )

    finally:

        connection.close()