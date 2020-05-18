#task-1.5
#Given two Python sets, update first set with items that exist only in the first set and not in the second set .
#S1={1,2,3,4,5,6,7,8,9}
#S2={1,3,4,6,8,11,22,34,51,67}
s1=set(map(int,input("Enter the Elements of Set1 each elements is separated by comma',':").split(",")))
s2=set(map(int,input("Enter the Elements of Set2 each elements is separated by comma',':").split(",")))
s1.update(s1.difference(s2))
print(f"First set is updated with items that exist only in the first set and not in the second set: {s1}")