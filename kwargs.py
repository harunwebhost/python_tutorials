mylist = ['ajaz','ahmed']
#dist = dict(mylist)
def mytask(mylist,**kwargs):
    return [i if  kwargs['revers_string'] == True  i.capitalize()  else  i.lower() for i in mylist  )]
print(mytask(mylist,revers_string = True)).capitalize()