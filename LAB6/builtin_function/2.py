def letters(s):
    
    
    capital_letter = 0
    small_letter = 0
    
    for i in s:
        if (i >= 'A' and i <= 'Z'):
            capital_letter += 1
        elif(i >= 'a' and i <= 'z'):
            small_letter += 1   
        
    return capital_letter, small_letter

s = input()

capital, small = letters(s)

print("КОЛИЧЕСТВО ЗАГЛАВНЫХ БУКВ:", capital)

print("КОЛИЧЕСТВО СТРОЧНЫХ БУКВ:", small)

# for i in s:
#    if (i >= 'A' and i <= 'Z'):
#        capital_letter += 1
#    if (i >= 'a' and i <= 'z'):
#        small_letter += 1
#        
#print(capital_letter , " ", small_letter)

#qwerty