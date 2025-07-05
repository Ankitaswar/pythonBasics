#dic -> key:value pair, key is immutable and unique

data = {1:"Ankit", 2: "Aswar", 4:"Vikas"}
print(data)

print(data[4])  #fetch using key if not throw error
# print(data[3]) # throw error as key is not present

print(data.get(3))  #None
print(data.get(3, "Not found with key : 3"))
print(data.get(1)) #fetch using key but it not present not throw error


key = ['Ankit', 'Kiran', 'Harsh']
values = ['Python', 'Java', 'JS']
#merge to list and create dictionary
dic = dict(zip(key, values))
print(dic)

print(dic.get('Kiran'))

dic['Monika'] = 'C++'
print(dic)

del dic['Harsh']
print(dic)


#Create a dictionary which has list and dic inside it.
prog = {'JS':'Atom', 'CS':'VS', 'Python' : ['Pycharm', 'Sublime'],
            'Java' : {'JSE': 'NetBeans', 'JEE':'Eclipse'}}
print(prog)
print(prog['Python'][1])
print(prog['Java'].get('JEE'))
print(prog['Java']['JSE'])

print(prog.keys())
print(prog.values())

prog.update({'city':'Gwalior', 'Age' : 24})
print(prog)

prog.setdefault('city' , 'Mumbai') #add key if not present
print(prog)

prog.setdefault('LastCity' , 'Mumbai') #add key if not present
print(prog)

#AddValue to a list inside a dictionary
my_dict = {}
my_dict['fruits'] = ['Apple']
print(my_dict)
print( f"Type of my dict is {type(my_dict['fruits'])}")  #therefore we can use append function.
my_dict['fruits'].append('Banana')
print(my_dict)




