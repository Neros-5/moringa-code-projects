# Prompts User for Input for Size of the Pizza Ordered
print("What Size of a Pizza is needed?")
size = input("Enter 'Small' for a small size or 'Large' for a Large size Pizza: ")

# Loop to check paramaters of Pizza size, and assign cost based on the given answer
while True:
    if size == "Small" or size == "small":
        cost1 = 8
        break
    elif size == "Large" or size == "large":
        cost1 = 12
        break
    else:
        print("Invalid Parameter, enter correct Size.")
        size = input("Enter 'Small' for a small size or 'Large' for a Large size Pizza: ")


# Prompts User for Input for Number of the Toppings Ordered on the Pizza
toppings = int(input("How many Toppings was the Pizza order needed?: "))

# Conditions to check paramaters of number of Topppings, and assign cost based on the given answer
if toppings == 0:
    cost2 = 0
else:
    cost2 = toppings

# Prompts User for Distance from Business to Customer Location in Miles
location = int(input("What is the distance in miles, from here to the customer location?: "))

# Loop to check paramaters of Location, and assign cost based on the given answer
while True:
    if location == 0:
        cost3 = 0
        break
    elif location <= 5:
        cost3 = 2
        break
    elif location <= 15:
        cost3 = 2 + (location - 5)
        break
    else:
        print("Location Distance is too far to be delivered. Check and Try again.")
        location = int(input("What is the distance in miles, from here to the customer location?: "))

# Takes the cost of each parameter, adds them together and Outputs the total.
total = cost1 + cost2 + cost3
print(f"The Total cost for the Order is: ${total}")