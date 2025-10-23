# ...existing code...
'''def cal_sum(n):
    if n == 0:
        return 0
    return cal_sum(n-1) + n
sum = cal_sum(5)
print("Sum of first 5 natural numbers is:", sum)'''
#
def check_number(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")
check_number(7)
#
def calculator(a, b, operator):
    if operator == "+":
        print("Result:", a + b)
    elif operator == "-":
        print("Result:", a - b)
    elif operator == "*":
        print("Result:", a * b)
    elif operator == "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operator! Use +, -, *, or /.")
calculator(10, 5, "*")   
#
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)       
count_vowels("Artificial")   
#
def analyze(numbers):
    stats = {
        'sum': sum(numbers),
        'max': max(numbers),
        'min': min(numbers)
    }
    print(stats)
analyze([5, 10, 15])
#
def table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
table(3)

