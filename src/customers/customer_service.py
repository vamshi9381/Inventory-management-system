from ..config.database import get_connection


# ============================================================
# ADD CUSTOMER
# ============================================================

def add_customer(customer_name, email, phone, address):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO customers
            (
                customer_name,
                email,
                phone,
                address
            )
            VALUES (%s, %s, %s, %s);
        """

        cursor.execute(
            query,
            (
                customer_name,
                email,
                phone,
                address
            )
        )

        connection.commit()

        print("\nCustomer added successfully.")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# VIEW CUSTOMERS
# ============================================================

def get_customers():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                customer_id,
                customer_name,
                email,
                phone,
                address,
                created_at
            FROM customers
            ORDER BY customer_id;
        """

        cursor.execute(query)

        customers = cursor.fetchall()

        if not customers:

            print("\nNo customers found.")

            return

        print("\n========================================")
        print("            ALL CUSTOMERS")
        print("========================================")

        for customer in customers:

            print(
                f"ID: {customer[0]} | "
                f"Name: {customer[1]} | "
                f"Email: {customer[2]} | "
                f"Phone: {customer[3]} | "
                f"Address: {customer[4]} | "
                f"Created: {customer[5]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# SEARCH CUSTOMER
# ============================================================

def search_customer(customer_name):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                customer_id,
                customer_name,
                email,
                phone,
                address,
                created_at
            FROM customers
            WHERE customer_name ILIKE %s
            ORDER BY customer_id;
        """

        cursor.execute(
            query,
            (f"%{customer_name}%",)
        )

        customers = cursor.fetchall()

        if not customers:

            print("\nNo customers found.")

            return

        print("\n========================================")
        print("           SEARCH RESULTS")
        print("========================================")

        for customer in customers:

            print(
                f"ID: {customer[0]} | "
                f"Name: {customer[1]} | "
                f"Email: {customer[2]} | "
                f"Phone: {customer[3]} | "
                f"Address: {customer[4]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# UPDATE CUSTOMER
# ============================================================

def update_customer(customer_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        # Get existing customer
        query = """
            SELECT
                customer_name,
                email,
                phone,
                address
            FROM customers
            WHERE customer_id = %s;
        """

        cursor.execute(
            query,
            (customer_id,)
        )

        customer = cursor.fetchone()

        if customer is None:

            print("\nCustomer not found.")

            return

        # Existing values
        old_name = customer[0]
        old_email = customer[1]
        old_phone = customer[2]
        old_address = customer[3]

        print("\n========================================")
        print("        CURRENT CUSTOMER DETAILS")
        print("========================================")

        print(f"Customer Name : {old_name}")
        print(f"Email         : {old_email}")
        print(f"Phone         : {old_phone}")
        print(f"Address       : {old_address}")

        print("\nPress ENTER to keep the existing value.\n")

        # Customer Name
        name_input = input(
            f"Customer name [{old_name}]: "
        ).strip()

        if name_input == "":
            customer_name = old_name
        else:
            customer_name = name_input

        # Email
        email_input = input(
            f"Email [{old_email}]: "
        ).strip()

        if email_input == "":
            email = old_email
        else:
            email = email_input

        # Phone
        phone_input = input(
            f"Phone [{old_phone}]: "
        ).strip()

        if phone_input == "":
            phone = old_phone
        else:
            phone = phone_input

        # Address
        address_input = input(
            f"Address [{old_address}]: "
        ).strip()

        if address_input == "":
            address = old_address
        else:
            address = address_input

        # Update query
        update_query = """
            UPDATE customers
            SET
                customer_name = %s,
                email = %s,
                phone = %s,
                address = %s
            WHERE customer_id = %s;
        """

        cursor.execute(
            update_query,
            (
                customer_name,
                email,
                phone,
                address,
                customer_id
            )
        )

        connection.commit()

        print("\nCustomer updated successfully.")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# DELETE CUSTOMER
# ============================================================

def delete_customer(customer_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM customers
            WHERE customer_id = %s;
        """

        cursor.execute(
            query,
            (customer_id,)
        )

        # Customer doesn't exist
        if cursor.rowcount == 0:

            print("\nCustomer not found.")

            return

        connection.commit()

        print("\nCustomer deleted successfully.")

    except Exception as error:

        connection.rollback()

        error_message = str(error).lower()

        if "foreign key" in error_message:

            print(
                "\nCannot delete this customer "
                "because orders are using this customer."
            )

        else:

            print("\nError:", error)

    finally:

        connection.close()