# Define a string variable 'name'
name = "Yasowant Nayak"

# Get the first character of the string and print it
first_char = name[0]
print(first_char)  # Output: Y

# Print the original name
print(name)  # Output: Yasowant Nayak

# Extract the first 8 characters (substring from index 0 to 7) and print it
first_name = name[0:8]
print(first_name)  # Output: Yasowant

# Define a string containing numbers
number_list = "0123456789"

# Print the entire number_list string
print(number_list[:])  # Output: 0123456789

# Print the number_list string starting from index 0
print(number_list[0:])  # Output: 0123456789

# Print the first 6 characters of number_list
print(number_list[:6])  # Output: 012345

# Print characters from index 2 to 7 (excluding index 8)
print(number_list[2:8])  # Output: 234567

# Print every second character from index 0 to 6
print(number_list[0:7:2])  # Output: 0246

# Convert the name to lowercase and print it
print(name.lower())  # Output: yasowant nayak

# Convert the name to uppercase and print it
print(name.upper())  # Output: YASOWANT NAYAK

# Define a string with extra spaces
nameData = "  kiran  "

# Remove leading and trailing spaces and print the result
print(nameData.strip())  # Output: kiran

# Replace "Kiran" with "Disney" and print the result
# Note: The replace function is case-sensitive, so this will not replace anything
print(nameData.replace("Kiran", "Disney"))  # Output:   kiran  

# Print the original nameData to show it remains unchanged
print(nameData)  # Output:   kiran  


# Define a string of student names separated by commas
student = "Yasowant,Mayank,Zahira,Disney,kiran"

# Split the string by default whitespace delimiter and print the result
print(student.split())  
# Output: ['Yasowant,Mayank,Zahira,Disney,kiran']
# Since there is no whitespace in the string, it remains as a single element.

# Split the string by ',' (comma as delimiter) and print the result
print(student.split(","))  
# Output: ['Yasowant', 'Mayank', 'Zahira', 'Disney', 'kiran']
