# Define a list of student names
studentName = ["Yasowant", "Mayank", "Zahira", "Disney"]

# Print the entire list
print(studentName)  
# Output: ['Yasowant', 'Mayank', 'Zahira', 'Disney']

# Print the first element of the list
print(studentName[0])  
# Output: Yasowant

# Print the last element of the list
print(studentName[-1])  
# Output: Disney

# Update the third element in the list
studentName[2] = 'Kiran'
print(studentName)  
# Output: ['Yasowant', 'Mayank', 'Kiran', 'Disney']

# Append a new name to the list
studentName.append("Puja")
print(studentName)  
# Output: ['Yasowant', 'Mayank', 'Kiran', 'Disney', 'Puja']

# Remove the last element from the list
studentName.pop()
print(studentName)  
# Output: ['Yasowant', 'Mayank', 'Kiran', 'Disney']

# Check if "Yasowant" is in the list and print a message
if "Yasowant" in studentName:
    print("is Present")  
# Output: is Present

# Check if "Puja" is in the list and print a message
if "Puja" in studentName:
    print("is Present")  # No Output, since "Puja" was removed earlier

# Insert a new name at the third position (index 2)
studentName.insert(2, "Vikash")
print(studentName)  
# Output: ['Yasowant', 'Mayank', 'Vikash', 'Kiran', 'Disney']

# Remove "Yasowant" from the list
studentName.remove("Yasowant")
print(studentName)  
# Output: ['Mayank', 'Vikash', 'Kiran', 'Disney']

# Generate a list of squared numbers using list comprehension
squared_num = [x ** 2 for x in range(10)]
print(squared_num)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
