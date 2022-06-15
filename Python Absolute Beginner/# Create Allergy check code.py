# Create Allergy check code

# [ ] get input for input_test variable
print("Enter a food you have eaten in the last 24 hours")
input_test= input()
print(input_test)

# [ ] print "True" message if "dairy" is in the input or False message if not
print("Dairy Check?","Dairy".lower() in input_test.lower())

# [ ] print True message if "nuts" is in the input or False if not
print("Nut Check?","Nuts".lower() in input_test.lower())

# [ ] Challenge: Check if "seafood" is in the input - print message
print("Seafood Check?","Seafood".lower() in input_test.lower())

# [ ] Challenge: Check if "chocolate" is in the input - print message
print("Chocolate Check?","Chocolate".lower() in input_test.lower())