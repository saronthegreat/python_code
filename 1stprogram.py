# """ """
# python is dynamicly typed
name = "Saron"
age = 88
location = "Dillibazar"
# concate
print("My name is " +name + "age is " +str(age)+"Location is" +location)
# f string
print(f"My name is {name} and age is {age} and Location is {location}")
# format old version
print("My name is %s and age is %d and Location is %s" %(name, age, location))
# format new version
print("My name is {0} and age is {1} and location is {2}".format(name, age, location))

num1 = int(input("Enter the number1"))
num2 = int(input("Enter the number2"))
sum1 = num1 + num2
print("The sum is" +sum1 + "and the type is" + type(sum1))

num3 = (input("Enter the number1"))
num4 = (input("Enter the number2"))
sum2 = num3 + num4