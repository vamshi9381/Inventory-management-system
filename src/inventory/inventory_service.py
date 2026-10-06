from ..config.database import get_connection


# ============================================================
# ADD INVENTORY
# ============================================================

def add_inventory(product_id, quantity, reorder_level):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO inventory
            (
                product_id,
                quantity,
                reorder_level
            )
            VALUES (%s, %s, %s);
        """

        cursor.execute(
            query,
            (
                product_id,
                quantity,
                reorder_level
            )
        )

        connection.commit()

        print("\nInventory added successfully.")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# VIEW INVENTORY
# ============================================================

def get_inventory():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                i.inventory_id,
                i.product_id,
                p.product_name,
                i.quantity,
                i.reorder_level,
                i.last_updated
            FROM inventory i
            INNER JOIN products p
                ON i.product_id = p.product_id
            ORDER BY i.inventory_id;
        """

        cursor.execute(query)

        inventory = cursor.fetchall()

        if not inventory:

            print("\nNo inventory records found.")

            return

        print("\n========================================")
        print("             ALL INVENTORY")
        print("========================================")

        for item in inventory:

            print(
                f"Inventory ID: {item[0]} | "
                f"Product ID: {item[1]} | "
                f"Product: {item[2]} | "
                f"Quantity: {item[3]} | "
                f"Reorder Level: {item[4]} | "
                f"Updated: {item[5]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# SEARCH INVENTORY
# ============================================================

def search_inventory(product_name):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                i.inventory_id,
                i.product_id,
                p.product_name,
                i.quantity,
                i.reorder_level,
                i.last_updated
            FROM inventory i
            INNER JOIN products p
                ON i.product_id = p.product_id
            WHERE p.product_name ILIKE %s
            ORDER BY i.inventory_id;
        """

        cursor.execute(
            query,
            (f"%{product_name}%",)
        )

        inventory = cursor.fetchall()

        if not inventory:

            print("\nNo inventory found.")

            return

        print("\n========================================")
        print("          INVENTORY SEARCH RESULTS")
        print("========================================")

        for item in inventory:

            print(
                f"Inventory ID: {item[0]} | "
                f"Product ID: {item[1]} | "
                f"Product: {item[2]} | "
                f"Quantity: {item[3]} | "
                f"Reorder Level: {item[4]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# UPDATE INVENTORY
# ============================================================

def update_inventory(inventory_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                i.product_id,
                p.product_name,
                i.quantity,
                i.reorder_level
            FROM inventory i
            INNER JOIN products p
                ON i.product_id = p.product_id
            WHERE i.inventory_id = %s;
        """

        cursor.execute(
            query,
            (inventory_id,)
        )

        inventory = cursor.fetchone()

        if inventory is None:

            print("\nInventory record not found.")

            return

        old_product_id = inventory[0]
        old_product_name = inventory[1]
        old_quantity = inventory[2]
        old_reorder_level = inventory[3]

        print("\n========================================")
        print("        CURRENT INVENTORY DETAILS")
        print("========================================")

        print(f"Product ID    : {old_product_id}")
        print(f"Product Name  : {old_product_name}")
        print(f"Quantity      : {old_quantity}")
        print(f"Reorder Level : {old_reorder_level}")

        print("\nPress ENTER to keep the existing value.\n")

        quantity_input = input(
            f"Quantity [{old_quantity}]: "
        ).strip()

        if quantity_input == "":
            quantity = old_quantity
        else:

            try:
                quantity = int(quantity_input)

            except ValueError:

                print("\nInvalid quantity.")

                return

        reorder_input = input(
            f"Reorder level [{old_reorder_level}]: "
        ).strip()

        if reorder_input == "":
            reorder_level = old_reorder_level
        else:

            try:
                reorder_level = int(reorder_input)

            except ValueError:

                print("\nInvalid reorder level.")

                return

        update_query = """
            UPDATE inventory
            SET
                quantity = %s,
                reorder_level = %s,
                last_updated = CURRENT_TIMESTAMP
            WHERE inventory_id = %s;
        """

        cursor.execute(
            update_query,
            (
                quantity,
                reorder_level,
                inventory_id
            )
        )

        connection.commit()

        print("\nInventory updated successfully.")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# LOW STOCK REPORT
# ============================================================

def get_low_stock():

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                i.inventory_id,
                p.product_name,
                i.quantity,
                i.reorder_level
            FROM inventory i
            INNER JOIN products p
                ON i.product_id = p.product_id
            WHERE i.quantity <= i.reorder_level
            ORDER BY i.quantity;
        """

        cursor.execute(query)

        inventory = cursor.fetchall()

        if not inventory:

            print("\nNo low-stock products found.")

            return

        print("\n========================================")
        print("             LOW STOCK REPORT")
        print("========================================")

        for item in inventory:

            print(
                f"Inventory ID: {item[0]} | "
                f"Product: {item[1]} | "
                f"Quantity: {item[2]} | "
                f"Reorder Level: {item[3]}"
            )

    except Exception as error:

        print("\nError:", error)

    finally:

        connection.close()


# ============================================================
# DELETE INVENTORY
# ============================================================

def delete_inventory(inventory_id):

    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            DELETE FROM inventory
            WHERE inventory_id = %s;
        """

        cursor.execute(
            query,
            (inventory_id,)
        )

        if cursor.rowcount == 0:

            print("\nInventory record not found.")

            return

        connection.commit()

        print("\nInventory deleted successfully.")

    except Exception as error:

        connection.rollback()

        print("\nError:", error)

    finally:

        connection.close()