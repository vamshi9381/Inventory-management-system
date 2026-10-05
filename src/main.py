from .products.product_service import (
    add_product,
    get_products,
    search_product,
    update_product,
    delete_product
)


# ============================================================
# PRODUCT MANAGEMENT MENU
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
        print("6. Back")

        choice = input("Enter your choice: ").strip()

        # ====================================================
        # 1. ADD PRODUCT
        # ====================================================

        if choice == "1":

            print("\n========================================")
            print("             ADD PRODUCT")
            print("========================================")

            try:

                product_name = input(
                    "Enter product name: "
                ).strip()

                category_id = int(
                    input("Enter category ID: ")
                )

                supplier_id = int(
                    input("Enter supplier ID: ")
                )

                price = float(
                    input("Enter price: ")
                )

                sku = input(
                    "Enter SKU: "
                ).strip()

                description = input(
                    "Enter description: "
                ).strip()

                add_product(
                    product_name,
                    category_id,
                    supplier_id,
                    price,
                    sku,
                    description
                )

            except ValueError:

                print(
                    "\nInvalid input."
                )

                print(
                    "Category ID, Supplier ID and Price "
                    "must contain valid values."
                )

        # ====================================================
        # 2. VIEW PRODUCTS
        # ====================================================

        elif choice == "2":

            print("\n========================================")
            print("             ALL PRODUCTS")
            print("========================================")

            get_products()

        # ====================================================
        # 3. SEARCH PRODUCT
        # ====================================================

        elif choice == "3":

            print("\n========================================")
            print("            SEARCH PRODUCT")
            print("========================================")

            product_name = input(
                "Enter product name to search: "
            ).strip()

            if product_name == "":

                print(
                    "Search name cannot be empty."
                )

            else:

                search_product(product_name)

        # ====================================================
        # 4. UPDATE PRODUCT
        # ====================================================

        elif choice == "4":

            print("\n========================================")
            print("            UPDATE PRODUCT")
            print("========================================")

            try:

                product_id = int(
                    input("Enter product ID: ")
                )

                update_product(product_id)

            except ValueError:

                print(
                    "\nInvalid product ID."
                )

                print(
                    "Product ID must be a number."
                )

        # ====================================================
        # 5. DELETE PRODUCT
        # ====================================================

        elif choice == "5":

            print("\n========================================")
            print("            DELETE PRODUCT")
            print("========================================")

            try:

                product_id = int(
                    input("Enter product ID to delete: ")
                )

                # --------------------------------------------
                # CONFIRM DELETE
                # --------------------------------------------

                confirmation = input(
                    "Are you sure you want to delete "
                    "this product? (yes/no): "
                ).strip().lower()

                if confirmation == "yes":

                    delete_product(product_id)

                elif confirmation == "no":

                    print(
                        "Delete operation cancelled."
                    )

                else:

                    print(
                        "Please enter yes or no."
                    )

            except ValueError:

                print(
                    "\nInvalid product ID."
                )

                print(
                    "Product ID must be a number."
                )

        # ====================================================
        # 6. BACK
        # ====================================================

        elif choice == "6":

            print(
                "\nReturning to main menu..."
            )

            break

        # ====================================================
        # INVALID OPTION
        # ====================================================

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select a number between 1 and 6."
            )


# ============================================================
# MAIN MENU
# ============================================================

def main():

    while True:

        print("\n========================================")
        print("       INVENTORY MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Product Management")
        print("2. Exit")

        choice = input(
            "Enter your choice: "
        ).strip()

        # ====================================================
        # 1. PRODUCT MANAGEMENT
        # ====================================================

        if choice == "1":

            product_menu()

        # ====================================================
        # 2. EXIT
        # ====================================================

        elif choice == "2":

            print("\n========================================")
            print("     Thank you for using the system!")
            print("========================================")

            break

        # ====================================================
        # INVALID OPTION
        # ====================================================

        else:

            print(
                "\nInvalid choice."
            )

            print(
                "Please select 1 or 2."
            )


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":

    main()