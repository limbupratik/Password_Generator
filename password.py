import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper  ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@#$&_-()=%*:/!?+."

string = lower + upper + numbers + symbols
length = int(input("How many Character long you need the password: "));
password = "".join(random.sample(string, length))

print("Here is your password", password)


