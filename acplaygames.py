print("Welcome to the Shy Calculator. If you're here, it means you're shy.")
yeslist = ["Y", "YES", "ye", "y", "Yes", "yes"]
nolist = ["N", "NO", "NAH" "n", "No", "no"]
def calculator():
    while True:
        try:
            x = float(input("Alright, choose number 1 \n"))
            print("bruh!")
            y = float(input("Alright, choose number 2 \n"))
            print("Alright, let's move on the actual calculator noob!")
            func = input("What function would you like to operate with? \n +, -, *, or / ? \n" )
            if func == "+":
                answer = (x + y)
                print(f"Computing... \n x + y = {answer}")
                cont = input("Would you like to continue?")
                if cont in yeslist:
                    print("Ok!")
                if cont in nolist:
                    break
            elif func == "-":
                answer = (x - y)
                print(f"Computing... \n x + y = {answer}")
                cont = input("Would you like to continue?")
                if cont in yeslist:
                    print("Ok!")
                if cont in nolist:
                    break
            elif func == "*":
                answer = (x * y)
                print(f"Computing... \n x + y = {answer}")
                cont = input("Would you like to continue?")
                if cont in yeslist:
                    print("Ok!")
                if cont in nolist:
                    break
            elif func == "/":
                answer = (x / y)
                print(f"Computing... \n x + y = {answer}")
                cont = input("Would you like to continue?")
                if cont in yeslist:
                    print("Ok!")
                if cont in nolist:
                    break
        except:
            print('You did not type in a number')
            calculator()

calculator()


