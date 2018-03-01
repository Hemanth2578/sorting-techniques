def mergesort(list):
   if len(list)>1:
      mid=len(list)//2
      left=list[:mid]
      right=list[mid:]
      mergesort(left)
      mergesort(right)
      i,j,k=0,0,0
      while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k]=left[i]
                i=i+1
            else:
                list[k]=right[j]
                j=j+1
            k=k+1

      while i < len(left):
            list[k]=left[i]
            i=i+1
            k=k+1

      while j < len(right):
            list[k]=right[j]
            j=j+1
            k=k+1
   print("Merging ",list)

    
    
list=[]
n=int(input("enter the length of the list:"))
print("Enter the elements into the list:\n")
for i in range(n):
   list.append(int(input()))
mergesort(list)

   
