from ..config.database import get_connection


# ============================================================
# CREATE - ADD SUPPLIER
# ============================================================

def add_supplier(
    supplier_name,
    contact_person,
    phone,
    email,
    address
):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            INSERT INTO suppliers
            (
                supplier_name,
                contact_person,
                phone,
                email,
                address
            )
            VALUES (%s, %s, %s, %s, %s);
        """

        cursor.execute(
            query,
            (
                supplier_name,
                contact_person,
                phone,
                email,
                address
            )
        )

        connection.commit()

        print("\nSupplier added successfully.")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# READ - VIEW SUPPLIERS
# ============================================================

def get_suppliers():

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            SELECT
                supplier_id,
                supplier_name,
                contact_person,
                phone,
                email,
                address
            FROM suppliers
            ORDER BY supplier_id;
        """

        cursor.execute(query)

        suppliers = cursor.fetchall()

        if not suppliers:

            print("\nNo suppliers found.")

            return

        print("\n========================================")
        print("             ALL SUPPLIERS")
        print("========================================")

        for supplier in suppliers:

            print(
                f"ID: {supplier[0]} | "
                f"Name: {supplier[1]} | "
                f"Contact: {supplier[2]} | "
                f"Phone: {supplier[3]} | "
                f"Email: {supplier[4]} | "
                f"Address: {supplier[5]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# SEARCH SUPPLIER
# ============================================================

def search_supplier(supplier_name):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            SELECT
                supplier_id,
                supplier_name,
                contact_person,
                phone,
                email,
                address
            FROM suppliers
            WHERE supplier_name ILIKE %s
            ORDER BY supplier_id;
        """

        cursor.execute(
            query,
            (f"%{supplier_name}%",)
        )

        suppliers = cursor.fetchall()

        if not suppliers:

            print("\nNo suppliers found.")

            return

        print("\n========================================")
        print("            SEARCH RESULTS")
        print("========================================")

        for supplier in suppliers:

            print(
                f"ID: {supplier[0]} | "
                f"Name: {supplier[1]} | "
                f"Contact: {supplier[2]} | "
                f"Phone: {supplier[3]} | "
                f"Email: {supplier[4]} | "
                f"Address: {supplier[5]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# UPDATE SUPPLIER
# ============================================================

def update_supplier(supplier_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        # ----------------------------------------------------
        # GET CURRENT SUPPLIER
        # ----------------------------------------------------

        query = """
            SELECT
                supplier_name,
                contact_person,
                phone,
                email,
                address
            FROM suppliers
            WHERE supplier_id = %s;
        """

        cursor.execute(
            query,
            (supplier_id,)
        )

        supplier = cursor.fetchone()

        if supplier is None:

            print("\nSupplier not found.")

            return

        old_name = supplier[0]
        old_contact = supplier[1]
        old_phone = supplier[2]
        old_email = supplier[3]
        old_address = supplier[4]

        # ----------------------------------------------------
        # CURRENT DETAILS
        # ----------------------------------------------------

        print("\n========================================")
        print("        CURRENT SUPPLIER DETAILS")
        print("========================================")

        print(f"Supplier Name : {old_name}")
        print(f"Contact Person: {old_contact}")
        print(f"Phone         : {old_phone}")
        print(f"Email         : {old_email}")
        print(f"Address       : {old_address}")

        print("\nPress ENTER to keep the existing value.")
        print()

        # ----------------------------------------------------
        # SUPPLIER NAME
        # ----------------------------------------------------

        name_input = input(
            f"Supplier name [{old_name}]: "
        ).strip()

        if name_input == "":
            supplier_name = old_name
        else:
            supplier_name = name_input

        # ----------------------------------------------------
        # CONTACT PERSON
        # ----------------------------------------------------

        contact_input = input(
            f"Contact person [{old_contact}]: "
        ).strip()

        if contact_input == "":
            contact_person = old_contact
        else:
            contact_person = contact_input

        # ----------------------------------------------------
        # PHONE
        # ----------------------------------------------------

        phone_input = input(
            f"Phone [{old_phone}]: "
        ).strip()

        if phone_input == "":
            phone = old_phone
        else:
            phone = phone_input

        # ----------------------------------------------------
        # EMAIL
        # ----------------------------------------------------

        email_input = input(
            f"Email [{old_email}]: "
        ).strip()

        if email_input == "":
            email = old_email
        else:
            email = email_input

        # ----------------------------------------------------
        # ADDRESS
        # ----------------------------------------------------

        address_input = input(
            f"Address [{old_address}]: "
        ).strip()

        if address_input == "":
            address = old_address
        else:
            address = address_input

        # ----------------------------------------------------
        # UPDATE DATABASE
        # ----------------------------------------------------

        update_query = """
            UPDATE suppliers
            SET
                supplier_name = %s,
                contact_person = %s,
                phone = %s,
                email = %s,
                address = %s
            WHERE supplier_id = %s;
        """

        cursor.execute(
            update_query,
            (
                supplier_name,
                contact_person,
                phone,
                email,
                address,
                supplier_id
            )
        )

        connection.commit()

        print(
            "\nSupplier updated successfully."
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
# DELETE SUPPLIER
# ============================================================

def delete_supplier(supplier_id):

    connection = get_connection()

    try:

        cursor = connection.cursor()

        query = """
            DELETE FROM suppliers
            WHERE supplier_id = %s;
        """

        cursor.execute(
            query,
            (supplier_id,)
        )

        if cursor.rowcount == 0:

            print("\nSupplier not found.")

            return

        connection.commit()

        print(
            "\nSupplier deleted successfully."
        )

    except Exception as error:

        connection.rollback()

        if "foreign key constraint" in str(error).lower():

            print(
                "\nCannot delete this supplier "
                "because products are using it."
            )

        else:

            print(
                "\nError:",
                error
            )

    finally:

        connection.close()