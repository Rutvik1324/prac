# Function to check prime number
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Taking input from user
num = int(input("Enter a number: "))

# Checking and printing result
if is_prime(num):
    print("The number is Prime")
else:
    print("The number is Not Prime")
