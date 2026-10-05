from .products.product_service import (
    add_product,
    get_products,
    search_product,
    update_product_price,
    delete_product
)


# ==================================================
# PRODUCT MANAGEMENT MENU
# ==================================================

def product_menu():

    while True:

        print("\n================================")
        print("       PRODUCT MANAGEMENT")
        print("================================")

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product Price")
        print("5. Delete Product")
        print("6. Back")

        choice = input("Enter your choice: ")

        # ------------------------------------------
        # ADD PRODUCT
        # ------------------------------------------

        if choice == "1":

            print("\n========== ADD PRODUCT ==========")

            product_name = input("Product name: ")
            category_id = int(input("Category ID: "))
            supplier_id = int(input("Supplier ID: "))
            price = float(input("Price: "))
            sku = input("SKU: ")
            description = input("Description: ")

            add_product(
                product_name,
                category_id,
                supplier_id,
                price,
                sku,
                description
            )

        # ------------------------------------------
        # VIEW PRODUCTS
        # ------------------------------------------

        elif choice == "2":

            print("\n========== ALL PRODUCTS ==========")

            get_products()

        # ------------------------------------------
        # SEARCH PRODUCT
        # ------------------------------------------

        elif choice == "3":

            print("\n========== SEARCH PRODUCT ==========")

            product_name = input(
                "Enter product name to search: "
            )

            search_product(product_name)

        # ------------------------------------------
        # UPDATE PRODUCT PRICE
        # ------------------------------------------

        elif choice == "4":

            print("\n========== UPDATE PRODUCT ==========")

            product_id = int(
                input("Enter product ID: ")
            )

            new_price = float(
                input("Enter new price: ")
            )

            update_product_price(
                product_id,
                new_price
            )

        # ------------------------------------------
        # DELETE PRODUCT
        # ------------------------------------------

        elif choice == "5":

            print("\n========== DELETE PRODUCT ==========")

            product_id = int(
                input("Enter product ID to delete: ")
            )

            delete_product(product_id)

        # ------------------------------------------
        # BACK
        # ------------------------------------------

        elif choice == "6":

            print("\nReturning to main menu...")
            break

        # ------------------------------------------
        # INVALID OPTION
        # ------------------------------------------

        else:

            print("\nInvalid choice. Please try again.")


# ==================================================
# MAIN MENU
# ==================================================

def main():

    while True:

        print("\n========================================")
        print("     INVENTORY MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Product Management")
        print("2. Exit")

        choice = input("Enter your choice: ")

        # ------------------------------------------
        # PRODUCT MANAGEMENT
        # ------------------------------------------

        if choice == "1":

            product_menu()

        # ------------------------------------------
        # EXIT
        # ------------------------------------------

        elif choice == "2":

            print("\nThank you for using the system!")
            break

        # ------------------------------------------
        # INVALID OPTION
        # ------------------------------------------

        else:

            print("\nInvalid choice. Please try again.")


# ==================================================
# PROGRAM START
# ==================================================

if __name__ == "__main__":
    main()