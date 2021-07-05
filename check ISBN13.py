import sys
print(sys.maxsize)

def ISBN13(input):
    output = input
    total = 0
    length = len(str(input))
    if length != 12:                        # check the input has 12 digits
        return 'Incorrect Input'
    for loop in range(length):
        eachDigit = input % 10              # extract each unit
        input = input // 10                 # shift operation
        if loop % 2:                        # using boolean value to multiply each digit alternatively by 1 and 3
            total = total + eachDigit
        else:
            total = total + eachDigit * 3
    endNumber = (10 - total % 10) % 10      # make 10 to 0
    return output * 10 + endNumber


x = ISBN13(978014300723)
print(x)