def hotel_cost(num_nights):
    # Assuming a hotel cost of $100 per night
    return num_nights * 100

def plane_cost(city_flight):
    # Prices for different cities
    if city_flight == "New York":
        return 300
    elif city_flight == "Los Angeles":
        return 250
    elif city_flight == "London":
        return 400
    else:
        return 200

def car_rental(rental_days):
    # Assuming a daily car rental cost of $50
    return rental_days * 50

def holiday_cost(city_flight, num_nights, rental_days):
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost

# User inputs
city_flight = input("Enter the city you will be flying to (New York, Los Angeles, London, etc.): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

# Calculate total holiday cost
total_cost = holiday_cost(city_flight, num_nights, rental_days)

# Print holiday details
print("\nHoliday Details:")
print("Destination: ", city_flight)
print("Number of Nights in Hotel: ", num_nights)
print("Number of Days for Car Rental: ", rental_days)
print("Total Holiday Cost: $", total_cost)