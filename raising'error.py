
while True:
    try:
        age=int(input("What is your age:"))
        10/age
        raise ValueError("hey cut it out!")
        continue
    except ZeroDivisionError:
        print("Please enter a number other than zero!")
    else:
        print("THANK YOU!")
        break
    finally:
        print("FINALLLY I AM DONE:))")
