list1 = ['abc','def']
# revese_list = []
# for char in list1:
#     revese_list.append(char[::-1])
# print(revese_list)

# def reverse(list1):
#     return [char[::-1] for char in list1]
# print(reverse(list1))

# def reverse(s): 
#   str = "" 
#   for i in s:
#       str = i + str
#   return str
# print(reverse('abc'))
# print(type([i for i in range(1,11) if i%2==0]))
combain_list = [1,2,3.8,[1,2,2,4],True,False,1.0]
# get_filter = []
# for filter_list in combain_list:
#     if type(filter_list) == int or type(filter_list) == float:
#         get_filter.append(str(filter_list))
# print(get_filter)

def filter_number(combain_list):
    return [str(filter) for filter in combain_list if type(filter)== int or type(filter) == float]

print(filter_number(combain_list))
