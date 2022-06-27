word=""
quote=input("enter a 1 sentence quote, non-alpha seperate words: ")
for letter in quote.lower():
    if letter.isalpha() == True:
        word+=letter
    else: 
        if word.lower() > "g" :
            print(word.upper())
            word=""
        else :
            word=""
