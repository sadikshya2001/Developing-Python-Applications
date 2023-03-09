numofMonth = int(input("Enter the number of month: "))

match numofMonth:
    case 1:
        print("This is January and it has 31 days")
    
    case 2:
        print("This is February and it has 28 days")

    case 3:
        print("This is March and it has 31 days")

    case 4:
        print("This is April and it has 30 days")

    case 5:
        print("This is May and it has 31 days")

    case 6:
        print("This is June and it has 30 days")

    case 7:
        print("This is July and it has 31 days")

    case 8:
        print("This is August and it has 31 days")

    case 9:
        print("This is September and it has 30 days")

    case 10:
        print("This is October and it has 31 days")

    case 11:
        print("This is November and it has 30 days")

    case 12:
        print("This is December and it has 31 days")

    case _:
        print("INVALID")

    
