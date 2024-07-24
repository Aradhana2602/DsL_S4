# Linear Search
def linear_search(x,key):
    for i in range(len(x)):
        if x[i]==key:
            return i
        
    return -1


#SENTINEL SEARCH
def sentinel_src(x,key):
    x.append(key)
    i=0
    while(x[i]!=0):
        i=+1
        if(i<n):
            return i
        else :
            return -1




n=int(input("number of roll no:"))


key=int(input("RollNo to implement linear search:"))
x=[]
while n>0:
    rollno=int(input("enter the roll no:"))
    x.append(rollno)
    n-=1
index =linear_search(x,key)
if index!=-1:
    print(f"Roll number found at index{index}.")
else:
    print("Element not found  ")

# BINARY SEARCH
x.sort()
def binarySearch(x,key):
        n=len(x)
        low=0
        high=n
        while(low<=high):
            mid=int((low+high)/2)
            if(x[mid]==key):
                return mid
            elif(x[mid]>key):
                high=mid-1
            else:
                low=mid+1
                
        return low
    

qw=binarySearch(x,key)
print("BINARY SEARCH",qw)
print("LINEAR SERACH",sentinel_src(x,key))





