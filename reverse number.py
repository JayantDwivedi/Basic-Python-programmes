def reverse_number(number):
    reminder = 0
    while number > 0:
        reminder *= 10
        reminder += number % 10
        number /= 10
    return reminder
number=eval("Enter a number :: ")
print(reverse_number(number))
