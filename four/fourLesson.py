# price = int(input("Enter ther price: "))
# print(price)
# print(type(price))

# a = True + True + False
# print(a)
# num1 = 2 > 1
# num2 = 1 == 3
# num3 = num1 == num2
# print(num3)
# a = num1 + num2
# print(a)

# num1 = 4
# num2 = 5
# print(num1 <= num2)


# age = int(input("Enter ur age: "))
# a = age % 10 == 0 or age >= 50
# print(a)

# name = 'Sara'
# if name == 'Bob':
#     print("Its male")
# else:
#     print("Its female")


# a = int(input("Enter a number: \n"))
# if a>0 and a == 5:
#     print("Positive 5")
# # elif a == 0:
# #     print("Zero")
# else:
#     print('Negative')
    
# person = input("Enter status of a person: \n")
# if person == 'student' or person == 'school 10th' or person == 'school 11th':
#     print(f"This man is over 15 y o because he is {person}")
# elif person == 'worker':
#     print(f"This man is over 15 y o because he is {person}")
# else:
#     print("He isnt over 15 y o")


try:
    age = int(input("Enter your age: \n"))
    if age < 18:
        print("You are a child")
    elif age >= 18 and age < 35:
        print("You are an adult")
    elif age >= 35 and age < 65:
        print("You are an elder")
    elif age >= 65:
        print("You are a pensioner")
    elif age <= 0:
        print("Age cant be lower or equal to zero, enter a correct")
except ValueError:
    print("Enter correct data")
    
word = 'people'
text = 'Hello my name is Sam'
list1 = [2, 4, 64, 6, 'name']
search = 'name'
if search in text:
    print(f"{search} in the text")
else:
    print(f"{search} is not in the text")
if search in list1:
    print(f"{search} is in the list")
else:
    print(f"{search} is not in the list")