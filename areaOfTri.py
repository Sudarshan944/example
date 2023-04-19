n=int(input("Enter value 1->triangle 2->rectangle 3->square"))
base=int(input("Enter base value :"))
if(n==1):
    height=int(input("Enter height value :"))
    area=0.5*base*height
elif(n==2):
    height = int(input("Enter height value :"))
    area=base*height
else:
    area=base*base
print("Area :",area)
