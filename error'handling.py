age=0
while True:
    try:
        age=int(input("What is your age:"))
        10/age
    except NameError:
        print("Please enter a number!")
        continue
    except ZeroDivisionError:
        print("Please enter a number other than zero!")
    else:
        print("THANK YOU!")
        break
    finally:
        print("Your age is: {}" .format(age))
        print("FINALLLY I AM DONE:))")
