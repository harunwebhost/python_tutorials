# def multiply(num,*args):
#     multiply_list = []
#     for i in args:
#         multiply_list.append(i**num)
#     return multiply_list

num = int (raw_input("Enter you number"))
args= raw_input("Enter args numbers").split(',')

def multiply(num, *args):
    if args:
        return [int(i)**num for i in args]
    else:
        return "you have not enter anything"
print(multiply(num,*args))