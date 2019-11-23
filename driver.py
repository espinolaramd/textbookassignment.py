from book import textbook

book1 = textbook("Edonomics","Diego","Espinola",29,"1 Edition","123432","2010","Espinola",25,29.99)
book2 = textbook("The beauty of soccer","Lionel","Messi",32,"2 Edition","23455","2006","Espinola",30,129.99)

menu = 0

while menu != 4:
    print("This is the home menu, select what you want to do")
    print("1. Add to inventory")
    print("2. Deduct from inventory")
    print("3. Modify the price of the book")
    print("4. Quit the program")

    menu= int(input())

    if menu == 1:
        choice = int(input("Book 1 or Book 2?"))
        if choice == 1:
            print("How many would you like to add?")
            quantity = int(input())
            book1.add_inventory(quantity)
            print("The quantity in inventory is now"+ str(book1.quantity)+ "\n\n")
        elif choice == 2:
            print("How many would you like to add?")
            quantity = int(input())
            book2.add_inventory(quantity)
            print("The quantity in inventory is not"+ str(book2.quantity)+ "\n\n")
    elif menu == 2:
        choice = int(input("Book 1 or Book 2?"))
        if choice == 1:
            print("How many you like to deduct?")
            quantity = int(input())
            result = book1.deduct_inventory(quantity)
            if result == 0:
                print("The quantity in the inventory is now" + str(book1.quantity) +" \n\n")
            else:
                print("The inventory does not have enough to remove the quantity you entered ")
                print("The quantity in the inventory is now" + str(book1.quantity) + "\n\n")
        elif choice == 2:
            print("How many you like to deduct?")
            quantity = int(input())
            result = book2.deduct_inventory(quantity)
            if result == 0:
                print("The quantity in the inventory is now" + str(book2.quantity) +" \n\n")
            else:
                print("The inventory does not have enough to remove the quantity you entered ")
                print("The quantity in the inventory is now" + str(book1.quantity) + "\n\n")
    elif menu == 3:
        choice = int(input("Book 1 or Book 2"))
        if choice == 1:
            price = float("Enter the new price")
            print("The of"+ book1.title+"has been change to " +str(book1.price)+ "\n\n")
        if choice == 2:
            price = float("Enter the new price")
            print("The price of" +book2.title+"has been change to" +str(book2.price)+ "\n\n")
    elif menu == 4:
        print("Have a nice day")
    else:
        print("Error,please choice an oprion from the menu.")



