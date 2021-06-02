A Program to check if strings are rotations of each other or not?

str1 = "ABACD"
str2 = "CDABA"

def isRotation(S1,S2):
    S1+=S1
    return S1.count(S2)
    
    
print(isRotation(str1, str2))
