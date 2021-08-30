import random
a = random.randint(0,49)
b = random.randint(0,50)
c=a+b
# print(a,"+",b,"=")
d=int(input(a,"+",b,"="))
if(c==d):
    print("Verified User")
else:
    print("Unverified User")