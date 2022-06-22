rooms = input("How many rooms do you want to carpet?")
#initial values
room_num = 0
total = 0

#convert_inches_to_feet = inches / 12
def convert_inches_to_feet(inches):
    feet = inches / 12
    return feet
#calculate_square_footage = width * length
def calculate_square_footage(width, length):
    squared = width_feet * length_feet
    return squared
#calculate_room_price = (convert_inches_to_feet * calculate_square_footage) * price
def calculate_room_price(square_foot,price_per_square_foot):
    price = round(square_foot * price_per_square_foot,2)
    return price
for i in range(int(rooms)):
    room_num = room_num+1

    length = input("What is the length of Room #" + str(room_num) + " in inches?")
    length_feet = convert_inches_to_feet(float(length))#length inches to feet
    print(length_feet)
    width = input("What is the width of Room #" + str(room_num) + " in inches?")
    width_feet = convert_inches_to_feet(float(width))#width inches to feet
    print(width_feet)
    square_foot = calculate_square_footage(width_feet,length_feet) #square footage call

    price_per_square_foot = input("What is the price of the carpet per square foot?")
    price = calculate_room_price(square_foot,float(price_per_square_foot))#price call

    print("This room will cost $"+str(price),"to carpet.")
    total = total+price#running price tally
print("The total price will be $"+str(total))
