from textbook import textbook

book1 = textbook("Biology","Troy","Amegashie",35,"3rd Edition","15863","2017","TroyJBooks",25,29.99)
book2 = textbook("The beauty of soccer","Lionel","Messi",32,"2 Edition","23455","2006","Espinola",30,129.99)


def textbook_program():
    print("Welcome! This is your menu, what would you like to do?")
    print("1. Add to inventory")
    print("2. Deduct from inventory")
    print("3. Modify the price of a book")

    menu = int(input())

    if menu == 1:
        choice = int(input("Book 1 or Book 2?"))
        if choice == 1:
            print("How many copies would you like to add?")
            quantity = int(input())
            book1.add_inventory(quantity)
            print("The quantity available now is"+ str(book1.quantity)+ "\n\n")
        elif choice == 2:
            print("How many copies would you like to add?")
            quantity = int(input())
            book2.add_inventory(quantity)
            print("The quantity available now is"+ str(book2.quantity)+ "\n\n")
    elif menu == 2:
        choice = int(input("Book 1 or Book 2?"))
        if choice == 1:
            print("How many copies would you like to deduct?")
            quantity = int(input())
            result = book1.deduct_inventory(quantity)
            if result == 0:
                print("The quantity in the inventory is now" + str(book1.quantity) +" \n\n")
            else:
                print("Inventory is too low to remove that quantity")
                print("The quantity available is" + str(book1.quantity) + "\n\n")
        elif choice == 2:
            print("How many copies would you like to deduct?")
            quantity = int(input())
            result = book2.deduct_inventory(quantity)
            if result == 0:
                print("The quantity in the inventory is now" + str(book2.quantity) +" \n\n")
            else:
                 print("Inventory is too low to remove that quantity ")
                 print("The quantity available is" + str(book1.quantity) + "\n\n")
    elif menu == 3:
        choice = int(input("Book 1 or Book 2"))
        if choice == 1:
            price = float("Enter the new price")
            print(f"The price of {book1.title} has been updated to {str(book1.price)}\n\n")
        if choice == 2:
            price = float("Enter the new price")
            print("The price of" +book2.title+"has been updated to" +str(book2.price)+ "\n\n")


textbook_program()
