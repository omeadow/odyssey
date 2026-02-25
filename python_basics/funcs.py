def add_two_numbers(num1, num2):
    sum = num1 + num2
    add_two_numbers.sum = sum
    return num1+num2

def parent_func():
    def child_func():
        return "I am a child function"
    attribute = child_func
    number = 10

print(add_two_numbers.sum)