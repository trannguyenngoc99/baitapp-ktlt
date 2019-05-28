#giai huong trinh bac hai
a = float(input("Nhap vao a : "))
b = float(input("Nhap vao b : "))
c = float(input("Nhap vao c : "))
if a == 0 :
    print("Phuong trinh bac nhat")
else:
    d = b**2-4*a*c;
    if d<0:
        print("Phuong trinh vo nghiem")
    elif d==0 :
        print("Phuong trinh co nghiem kep ",-b/(2*a))
    else :
        x1 = (-b - sqrt(d))/(2*a)
        x2 = (-b + sqrt(d))/(2*a)
        printf("Phuong trinh co hai nghiem : \n",x1,"\n",x2)
