"""
An Armstrong number is equal to the sum of the cubes of its digits.
For example, 370 is an Armstrong number because 3*3*3 + 7*7*7 + 0*0*0 = 370.
An Armstrong number is often called Narcissistic number.
"""


def armstrong_number(n: int) -> bool:
    if not isinstance(n, int) or n < 1:
        return False

    sum = 0
    number_of_digits = 0
    temp = n
    while temp > 0:
        number_of_digits += 1
        temp //= 10
    temp = n
    while temp > 0:
        rem = temp % 10
        sum += rem ** number_of_digits
        temp //= 10
    return n == sum


num = int(input("Enter an integer to see if it is an Armstrong number: ").strip())
print(f"{num} is {'' if armstrong_number(num) else 'not '}an Armstrong number.")

