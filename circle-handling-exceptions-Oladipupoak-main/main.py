user_input = input("Please enter a number for radius: ")
try:
    radius = float(user_input)
    area = 3.14 * radius * radius
    print("The area of the circle is: ", area)
except:
    print("Not a number")






