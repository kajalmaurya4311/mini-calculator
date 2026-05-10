try:

    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))

    print("What kind of operation do you want to perform. Press + for addition\nPress - for substraction\nPress *  for multiplication\nPress / for division")

    oper = input("Enter Operation: ")
    
    match oper:
        case "+":
            print(f"The result is: {a + b}")

        case "-":
            print(f"The result is: {a - b}")

        case "*":
            print(f"The result is: {a * b}")

        case "/":
            print(f"The result is: {a / b}")

        case default:
            print(f"There was an error")

except Exception as e:
    print("Enter a valid value of a and b")
