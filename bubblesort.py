def bubblesort(list):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i]>list[j]:
                list[i],list[j]=list[j],list[i]
    print("sorted list:",list)
                
                
list=[]
m=int(input("enter the size of the list:"))
print("enter the elements into the list:")
for i in range(m):
    list.append(int(input()))
bubblesort(list)


