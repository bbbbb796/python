#class, object и аргументы ###############################


#class Car:
#    model = 'bmw'
#    engine = 1.6

#    def drive():
#        print('lets go')

#Car.drive()

#getattr(Car,'drive')()

#a1 = Car()
#a2 = Car()

#a1.model='Mersedes'
#a1.beach=10

#print(Car.__dict__)
#print(a1.__dict__)

#getattr(Car, 'x', 100)
#setattr(Car, 'y', 200)
#print(type(a1))


#self и __init__ #########################################

#class Point:
#    def __init__(self, x = 0, y = 0):
#        self.x = x
#        self.y = y
    
#    def __del__(self):
#        print("Удаление экземпляра: " + self.__str__())

#    x = 1; y = 1

#    def blabla(self, x, y):
#        self.x = x
#        self.y = y

#pt = Point(5, 10)
#pt = Point()
#pt2 = Point(5)
#pt3 = Point(5, 10)
#pt.blabla(5,10)
#print(pt.__dict__, pt2.__dict__, pt3.__dict__,sep="\n")

#Моно состояние для все экземпляров

#class Cat:
#    __sharit_attr = {
#        'beerd': 'siam',
#        'color': 'black'
#    }

#    def __init__(self):
#        self.__dict__ = Cat.__sharit_attr


#a1 = Cat()
#a1.p = 'say'
#print(a1.__dict__, sep='\n')
#print(Cat.__dict__, sep='\n')

#Публичные, приватные, защищенные атрибуты и методы гетеры и сетеры ############
#class BankAccount:
#    def __init__(self, name, balance, passport):
#        self.__a = name
#        self.__b = balance
#        self.__c = passport
    
#    def public_print_data(self):
#        print(self.a, self.b, self.c)

    #def protect_print_data(self):
    #    print(self.__a, self.__b, self.__c) #Если мы видим в нутри класса переменную с _ то это лучше не использовать вне класса


#account1 = BankAccount('Bob', 100000, 454845646854)
#ccount1.protect_print_data()
#try:
#    print(account1.__a, account1.__b, account1.__c,sep='\n')
#except AttributeError:
#    print('Мы не имеем или не можем предоставить доступ к базе данных нашил клиентов')


#Геттеры Сеттеры, декоратор property ############################


#class Layer:
#    WGET = 5

#    def __init__(self, lvl = 0):
#        self.__lvl = lvl
    
#    def __checkValue(lvl):
#        if Layer.__checkValue(lvl):
#            return True
#        return False

#    def setLVL(self, lvl):
#        if (isinstance(lvl, int)) or (isinstance(lvl,float)):
#            self.__lvl = lvl
#        else:
#            print('Введите число')

#    def getLVL(self):
#        return self.__lvl

#    def __setattr__(self, key, value):  #key == pt
#        if key == 'WGET':   
#            raise AttributeError    #raise == Исключение
#        else:
#            self.__dict__[key] = value  #__dict__[key] == все остальные pt ; #\ value == свойства
    
#pt = Layer()
#pt.WGET = 5


#class CoordValue:
#    def __init__(self, name):
#        self.__name = name #name == новые значения
#
#    def __get__(self, instance, owner):
#        return instance.__dict__[self.__name]
#    
#    def __set__(self, instance, value):
#        instance.__dict__[self.__name] = value #instance == pt
                                                #__dict__[self.__name] = value == принимает новые значения



#class Boint:
#    coordx = CoordValue('coordx')
#    coordy = CoordValue('coordy')
#
#
#    def __init__(self, x = 0 , y = 0):
#        self.coordx = x
#        self.coordy = y
    
#    def __checkValue(x):
#        if isinstance(x, int) or isinstance(x, float) :
#            return True
#        return False

#    @property
#    def coordx(self):
#        return self.__x

#    @coordx.setter    
#    def coordx(self, x):
#        if Boint.__checkValue(x):
#            self.__x = x
#        else:
#            raise ValueError('Неверный формат данных')
    
#    coordx = property(__getCoordx, __setCoordx)

#pt = Boint(1,2)
#pt.coordx = 6
#print(pt.coordx , pt.coordy)

#pt.coordx = 100
#x = pt.coordx
#print(x)


#property ######################################################################

#class BankAccount:
#
#    def __init__(self, name, balance):
#        self.name = name
#        self.__balance = balance
    
#    @property
#    def my_balance(self):
#        print('get balance')
#        return self.__balance

#    @my_balance.setter
#    def my_balance(self, value):
#        print('set balance')
#        self.__balance = value

#p = BankAccount('seva', 300)
#print(p.my_balance)



#ПРОСТОЕ НАСЛЕДОВАНИЕ КЛАССОВ ########################################


