# Step 1: Create a dictionary to store medical costs
medical_costs = {}
medical_costs['Marina'] = 6607.0
medical_costs['Vinay'] = 3225.0
medical_costs.update({'Connie': 8886.0, 'Isaac': 16444.0, 'Valentina': 6420.0})
print(medical_costs)

# Step 2: Update Vinay's medical cost
medical_costs['Vinay'] = 3325.0

# Step 3: Calculate the average insurance cost
total_cost = 0
for cost in medical_costs.values():
  total_cost += cost
average_cost = total_cost / len(medical_costs)
print(f'Average Insurance Cost: {average_cost}')

# Step 4: Create a dictionary mapping names to ages
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]
zipped_ages = zip(names, ages)
names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

# Step 5: Get Marina's age
marina_age = names_to_ages.get('Marina', None)
print(f'Marina\'s age is {marina_age}')
