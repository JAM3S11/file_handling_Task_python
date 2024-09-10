# FILE CREATION
file = open("my_file.txt", "w")
file.write('''
           Hello PLP May 2024 Cohort
           Specialization in Python
           This is a file based on file handling in Python.''')
file.close()

# FILE READING AND DISPLAY
file = open("my_file.txt", "r")
output = file.read()
print(output)
file.close()

# APPENDING
file = open("my_file.txt", "a")
file.write('''
           It entails File Creation,
           Reading and Appending
           Accompanied with error handling.''')
file.close()

# ERROR HANDLING FileNotFoundError, PermissionError
try:
    file = open("my_file.txt")
    output = file.read()
except FileNotFoundError as e:
    print("File not found: ", e)
except PermissionError as e:
    print("Permission denied: ", e)
else: 
    print(output)
finally:
    file.close()