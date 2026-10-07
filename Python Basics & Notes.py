name = "Ahmed"
age = 20
height = 175.5
student = True

print(type(age))

# =================================================


print("Hello Python")
print(10)


# =================================================


x = 10
y = 3
print(x + y) # 13
print(x - y) # 7
print(x * y) # 30
print(x / y) # 3.3333333333333335
print(x // y) # 3
print(x % y) # 1
print(x ** y) # 1000


# =================================================

x = 10
print(x == 10) # True
print(x > 5) # True
print(x < 5) # False


# =================================================

age = 20
print(age >= 18 and age <= 30)

age = 15
print(age < 18 or age > 60)

x = True
print(not x)

# =================================================
print("=================================================")

text = "Python Programming"
print(text.startswith("Python"))
file_name = "Python.py"
print(file_name.endswith(".py"))

# =================================================
print("=================================================")


my_set = {1, 2, 3}
x = my_set.pop()
print(x)
print(my_set)


# =================================================
print("=================================================")

student = {
"name": "Mahmoud",
"age": 20,
"grade": 90
}
print(student["name"])


print(student.keys())
print(student.values())
print(student.items())
for key, value in student.items():
    print(key, value)
    
    
    
# =================================================
print("=================================================")


fruits = ["apple", "banana", "orange"]
for i, fruit in enumerate(fruits):
    print(i, fruit)