#Функция с параметрами по умолчанию

def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

values_list = ['one',2,True]
values_dict = {'a':222222, 'b':'line','c':False}
#values_list_2 = ['five',[1,2]]
values_list_2 = [54.32, 'Строка' ]



print_params()
print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2)
print_params(*values_list_2, 42)