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


# Step 6: Create detailed medical records for each individual
medical_records = {}
medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records['Vinay'] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records['Connie'] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records['Isaac'] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 6420.0}
medical_records['Valentina'] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)


# Step 7: Print Connie's insurance cost
print(f"Connie's insurance cost is {medical_records['Connie']['Insurance_cost']} dollars")

# Step 8: Remove Vinay from medical records
medical_records.pop('Vinay')
print(medical_records)

# Step 9: Print a summary for each individual
for key, info in medical_records.items():
  print(f"{key} is a {info['Age']} year old {info['Sex']} {info['Smoker']} with a BMI of {info['BMI']} and insurance cost of {info['Insurance_cost']}")

# Step 10: Define a function to update/add medical records
def update_medical_records(name, age, sex, bmi, children, smoker_status, insurance_cost):
    medical_records[name] = {
        'Age': age,
        'Sex': sex,
        'BMI': bmi,
        'Children': children,
        'Smoker': smoker_status,
        'Insurance_cost': insurance_cost

# Step 11: Add Salma to the records
update_medical_records('Salma', 35, 'Female', 23.1, 1, 'Non-smoker', 5327.0)
print(medical_records['Salma'])

# Step 12: Create a separate dictionary for fitness goals
fitness_goals = {
  'Lina': {'Goal': 'gain some muscle mass', 'Weekly Exercise Hours': 8},
  'George': {'Goal': 'Lose weight', 'Weekly Exercise Hours': 10}


# Step 13: Print Lina's fitness goal
print(f"Lina wants to {fitness_goals['Lina']['Goal']} and exercises {fitness_goals['Lina']['Weekly Exercise Hours']} hours per week.")

