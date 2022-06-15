# project: "guess what I'm reading"

# 1[ ] get 1 word input for can_read variable
print("P1: Enter what you are reading")
can_read=input()

# 2[ ] get 3 things input for can_read_things variable
print("P2: Guess what they are reading! (3 guesses)")
can_read_things=input()


# 3[ ] print True if can_read is in can_read_things
print("Item found?",can_read.lower() in can_read_things)

# [] challenge: format the output to read "item found = True" (or false)
# hint: look print formatting exercises
