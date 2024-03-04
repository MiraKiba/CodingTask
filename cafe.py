# Step 2: Create a list called menu
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Step 3: Create a dictionary called stock
stock = {
    "Coffee": 100,    # Stock value for Coffee
    "Tea": 80,        # Stock value for Tea
    "Sandwich": 50,   # Stock value for Sandwich
    "Cake": 20        # Stock value for Cake
}

# Step 4: Create a dictionary called price
price = {
    "Coffee": 2.50,   # Price for Coffee
    "Tea": 2.00,      # Price for Tea
    "Sandwich": 5.00, # Price for Sandwich
    "Cake": 3.50      # Price for Cake
}

# Step 5: Calculate the total stock worth
total_stock_worth = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Step 6: Print out the result
print("Total Stock Worth in the Cafe: $", total_stock_worth)