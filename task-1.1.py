#task-1.1
#Create an inner function to calculate the addition in the following way
#•	Create an outer function that will accept two parameters ‘a’ and ‘b’ 
#•	Create an inner function inside an outer function that will calculate the addition of ‘a’ and ‘b’ 
#•	At last, an outer function will add 5 into addition and return it


def outer():
	#this outer()adds 5 to the value returned by inner()
    a=int(input("Enter The value for a:"))#stores the value of a
    b=int(input("Enter the value for b:"))#stores the value of b
    def inner():
    	#this inner() return the addition of a and b
        s=a+b #stores the adittion of a and b
        return s #return the sum of a and b
    s=inner()+5 #calls the inner() and add 5 to it
    return (f"Answer={s}") #return the main result after adding 5 to the sum of a and b
if __name__ == '__main__':
    print(outer())#print the result of outer()
	