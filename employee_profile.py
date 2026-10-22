"""Employee Profile Generator: a Python strings workshop project."""

# Store the employee's name and combine it with a space.
first_name = 'John'
last_name = 'Doe'
print(first_name)
print(last_name)

full_name = first_name + ' ' + last_name
print(full_name)

# Append an apartment number to the address.
address = '123 Main Street'
address += ', Apartment 4B'
print(address)

# Convert integers to strings before concatenating them with text.
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# Use an f-string to build the employee card.
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

# Extract parts of the employee code with string slicing.
employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
initials = employee_code[9:11]
print(year_code)
print(initials)

last_three = employee_code[-3:]
print(last_three)
