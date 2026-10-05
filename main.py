from products.product_service import get_products
from inventory.inventory_service import get_inventory
from inventory.inventory_service import get_low_stock_products
from reports.report_service import inventory_report
from reports.report_service import total_inventory_value


def main():

    while True:

        print("\n================================")
        print("   INVENTORY MANAGEMENT SYSTEM")
        print("================================")

        print("1. View Products")
        print("2. View Inventory")
        print("3. Low Stock Report")
        print("4. Inventory Report")
        print("5. Total Inventory Value")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_products()

        elif choice == "2":
            get_inventory()

        elif choice == "3":
            get_low_stock_products()

        elif choice == "4":
            inventory_report()

        elif choice == "5":
            total_inventory_value()

        elif choice == "6":
            print("Thank you!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()