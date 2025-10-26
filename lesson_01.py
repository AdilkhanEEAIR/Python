# Пример 1. Присваивание, перепривязка, множественное присваивание
print("Example 1:")
x = 10
y = x       # y ссылается на тот же объект, что и x
x = x + 5   # теперь x указывает на новый объект (15)
x, y, z = 1, 2, 3
x, y = y, x  # swap
print("x, y, z =", x, y, z)

# Пример 2. == vs is
print("Example 2:")
a = 256
b = 256
print("a == b:", a == b)      # значения равны
print("a is b:", a is b)      # может быть True из-за интернирования малых целых
c = 300
d = 300
print("c == d:", c == d)
print("c is d:", c is d)      # тождества, как правило, нет
s1 = "hello"
s2 = "he" + "llo"
print("s1 == s2:", s1 == s2)
print("s1 is s2:", s1 is s2)  # тождество не гарантируется — полагайтесь на '=='

# Пример 3. Индексация/срезы/методы
print("Example 3:")
s = "sublime"
print("s[0], s[-1] =>", s[0], s[-1])
print("s[1:4] =>", s[1:4])
print("s[-4:] =>", s[-4:])
print('replace:', s.replace("li", "te"))
print("повтор:", "la " * 3)
# Демонстрация неизменяемости:
try:
    s[0] = "S"
except TypeError as e:
    print("Нельзя изменить символ по индексу:", e)
    
# Пример 4. f-строки и приведение типов
print("Example 4:")
name = "Adilkhan"
age = 19
print("Конкатенация:", "Меня зовут " + name + ", мне " + str(age))
print(f"f-строка: Меня зовут {name}, мне {age}")
value = 5/3
print(f"Округление в выводе: {value:.2f}")

# Пример 5. Арифметика и функции
print("Example 5:")
print("5 + 9.03 =", 5 + 9.03)
print("10 * (3 + 7) =", 10 * (3 + 7))
print("17 // 4 =", 17 // 4, " (целочисленное деление)")
print("17 % 4 =", 17 % 4, " (остаток)")
print("2 ** 10 =", 2 ** 10)
print("abs(-9) =", abs(-9))
print("max(3,6,9) =", max(3,6,9), "; min(...) =", min(3,6,9))
print("pow(3,3) =", pow(3,3))
print("bin(70) =", bin(70))
# round: посмотрите реальные результаты округления на примерах
for v in [9.4, 9.5, 10.5]:
    print("round(", v, ") =", round(v))


# Пример 6. Логика и членство
print("Example 6:")
a, b = 10, 15
print("a < b and b >= 15 =>", a < b and b >= 15)
colors = ["red", "green", "blue"]
print("'green' in colors:", "green" in colors)
text = "Hello, world"
print("'world' in text:", "world" in text)
x = [1,2,3]; y = [1,2,3]
print("x == y:", x == y, "; x is y:", x is y)

# Пример 7. Мини-калькулятор (без внешних библиотек)
print("Example 7:")
def calc(a_str, b_str, op):
    a = float(a_str) if "." in a_str else int(a_str)
    b = float(b_str) if "." in b_str else int(b_str)
    if op == "+": return a + b
    if op == "-": return a - b
    if op == "*": return a * b
    if op == "/": return a / b
    raise ValueError("Неизвестная операция")
print(calc("5", "10", "+"))
print(calc("5.5", "1.2", "+"))

# Пример 8. Локальная и глобальная область видимости
print("Example 8:")
v = "dogs"
def funcscope():
    v = "birds"   # локальная
    return "Внутри функции: " + v
print(funcscope())
print("Вне функции:", v)

# Пример 9. Несколько полезных встроенных функций
print("Example 9:")
print("bool('') =", bool(''), "; bool('x') =", bool('x'))
print("len('python') =", len('python'))
print("list('abc') =", list('abc'))
print("sorted([3,1,2]) =", sorted([3,1,2]))
print("sum([1,2,3]) =", sum([1,2,3]))