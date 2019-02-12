n = 1
s1 = "Critical"
s2 = "Damage"
for n in range(100):
    if(n%5==0 and n%3==0):
        print(s1 + " " + s2)
    elif(n%5==0):
        print(s2)
    elif(n%3==0):
        print(s1)
    else:
        print(n)
        
