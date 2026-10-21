
# Pizza Order Cost Calculator
# This program calculates the cost of a pizza, extra toppings, and delivery.

# Ask the customer for their pizza size.
pizza_size = input("Choose a pizza size (small or large): ").strip().lower()

# Decide the base price based on pizza size.
if pizza_size == "small":
    base_cost = 8
elif pizza_size == "large":
    base_cost = 12
else:
    print("Invalid pizza size. Please enter small or large.")
    raise SystemExit

# Ask for the number of extra toppings and delivery distance.
# Use 0 miles if the customer will pick up the pizza.
try:
    toppings = int(input("How many extra toppings? "))
    distance = int(input("Delivery distance in whole miles (0 for pickup): "))
except ValueError:
    print("Invalid input. Enter whole numbers for toppings and distance.")
    raise SystemExit

# Make sure the customer did not enter negative numbers.
if toppings < 0 or distance < 0:
    print("Toppings and delivery distance cannot be negative.")
    raise SystemExit

# Each extra topping costs $1.
toppings_cost = toppings * 1

# Work out the delivery fee.
if distance == 0:
    delivery_fee = 0
elif distance <= 5:
    delivery_fee = 2
else:
    delivery_fee = 2 + (distance - 5) * 1

# Add all costs to get the final price.
total_cost = base_cost + toppings_cost + delivery_fee

# Show the order summary using f-strings.
print("\n--- Pizza Order Summary ---")
print(f"Pizza size: {pizza_size.title()}")
print(f"Base cost: ${base_cost:.2f}")
print(f"Toppings ({toppings}): ${toppings_cost:.2f}")
print(f"Delivery ({distance} miles): ${delivery_fee:.2f}")
print(f"Total cost: ${total_cost:.2f}")
