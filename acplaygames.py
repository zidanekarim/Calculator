print("Calculator starting in \n 3...2...1")
yeslist = ["Y", "ye", "y", "Yes", "yes"]
nolist = ["N", "NO", "NAH", "n", "No", "no"]


def restart():
    global h
    cont = input("Would you like to continue?")
    if cont.lower() in yeslist:
        print("Ok!")
        h = 1
    if cont.lower() in nolist:
        h = 2
        print("Alright")


def calculator():
    global h
    h = 1
    while h == 1:
        try:
            x = float(input("Alright, choose number 1 \n"))
            y = float(input("Alright, choose number 2 \n"))
            print("Alright, let's move on the actual calculator!")
            func = input("What function would you like to operate with? \n +, -, *, or / ? \n")
            if func == "+":
                answer = (x + y)
                print("Computing... \n" + str(x) + " + " + str(y) + " = " + str(answer))
                restart()
            elif func == "-":
                answer = (x - y)
                print("Computing... \n" + str(x) + " - " + str(y) + " = " + str(answer))
                restart()

            elif func == "*":
                answer = (x * y)
                print("Computing... \n" + str(x) + " * " + str(y) + " = " + str(answer))
                restart()

            elif func == "/":
                answer = (x / y)
                print("Computing... \n" + str(x) + " / " + str(y) + " = " + str(answer))
                restart()
        except():
            print('You did not type in a number')
            calculator()


calculator()