#class Person: #parent
#
#    def can_breath(self):
#        print('я могу дышать')
#
#    def can_walk(self):
#        print('я могу ходить')

#class Doctor(Person): #sublclass
#
#    def can_cure(self):
#        print('я могу лечить')

#class Arhitect(Person): #subclass
#
#    def can_build(self):
#        print('я могу построить здание')


#print(issubclass(Doctor, Person))
#print(issubclass(Person, Doctor))


#Пространство имен класса Class Body scope in Python ###########################

#class DepartmentIT:
    
#    python_dev = 5
#    go_dev = 3
#    react_dev = 2

#    def info(self):
#        print(self.python_dev, self.go_dev, self.react_dev)
    
#    def info2(self):
#        print(DepartmentIT.python_dev, DepartmentIT.go_dev, DepartmentIT.react_dev)
    
#    @property
#    def info_prop(self):
#        print(self.python_dev, self.go_dev, self.react_dev)

#    @classmethod
#    def info_class(cls):
#        print(cls.python_dev, cls.go_dev, cls.react_dev)

#    @staticmethod
#    def info_static():
#        print(DepartmentIT.python_dev, DepartmentIT.go_dev DepartmentIT.react_dev)

#    def make_bakend(self):
#        print('Pyhon and GO')
    
#    def make_frontend(self):
#        print('React')
    
#    def hiring_pyt_dev(self):
#        DepartmentIT.python_dev = DepartmentIT.python_dev + 1

#it = DepartmentIT()
#print(it.python_dev)
#it.hiring_pyt_dev()
#print(it.python_dev)



#Наследование. Переопределение методов в Python ###############################

#class Person:

#    def __init__(self, name):
#        self.name = name
    
#    def breath(self):
#        print('человек дышит')

#    def walk(self):
#        print('человек ходит')
    
#    def __str__(self):
#        return f"Person - {self.name}"

#class Doctor(Person):

#    def breath(self):
#        print("Доктор дышит")

#    def __str__(self):
#        return f"Doctor - {self.name}"

#d = Doctor('john')
#p = Person('adam')
#print(p, d,sep="\n")


#Наследование. Расширение класса в Python #####################################

#class Person:
#    age = 25
#    def breath(self):
#        print('Человек дышит')

#    def sleep(self):
#        print('Человек спит')
    
#    def combo(self):
#        if hasattr(self, 'walk'):
#            self.walk()
#        if hasattr(self, 'age'):
#            print(self.age)
#        self.breath()
#        self.sleep()

#class Doctor(Person):
#    age = 30
#    def sleep(self):
#        print('Доктор спит')
    
#    def breath(self):
#        print('Доктор дышит')
    
#    def walk(self):
#        print('Доктор идет')

#p = Person()
#d = Doctor()
#p.combo()
#print('-'*10)
#d.combo()


#Множественное наследование в Python и функция Super() #########################

#class Doctor:
#    def __init__(self, degree):
#        self.degree = degree

#    def graduate(self):
#        print("Ура, я отучился на доктора")

#    def can_build(self):
#        print("я доктор, я умею строить, но не очень")


#class Builder:
#    def __init__(self, rank):
#        self.rank = rank

#    def graduate(self):
#        print("Ура, я отучился на строителя")
    
#    def can_cure(self):
#        print("я строитель, я умею лечить,но не очень ")


#class Person(Doctor, Builder):
#    def __init__(self, degree,rank):
#        super().__init__(degree)
#        Builder.__init__(rank)

#    def __str__(self):
#        return f"Person - {self.rank} {self.degree}"

#print(Person.__mro__)

#s = Person(5, 'spec')
#print(s)


#ООП Python 3: коллекция __slots__ для классов #################################

#import timeit

#class Point:
    
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
    

#class Point2D:
#    __slots__ = ('x', 'y')
#    MAX_COORD = 100
#
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
#    
#    def calc(self):
#        self.x += 1
#        del self.y
#        self.y = 0

#pt = Point2D(10,20)
#print(pt.x, pt.y)

#t = timeit.timeit(pt.calc)
#print(t)


#Slots свойства и наследование в Python ######################################

#class Rectangle:
#    __slots__ = ('width', 'height')

#    def __init__(self, a, b):
#        self.width = a
#        self.height = b

#    @property
#    def perimetr(self):
#        return (self.width+self.height)*2
    
#    @property
#    def area(self):
#        return self.width * self.height

#class Square(Rectangle):
#    __slots__ = tuple()

#    def __init__(self, a, b):
#        super().__init__(a,b)


#a = Square(4,4)
#b = Rectangle(4,5)

#print(a.perimetr, a.area, a.color)
#print('-'*20)
#print(b.perimetr, b.area)
