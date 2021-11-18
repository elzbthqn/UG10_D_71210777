a = int(input("Masukkan bilangan 1 : "))
b = int(input("Masukkan bilangan 2 : "))
c = int(input("Masukkan bilangan 3 : "))
if a > b > c:
    print("Urutan bilangan dari yang terbesar adalah",a,b,c)
elif b > a > c:
    print("Urutan bilangan dari yang terbesar adalah",b,a,c)
elif a > c > b:
    print("Urutan bilangan dari yang terbesar adalah",a,c,b)
elif b > c > a:
    print("Urutan bilangan dari yang terbesar adalah",b,c,a)
elif c > b > a:
    print("Urutan bilangan dari yang terbesar adalah",c,b,a)
elif c > a > b:
    print("Urutan bilangan dari yang terbesar adalah",c,a,b)
elif a == b > c:
    print("Urutan bilangan dari yang terbesar adalah",a,b,c)
elif a > b == c:
    print("Urutan bilangan dari yang terbesar adalah",a,b,c)
elif a == c > b:
    print("Urutan bilangan dari yang terbesar adalah",a,c,b)
elif a > c == b:
    print("Urutan bilangan dari yang terbesar adalah",a,c,b)
elif c > a == b:
    print("Urutan bilangan dari yang terbesar adalah",c,a,b)
elif b > a == c:
    print("Urutan bilangan dari yang terbesar adalah",b,a,c)
elif c == b > a:
    print("Urutan bilangan dari yang terbesar adalah",c,b,a)
else:
    a == b == c
    print("Urutan bilangan dari yang terbesar adalah",a,b,c)