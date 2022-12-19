# Prompt the user to enter the vehicle type
vehicle_type = input("Enter the vehicle type (S - Saloon, HP - High Performance, V - Van): ")

# Validate the vehicle type input
while vehicle_type not in ["S", "HP", "V"]:
  print("Error: Invalid vehicle type. Please enter a valid vehicle type (S, HP, or V).")
  vehicle_type = input("Enter the vehicle type (S - Saloon, HP - High Performance, V - Van): ")

# Prompt the user to enter the number of days hire required
days_hire = input("Enter the number of days hire required (max. limit 10 days): ")

# Validate the number of days hire input
while not days_hire.isdigit() or int(days_hire) > 10:
  print("Error: Invalid number of days hire. Please enter a positive integer less than or equal to 10.")
  days_hire = input("Enter the number of days hire required (max. limit 10 days): ")
days_hire = int(days_hire)

# Prompt the user to enter if insurance cover is required
insurance_cover = input("Enter if insurance cover is required (Yes or No): ")

# Validate the insurance cover input
while insurance_cover not in ["Yes", "No"]:
  print("Error: Invalid insurance cover input. Please enter 'Yes' or 'No'.")
  insurance_cover = input("Enter if insurance cover is required (Yes or No): ")

# Prompt the user to enter if quote is for a new or existing customer
customer_type = input("Enter if quote is for a new or existing customer (new or existing): ")

# Validate the customer type input
while customer_type not in ["new", "existing"]:
  print("Error: Invalid customer type input. Please enter 'new' or 'existing'.")
  customer_type = input("Enter if quote is for a new or existing customer (new or existing): ")

# If the customer type is "existing", prompt the user to enter the loyalty card type
if customer_type == "existing":
  loyalty_card_type = input("Enter the loyalty card type (Bronze, Silver, or Gold): ")

  # Validate the loyalty card type input
  while loyalty_card_type not in ["Bronze", "Silver", "Gold"]:
    print("Error: Invalid loyalty card type. Please enter 'Bronze', 'Silver', or 'Gold'.")
    loyalty_card_type = input("Enter the loyalty card type (Bronze, Silver, or Gold): ")

# Calculate the total hire cost
daily_charges = {"S": 22.50, "HP": 28.00, "V": 35.00}
total_hire_cost = daily_charges[vehicle_type] * days_hire
if days_hire > 7:
  total_hire_cost *= 0.9
if customer_type == "existing" and loyalty_card_type == "Gold" and vehicle_type == "HP":
  total_hire_cost -= 18.00
if insurance_cover == "Yes":
  total_hire_cost += 15.50
total_hire_cost += 50

# Display a summary of the car hire quote
print(f"{total_hire_cost}")
