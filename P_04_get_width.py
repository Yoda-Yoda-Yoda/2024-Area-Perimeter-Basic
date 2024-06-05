# Ask user for width and loop until they
# Enter a nuber that is more than zero

error = "Please enter number that is more than zero\n"

while True:
    try:
        # ask the user for a number
        width = float(input("width: "))

        # check that the number is more than zero
        if width > 0:
            break

        else:
            print(error)
    except ValueError:
        print(error)
