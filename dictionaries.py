countryDb = {}
while True:
    print("1) Insert")
    print("2) Display all countries")
    print("3) Display all capitals")
    print("4) Get capital")
    print("5) Delete")

    choice = int(input("Enter a choice from 1 to 5."))
    if choice == 1:
        country = input("Enter a country: ").upper()
        capital = input("Enter your country's capital: ").upper()
        countryDb[country] = capital
        print("Here is the updated dictionary:")
        print(countryDb)
    elif choice == 2:
        print(list(countryDb.keys()))
    elif choice == 3:
        print(list(countryDb.values()))
    elif choice == 4:
        countryA = input("Enter a country to find the capital of: ").upper()
        print(countryDb.get(countryA))
    elif choice == 5:
        countryB = input("Enter country to delete: ").upper()
        del countryDb[countryB]

    else:
        print("Invalid choice. Try again.")
        break