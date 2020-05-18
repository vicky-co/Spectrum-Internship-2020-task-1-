#task-1.3
#Given a Python list, remove all the even number from the list and save those even number in another list and print both the lists.
#For a given input list:  List1 = [1,2,3,4,5,6,7]
#Output : List1=[1,3,5,7]

#	      List2 = [2,4,6]
def listevod():
    print("Enter the elements of list in a line, Example=1 2 etc")
    l1=list(map(int,input().split()))#stores all the numbers 
    l2,l3=[],[]#l2  will stores the even numbers and l3  will stores odd numbers 
    for i in range(0,len(l1)):
        if(l1[i]%2==0):
            l2.append(l1[i])#all even numbers are added one by one
        else:
            l3.append(l1[i])#all odd numbers are added one by one
    l1=l3 #l1 stores the all odd number which are present in l1       
    print("List1={}".format(l1))#print list 1
    print(f"List2={l2}")#print list 2
if __name__=='__main__':
    listevod()#calls listevod()