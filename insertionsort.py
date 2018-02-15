def insertionsort(list):
    for i in range(1,len(list)):
        j=i
        while j>0 and list[j-1]>list[j]:
                list[j],list[j-1]=list[j-1],list[j]
                j=j-1
        print("list:",list,"after iteration:",i)
    print("sorted list:",list)



list=[]
m=int(input("enter the size of the list:"))
print("enter the elements into the list:")
for i in range(m):
    list.append(int(input()))
insertionsort(list)


