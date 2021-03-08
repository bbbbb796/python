#for n in a.copy():
#    print(n)
#    a.remove(n)
#print(a)

#a=[1,2,3,4,5,6]
#b=a.copy()
#b.append(1000)
#print(a)


#import copy
#a=[1,2,3, [100]]
#b=copy.deepcopy(a)
#b[3].append(200)
#print(a)

#m=[
#    [1,2,3],
#    [4,5,6],
#    [7,8,9]
#]

#for l in m:
#    for n in l:
#        print(n)

#n=input('NAME: ')
#print(n or 'Guest')

#a=int(input('Age: '))
#print('Welcom' if a>=18 else 'No access')

#g=lambda x,y: x*y
#print(g(2,5))

#a=['seva','igor','oleg']
#b=['150000','10000','35000']

#print(dict(zip(a,b)))

#data=[150]
#def a(x):
#    return x*2

#g=list(map(a, data))

#def r():
#    print('I am admin')

#l= input('Login: ')
#r() if l == 'admin' else print('Hello user')'

#a=10
#b=10
#print(a is b)

#r=[]
#for i in range(11):
#    r.append(i)
#print(r)

#r_1=[i for i in range(11)]
#print(r_1)

#r=[i for i in range(-10,11) if i>0]
#print(r)

#a=[1,2]
#try:
#    b=a[5]
#except IndexError:
#    print('Неверный индекс')

#except Exception as e:===}УЗНАТЬ ОШИБКУ
#    print(e.__class__)===}УЗНАТЬ ОШИБКУ


#try:
#    a=int(input('Age: '))
#except ValueError:
#    print('Вы должны были ввести число')

#import re
#p='([a-zA-Z0-9_]+@[a-z]+\.(ru|org|com))'
#email='kurochkin_seva@mail.ru'
#print(re.match(p, email))
#print(re.search(p, email))

#text='kefmewfbi kurochkin_seva@mail.ru fgragarga agaga kurochkin_seva@mail.ru fdweff'
#print(re.findall(p, text))

#'\.{2,}'
