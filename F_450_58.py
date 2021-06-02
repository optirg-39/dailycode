Print all the duplicates in the input string?

#Using Hashing
r="Rishabhrishabh"

def strigduplcate(S):
    d={}
    for i in S:
        d[i]=S.count(i)
    
print(strigduplcate(r))
