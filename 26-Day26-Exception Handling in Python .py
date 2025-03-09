A = input("Enter a Number:")
print(f"Multiplication Table of {A} is:")
try:
    for i in range(1,11):
        print(f"{int(A)} X {i} = {int(A)*i}")
except:
    print("Invalid Input")

    print("End of Program")



    try:
        A = int(input("Enter a Number:"))
        B = [6,8]
        print(B[A])
    except ValueError:
        print("Invalid Input")
    except IndexError:
        print("Index Out of Range")
