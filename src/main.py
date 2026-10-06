# ============================================================
# IMPORTS
# ============================================================

from .products.product_service import (
    add_product,
    get_products,
    search_product,
    update_product,
    delete_product
)

from .categories.category_service import (
    add_category,
    get_categories,
    search_category,
    update_category,
    delete_category
)

from .suppliers.supplier_service import (
    add_supplier,
    get_suppliers,
    search_supplier,
    update_supplier,
    delete_supplier
)

from .customers.customer_service import (
    add_customer,
    get_customers,
    search_customer,
    update_customer,
    delete_customer
)

from .inventory.inventory_service import (
    add_inventory,
    get_inventory,
    search_inventory,
    update_inventory,
    get_low_stock,
    delete_inventory
)

from .sales.sales_service import (
    create_order,
    get_orders,
    get_order_details,
    update_order_status,
    cancel_order
)

from .reports.report_service import (
    inventory_report,
    low_stock_report,
    sales_report,
    product_sales_report,
    customer_order_report,
    category_sales_report
)


# ============================================================
# PRODUCT MANAGEMENT
# ============================================================

def product_menu():

    while True:

        print("\n========================================")
        print("          PRODUCT MANAGEMENT")
        print("========================================")
        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n---------- ADD PRODUCT ----------")

            product_name = input(
                "Product name: "
            ).strip()

            try:

                category_id = int(
                    input("Category ID: ")
                )

                supplier_id = int(
                    input("Supplier ID: ")
                )

                price = float(
                    input("Price: ")
                )

            except ValueError:

                print("\nInvalid numeric value.")
                continue

            sku = input(
                "SKU: "
            ).strip()

            description = input(
                "Description: "
            ).strip()

            add_product(
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description
            )

        elif choice == "2":

            get_products()

        elif choice == "3":

            product_name = input(
                "Enter product name to search: "
            ).strip()

            search_product(product_name)

        elif choice == "4":

            try:

                product_id = int(
                    input("Enter product ID to update: ")
                )

                update_product(product_id)

            except ValueError:

                print("\nInvalid Product ID.")

        elif choice == "5":

            try:

                product_id = int(
                    input("Enter product ID to delete: ")
                )

                delete_product(product_id)

            except ValueError:

                print("\nInvalid Product ID.")

        elif choice == "6":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# CATEGORY MANAGEMENT
# ============================================================

def category_menu():

    while True:

        print("\n========================================")
        print("          CATEGORY MANAGEMENT")
        print("========================================")
        print("1. Add Category")
        print("2. View Categories")
        print("3. Search Category")
        print("4. Update Category")
        print("5. Delete Category")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n---------- ADD CATEGORY ----------")

            category_name = input(
                "Category name: "
            ).strip()

            description = input(
                "Description: "
            ).strip()

            add_category(
                category_name,
                description
            )

        elif choice == "2":

            get_categories()

        elif choice == "3":

            category_name = input(
                "Enter category name to search: "
            ).strip()

            search_category(category_name)

        elif choice == "4":

            try:

                category_id = int(
                    input("Enter category ID to update: ")
                )

                update_category(category_id)

            except ValueError:

                print("\nInvalid Category ID.")

        elif choice == "5":

            try:

                category_id = int(
                    input("Enter category ID to delete: ")
                )

                delete_category(category_id)

            except ValueError:

                print("\nInvalid Category ID.")

        elif choice == "6":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# SUPPLIER MANAGEMENT
# ============================================================

def supplier_menu():

    while True:

        print("\n========================================")
        print("          SUPPLIER MANAGEMENT")
        print("========================================")
        print("1. Add Supplier")
        print("2. View Suppliers")
        print("3. Search Supplier")
        print("4. Update Supplier")
        print("5. Delete Supplier")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n---------- ADD SUPPLIER ----------")

            supplier_name = input(
                "Supplier name: "
            ).strip()

            contact_person = input(
                "Contact person: "
            ).strip()

            phone = input(
                "Phone: "
            ).strip()

            email = input(
                "Email: "
            ).strip()

            address = input(
                "Address: "
            ).strip()

            add_supplier(
                supplier_name,
                contact_person,
                phone,
                email,
                address
            )

        elif choice == "2":

            get_suppliers()

        elif choice == "3":

            supplier_name = input(
                "Enter supplier name to search: "
            ).strip()

            search_supplier(supplier_name)

        elif choice == "4":

            try:

                supplier_id = int(
                    input("Enter supplier ID to update: ")
                )

                update_supplier(supplier_id)

            except ValueError:

                print("\nInvalid Supplier ID.")

        elif choice == "5":

            try:

                supplier_id = int(
                    input("Enter supplier ID to delete: ")
                )

                delete_supplier(supplier_id)

            except ValueError:

                print("\nInvalid Supplier ID.")

        elif choice == "6":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# CUSTOMER MANAGEMENT
# ============================================================

