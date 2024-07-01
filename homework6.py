#Работа со словарями:
my_dict={'Danila':1988,'Anna':2001, 'Vlad':1989}
print(my_dict)
print(my_dict['Anna'])
my_dict['Max']=2014
print(my_dict['Max'])
my_dict.update({'Lena':2019,'Oleg':1995})
del my_dict['Oleg']
print(my_dict['Lena'])
print(my_dict)

#Работа с множествами:
my_set={23,"дом",87.3,'вера',56,'деньги',True,23,'деньги',(1,5,34)}
print(my_set)
my_set.add(2)
my_set.add('солнце')
my_set.remove('деньги')
print(my_set)