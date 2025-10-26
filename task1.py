# This is the file for tasks in lesson_01

# 1
print("Task 1:")
def safe_div(a, b):
    if b == 0:
        return "Error"
    integ = a//b
    remainder = a % b
    return f"{a} divide by {b} is equal to {integ}, remainder is {remainder}"

print(safe_div(10, 3))  
print(safe_div(20, 5))   
print(safe_div(7, 0))

print(" ")
print("Task 2:")
name = input("Enter yout name:")
age = int(input("Enter your age:"))
print(f"You are {name} and you are {age} y o")

print(" ")
print("Task 3:")
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
numbers = list(range(1, 21))
even_numbers = []
for num in numbers:
    if is_even(num):
        even_numbers.append(num)
print("Evens:", even_numbers)

print(" ")
print("Task 4:")
s = "abracadabra"
freq = {}
for char in s:
    if char in freq:
        freq[char] +=1
    else:
        freq[char] = 1
print(freq)

print(" ")
print("Task 5:")
def clip(x, lo, hi):
    if x < lo:
        return lo
    elif x > hi:
        return hi
    else:
        return x
print(clip(5, 1, 10))    
print(clip(-3, 0, 10))  
print(clip(15, 0, 10))

print(" ")
print("Task 6:")
table = ""
for i in range(1, 6):
    for j in range(1, 6):
        table += "{:3}".format(i*j)  
    table += "\n"

print(table)

print(" ")
print("Task 7:")
def to_bin_str(n):
    return bin(n)[2:]

print(to_bin_str(5))   
print(to_bin_str(10))  
print(to_bin_str(0)) 