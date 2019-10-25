# list1= [1,2,3,4,77]
# list2 =[1,2,3,5,67,77]

# def comman(list1,list2,list3=[]):
# 	for found in list1:
# 		if found in list2:
# 			list3.append(found)
# 	return list3

# print("THIs is comman in both the list" , comman(list1,list2))


# min max
# list1 = [10,20,40]
# print "this is minimum value", min(list1)

list1=[1,2,3,[4,5,6],[10,20,40]]
j = 0
for i in list1:
    if type(i) == list:
        j= j + 1
print(j)
