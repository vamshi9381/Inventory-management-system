from ..config.database import get_connection


# ============================================================
# CREATE - ADD CATEGORY
# ============================================================

def add_category(category_name, description):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            INSERT INTO categories
            (
                category_name,
                description
            )
            VALUES (%s, %s);
        """

        cursor.execute(
            query,
            (
                category_name,
                description
            )
        )

        connection.commit()

        print("\nCategory added successfully.")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# READ - VIEW CATEGORIES
# ============================================================

def get_categories():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            SELECT
                category_id,
                category_name,
                description
            FROM categories
            ORDER BY category_id;
        """

        cursor.execute(query)

        categories = cursor.fetchall()

        if not categories:

            print("\nNo categories found.")

            return

        print("\n========================================")
        print("              CATEGORIES")
        print("========================================")

        for category in categories:

            print(
                f"ID: {category[0]} | "
                f"Name: {category[1]} | "
                f"Description: {category[2]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# SEARCH CATEGORY
# ============================================================

def search_category(category_name):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            SELECT
                category_id,
                category_name,
                description
            FROM categories
            WHERE category_name ILIKE %s
            ORDER BY category_id;
        """

        cursor.execute(
            query,
            (f"%{category_name}%",)
        )

        categories = cursor.fetchall()

        if not categories:

            print("\nNo categories found.")

            return

        for category in categories:

            print(
                f"ID: {category[0]} | "
                f"Name: {category[1]} | "
                f"Description: {category[2]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# UPDATE CATEGORY
# ============================================================

def update_category(category_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        # ----------------------------------------------------
        # GET EXISTING CATEGORY
        # ----------------------------------------------------

        query = """
            SELECT
                category_name,
                description
            FROM categories
            WHERE category_id = %s;
        """

        cursor.execute(
            query,
            (category_id,)
        )

        category = cursor.fetchone()

        if category is None:

            print("\nCategory not found.")

            return

        old_name = category[0]
        old_description = category[1]

        # ----------------------------------------------------
        # SHOW CURRENT VALUES
        # ----------------------------------------------------

        print("\n========================================")
        print("        CURRENT CATEGORY DETAILS")
        print("========================================")

        print(
            f"Category Name : {old_name}"
        )

        print(
            f"Description   : {old_description}"
        )

        print("\nPress ENTER to keep the existing value.\n")

        # ----------------------------------------------------
        # NEW NAME
        # ----------------------------------------------------

        name_input = input(
            f"Category name [{old_name}]: "
        ).strip()

        if name_input == "":
            category_name = old_name
        else:
            category_name = name_input

        # ----------------------------------------------------
        # NEW DESCRIPTION
        # ----------------------------------------------------

        description_input = input(
            f"Description [{old_description}]: "
        ).strip()

        if description_input == "":
            description = old_description
        else:
            description = description_input

        # ----------------------------------------------------
        # UPDATE
        # ----------------------------------------------------

        update_query = """
            UPDATE categories
            SET
                category_name = %s,
                description = %s
            WHERE category_id = %s;
        """

        cursor.execute(
            update_query,
            (
                category_name,
                description,
                category_id
            )
        )

        connection.commit()

        print(
            "\nCategory updated successfully."
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
# DELETE CATEGORY
# ============================================================

def delete_category(category_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            DELETE FROM categories
            WHERE category_id = %s;
        """

        cursor.execute(
            query,
            (category_id,)
        )

        if cursor.rowcount == 0:

            print("\nCategory not found.")

            return

        connection.commit()

        print(
            "\nCategory deleted successfully."
        )

    except Exception as error:

        connection.rollback()

        if "foreign key constraint" in str(error).lower():

            print(
                "\nCannot delete this category "
                "because products are using it."
            )

        else:

            print(
                "\nError:",
                error
            )

    finally:

        connection.close()