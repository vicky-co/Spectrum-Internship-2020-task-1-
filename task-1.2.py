#task-1.2
#Given input String of combination of the lower and upper case ,arrange characters in such a way that all lowercase letters should come first.
def caselu():
    s=input("Enter The String:")#stores the string 
    l,u=[],[]#l stores the all lower case letters and u stores the upper case letters
    for i in s:
        if(i.islower()):
            l.append(i)#all lowercase letters are added one by one
        else:
            u.append(i)#all uppercase letters are added one by one
    v=l+u #stores 1st the lowercase letters then uppercase letters
    print("Output=",end='')
    print(''.join(v)) #print the output
if __name__=='__main__':
    caselu() #call the caselufunction		    	

