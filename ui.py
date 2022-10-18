print("Welcome to the crypto-currencie converter")
print("To get started enter '1'")
print("For instructions enter '2'")


#hardcoded list of coins to be changed later
coinList = ['bit coin', 'doge coin', 'light coin']


isValid = None
while isValid is None:
    try:
        choice = int(input())
        if choice == 1 or choice == 2:
            isValid= True
        else:
            print("Invalid input.")
            print("To get started enter '1'")
            print("For instructions enter '2'")

    except:
        print("invalid input. Please enter only an integer")
        print("To get started enter '1'")
        print("For instructions enter '2'")


if choice == 2:
    print("This program will convert different crypto currencies")
    print("You will be prompted to choose a crypto currency to convert from,")
    print("Than you will select the amount of that currency.")
    print("Finally you will choose the currency to be converted too.")
    print("")
choice = None

print("Enter starting currency. Enter '1' to see currency options or '2' to see instructions.")
isValid = None
while isValid is None:
    choice = input()
    if choice == '2':
        print("This program will convert different crypto currencies")
        print("You will be prompted to choose a crypto currency to convert from,")
        print("Than you will select the amount of that currency.")
        print("Finally you will choose the currency to be converted too.")
        print("")
        print("To see coin options enter '1'")
        print("For instructions enter '2'")
    elif choice == '1':
        print("The coins to choose from are...")
        print(coinList)
        print("Enter starting currency. Enter '1' to see currency options or '2' to see instructions.")
    elif choice in coinList:
        isValid = True
    else:
        print("Enter a valid coin.")
        print("To see coin options enter '1'")
        print("For instructions enter '2'")


isValid = None
while isValid is None:
    print("Enter an integer equal to the quantity you want to convert")
    try:
        choice = int(input())
        isValid= True
        print('')
    except:
        print("Invalid input.")
        print("Enter an integer equal to the quantity you want to convert")

print("Enter currency to be converted too. Enter '1' to see currency options or '2' to see instructions.")
isValid = None
while isValid is None:
    choice = input()
    if choice == '2':
        print("This program will convert different crypto currencies")
        print("You will be prompted to choose a crypto currency to convert from,")
        print("Than you will select the amount of that currency.")
        print("Finally you will choose the currency to be converted too.")
        print("")
        print("Enter currency to be converted too. Enter '1' to see currency options or '2' to see instructions.")
    elif choice == '1':
        print("The coins to choose from are...")
        print(coinList)
        print("Enter currency to be converted too. Enter '1' to see currency options or '2' to see instructions.")
    elif choice in coinList:
        isValid = True
    else:
        print("Enter a valid coin.")
        print("To see coin options enter '1'")
        print("For instructions enter '2'")


print("Your answer is ________")
print("Enter '1' to do another conversion. Enter '2' to quit")
