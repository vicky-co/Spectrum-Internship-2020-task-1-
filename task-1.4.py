#task-1.4
#Get the key corresponding to the minimum value from the following dictionary using appropriate python logic.
#sample={
#‘physics’, 88 ,  ‘maths’, 75,  ’chemistry’ , 72,’Basic electrical’ , 89 
#}
l=list(input("Enter elements one by one separated by comma ',':").split(','))#enter the elements 1st key then their value separated by comma ","
l1=[l[i] for i in range(0,len(l),2)]#stores all the keys
l2=[l[i] for i in range(1,len(l),2)]#stores all the values
dic={}#dictionary which stores all the key with their values
m=min(l2)#stores the minimum value in l2
for i,j in zip(l1,l2): 
	dic[i]=int(j)#keys and values are added 
for x,y in dic.items():
    if(int(y)==int(m)):#finds the key corresponding to the minimum value
        print(f"The key correspinding to the minimun value ({y}) ={x}")#print the output
