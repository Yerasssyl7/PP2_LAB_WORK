def polind(s):
    n = s[::-1]
    
    if s == n:
        return "Polindrome"
    else:
        return "Not a polindrome"
    
s = input()

print(polind(s))

#n = s[::-1]
#if (s == n):
#    print("Polindrome")
#else:
#    print("Not polindrome")
#qwerty