def customer_menu():

    while True:

        print("\n========================================")
        print("          CUSTOMER MANAGEMENT")
        print("========================================")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Search Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n---------- ADD CUSTOMER ----------")

            customer_name = input(
                "Customer name: "
            ).strip()

            email = input(
                "Email: "
            ).strip()

            phone = input(
                "Phone: "
            ).strip()

            address = input(
                "Address: "
            ).strip()

            add_customer(
                customer_name,
                email,
                phone,
                address
            )

        elif choice == "2":

            get_customers()

        elif choice == "3":

            customer_name = input(
                "Enter customer name to search: "
            ).strip()

            search_customer(customer_name)

        elif choice == "4":

            try:

                customer_id = int(
                    input("Enter customer ID to update: ")
                )

                update_customer(customer_id)

            except ValueError:

                print("\nInvalid Customer ID.")

        elif choice == "5":

            try:

                customer_id = int(
                    input("Enter customer ID to delete: ")
                )

                delete_customer(customer_id)

            except ValueError:

                print("\nInvalid Customer ID.")

        elif choice == "6":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# INVENTORY MANAGEMENT
# ============================================================

def inventory_menu():

    while True:

        print("\n========================================")
        print("         INVENTORY MANAGEMENT")
        print("========================================")
        print("1. Add Inventory")
        print("2. View Inventory")
        print("3. Search Inventory")
        print("4. Update Inventory")
        print("5. Low Stock Report")
        print("6. Delete Inventory")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n---------- ADD INVENTORY ----------")

            try:

                product_id = int(
                    input("Product ID: ")
                )

                quantity = int(
                    input("Quantity: ")
                )

                reorder_level = int(
                    input("Reorder level: ")
                )

                if quantity < 0:

                    print("\nQuantity cannot be negative.")
                    continue

                if reorder_level < 0:

                    print(
                        "\nReorder level cannot be negative."
                    )

                    continue

                add_inventory(
                    product_id,
                    quantity,
                    reorder_level
                )

            except ValueError:

                print(
                    "\nPlease enter valid numeric values."
                )

        elif choice == "2":

            get_inventory()

        elif choice == "3":

            product_name = input(
                "Enter product name to search: "
            ).strip()

            search_inventory(product_name)

        elif choice == "4":

            try:

                inventory_id = int(
                    input("Enter inventory ID to update: ")
                )

                update_inventory(inventory_id)

            except ValueError:

                print("\nInvalid Inventory ID.")

        elif choice == "5":

            get_low_stock()

        elif choice == "6":

            try:

                inventory_id = int(
                    input("Enter inventory ID to delete: ")
                )

                delete_inventory(inventory_id)

            except ValueError:

                print("\nInvalid Inventory ID.")

        elif choice == "7":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# SALES / ORDER MANAGEMENT
# ============================================================

def sales_menu():

    while True:

        print("\n========================================")
        print("       SALES / ORDER MANAGEMENT")
        print("========================================")
        print("1. Create Order")
        print("2. View Orders")
        print("3. View Order Details")
        print("4. Update Order Status")
        print("5. Cancel Order")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            print("\n---------- CREATE ORDER ----------")

            try:

                customer_id = int(
                    input("Customer ID: ")
                )

                product_id = int(
                    input("Product ID: ")
                )

                quantity = int(
                    input("Quantity: ")
                )

                create_order(
                    customer_id,
                    product_id,
                    quantity
                )

            except ValueError:

                print(
                    "\nPlease enter valid numeric values."
                )

        elif choice == "2":

            get_orders()

        elif choice == "3":

            try:

                order_id = int(
                    input("Enter order ID: ")
                )

                get_order_details(order_id)

            except ValueError:

                print("\nInvalid Order ID.")

        elif choice == "4":

            try:

                order_id = int(
                    input("Enter order ID: ")
                )

                status = input(
                    "Enter new status "
                    "(PENDING/CONFIRMED/SHIPPED/"
                    "DELIVERED/CANCELLED): "
                ).strip()

                update_order_status(
                    order_id,
                    status
                )

            except ValueError:

                print("\nInvalid Order ID.")

        elif choice == "5":

            try:

                order_id = int(
                    input("Enter order ID to cancel: ")
                )

                cancel_order(order_id)

            except ValueError:

                print("\nInvalid Order ID.")

        elif choice == "6":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# REPORTS
# ============================================================

def reports_menu():

    while True:

        print("\n========================================")
        print("              REPORTS")
        print("========================================")
        print("1. Inventory Report")
        print("2. Low Stock Report")
        print("3. Sales Report")
        print("4. Product Sales Report")
        print("5. Customer Order Report")
        print("6. Category Sales Report")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":

            inventory_report()

        elif choice == "2":

            low_stock_report()

        elif choice == "3":

            sales_report()

        elif choice == "4":

            product_sales_report()

        elif choice == "5":

            customer_order_report()

        elif choice == "6":

            category_sales_report()

        elif choice == "7":

            break

        else:

            print("\nInvalid choice. Please try again.")


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n========================================")
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Product Management")
        print("2. Category Management")
        print("3. Supplier Management")
        print("4. Customer Management")
        print("5. Inventory Management")
        print("6. Sales / Order Management")
        print("7. Reports")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":

            product_menu()

        elif choice == "2":

            category_menu()

        elif choice == "3":

            supplier_menu()

        elif choice == "4":

            customer_menu()

        elif choice == "5":

            inventory_menu()

        elif choice == "6":

            sales_menu()

        elif choice == "7":

            reports_menu()

        elif choice == "8":

            print(
                "\nThank you for using "
                "Inventory Management System."
            )

            print("Goodbye!")

            break

        else:

            print(
                "\nInvalid choice. Please try again."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()