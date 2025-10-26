# Home Work 1 Python*

# Task 1
print("Task 1:")
x = [1,2,3]
y = [1,2,3]
print("x == y:", x == y)  # True, потому что значения одинаковы
print("x is y:", x is y)  # False, потому что объекты разные в памяти
print()

# Task 2
print("Task 2:")
def c_to_f(c):
    return round(c * 9/5 + 32, 1) #по формуле перевод цельсий в фаренгейт
def f_to_c(f):
    return round((f - 32) * 5/9, 1)

c = float(input("Enter temp in C: "))
f = float(input("Enter temp in F: "))
print(f"{c}°C = {c_to_f(c)}°F")
print(f"{f}°F = {f_to_c(f)}°C")
print()

# Task 3
print("Task 3:")
text = input("Enter a string to count characters: ").lower()
# создаем словарь, затем проходим по циклу и делаем подсчет
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True) # превращаем в tuple, чтобы было ключ-значение, где числа - значения
print("5 chars:", sorted_freq[:5])
print()

# Task 4
print("Task 4:")
def is_strong(pwd):
    if len(pwd) <8: # меньше 8
        return False
    if any(c.isspace() for c in pwd): # пробелы
        return False
    if not any(c.islower() for c in pwd): #нижний регистр
        return False
    if not any(c.upper() for c in pwd): # верхний регистр
        return False
    if not any(c.isdigit() for c in pwd): # на число
        return False
    return True

passwords = ["Password1", "weak", "12345678", "NoDigits!", "StrongPass9", "A1 bC3", "Valid123"] #проверки паролям

for pwd in passwords:
    print(f"{pwd}: {is_strong(pwd)}")
print()
    
# Task 5
print("Task 5:")
def eval_simple(expr):
    parts = expr.split()
    if len(parts) != 3:
        return "Incorrect Expression"
    
    a_str, op, b_str = parts

    # проверяем числа вручную
    def is_number(s):
        if s.count('.') <= 1:
            s2 = s.replace('.', '', 1)
            if s2.isdigit():
                return True
        return False

    if not (is_number(a_str) and is_number(b_str)):
        return "Error: A and B should be a nums"

    # преобразуем
    a = float(a_str) if '.' in a_str else int(a_str)
    b = float(b_str) if '.' in b_str else int(b_str)

    #  операции
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': 
        if b == 0: return "Error, dont divide by 0"
        return a / b
    if op == '//':
        if b == 0: return "Error, dont divide by 0"
        return a // b
    if op == '%':
        if b == 0: return "Error, dont divide by 0"
        return a % b
    if op == '**': return a ** b

    return "Unknown operator"

print(eval_simple("10 + 5"))   
print(eval_simple("7 // 3"))   
print(eval_simple("2 ** 4"))   
print(eval_simple("5 / 0"))    
print(eval_simple("abc + 5"))  
print()

# Task 6
print("Task 6:")
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
print()

# Task 7
print("Task 7:")
table = ""
for i in range(1, 11):
    for j in range(1, 11):
        table += "{:4}".format(i*j) #выравнивание и умножение   
    table += "\n" #отступ вниз по строкам

print(table)
print()

# Task 8
print("Task 8:")
def to_bin_str(n, width=0):
    s = bin(n)[2:]         # -'0b'
    if width > 0:
        s = s.zfill(width)
    return s

print(to_bin_str(5))       
print(to_bin_str(5, 8))    
print(to_bin_str(255, 8))  
print()

# Task 9
print("Task 9:")
nums = list(range(1, 101)) #список
filtered = [x for x in nums if (x % 3 == 0) ^ (x % 5 ==0)] #условие через xor
print("Filtered nums:", filtered)
print()

# Task 10
print("Task 10:")
def read_number(prompt):
    while True:
        val = input(prompt).strip()
        # проверяем float
        if val.replace('.', '', 1).isdigit():
            if '.' in val:
                return float(val)
            else:
                return int(val)
        else:
            print("Error! enter a num!")

num = read_number("Enter a num: ")
print("You input:", num)
print()