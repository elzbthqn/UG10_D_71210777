A = int(input("nilai a :"))
B = int(input("nilai b :"))
C = int(input("nilai c :"))

X = B**2 - 4*A*C
x1 = (-B+X**(1/2))/2*A 
x2 = (-B-X**(1/2))/2*A 

if X<0:
    print("Fungsi tersebut tidak memiliki akar riil")
elif X>0:
    print("Akar akar dari persamaan tersebut adalah",x2,"dan",x1)
else:
    print("Fungsi tersebut memiliki angka kembar yaitu",x1)