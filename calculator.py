def calculator(): #main # def means definition
    print("Simple Calculator")#all are just for inputs ig or neatness
    print("Select operation:")
    print("1  Add")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("5 Exponentiation")
    
    balls = input("Enter choice (1/2/3/4/5): ")#choose operand

    if balls in ('1', '2', '3', '4','5'):# depend on operand(processing stuff)
        x = float(input("Enter first number: "))#choose x
        y = float(input("Enter second number: "))#choose y

        if balls == '1':# for the diffrent operands like + - etc
            print(f"Result: {x + y}")#prints result
        elif balls == '2':
            print(f"Result: {x - y}")
        elif balls == '3':
            print(f"Result: {x * y}")
        elif balls == '4':
            if y != 0:# makes sure that pc doesnt blast by trying to calculate x / 0 also != most likelky means not equal to
                print(f"Result: {x / y}")
            else:
                print("Error: Division by zero is not allowed.")# if divisor is 0
        elif balls == '5':
            print(f"Result: {x ** y}")
    else:
        print("Invalid input")# if not an input listed so that it doesnt give error codes and make life hell

calculator()#Call calculator back ig ???? #note to self this is to acctually run the program since def doesnt do shit but is just a definition for a term
# elif with if , if theres like many of them ig and else if its either like ig true or false
while True:# basically this for just re running it on will and not having to run when not needed
    calculator()
    again = input("Do you want to calculate again? (yes/no): ")# again is like an varianle i guess either true or false
    if again.lower() != 'yes':# so based on no ever u type it like if it was kept only 'yes' the if u type something like 'Yes' or something like that then the program will end but since of the .lower u can type it however u want regardless of itslower or upper case and the != ensure anything other than yes is terminated
        break
