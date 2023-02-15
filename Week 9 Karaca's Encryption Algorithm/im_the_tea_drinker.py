x = input("Enter a text:  ")


def backwards(correct):
    x = correct[::-1]
    return x


def aca(input):
    input = input + "aca"
    return input

def replacer(input):
    input = input.replace("a", "0")
    input = input.replace("e", "1")
    input = input.replace("i", "2")
    input = input.replace("o", "2")
    input = input.replace("u", "3")


    return input

def encrypt(input):
    input = backwards(input)
    input = aca(input)
    input = replacer(input)
    return input

print(encrypt(x))


