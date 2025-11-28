salary=int(input("enter your monthly salary"))      
electricity1=int(input("enter electricity bill of last month"))
electricity2=int(input("enter electricity bill of this month"))
water1=int(input("enter water bill of last month"))
water2=int(input("enter water bill of this month"))
grocery_store1=int(input("enter grocery store bill of last month"))
grocery_store2=int(input("enter grocery store bill of this month"))
school1=int(input("enter school fees of last month"))
school2=int(input("enter school of this month"))
shopping1=int(input("enter shopping bill of last month"))
shopping2=int(input("enter shopping bill of this month"))
internet1=int(input("enter internet bill of last month"))
internet2=int(input("enter internet bill of this month"))
ott1=int(input("enter ott bill of last month"))
ott2=int(input("enter ott bill of this month"))
medical1=int(input("enter medical bill of last month"))
medical2=int(input("enter medical bill of this month"))

expences1=electricity1+water1+grocery_store1+school1+shopping1+internet1+ott1+medical1
expences2=electricity2+water2+grocery_store2+school2+shopping2+internet2+ott2+medical2
print("total expencess of last month : ",expences1)
print("total expencess of this month : ",expences2)

savings1=salary-expences1
savings2=salary-expences2
print("total savings of last month : ",savings1)
print("total savings of this month : ",savings2)

total_savings= savings1+savings2
total_expences=expences1+expences2
print("total expencess of both month : ",total_expences)
print("total savings of both month : ",total_savings)

l1=[electricity1,water1,grocery_store1,school1,shopping1,internet1,ott1,medical1]
a=electricity1
for i in l1:
    if (a<i):
        a=i
print(f"maximum expence of last month is of ",a)

l2=[electricity2,water2,grocery_store2,school2,shopping2,internet2,ott2,medical2]
b=electricity2
for j in l2:
    if (b<j):
        b=j
print(f"maximum expence of this month is of ",b)
