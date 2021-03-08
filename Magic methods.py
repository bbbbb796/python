#Магические методы. Методы __str__ и __repr__ ################################################

#class Lion:
#    def __init__(self, name):
#        self.name = name
    
#    def __repr__(self):
#        return f"The object Lion - {self.name}"

#    def __str__(self):
#        return f"Lion - {self.name}"

#print(Lion('simba'))


#Магические методы __add__, __mul__, __sub__ и __truediv__##############################################

#class BankAccount:
#    def __init__(self, name, balance):
#        self.name = name
#        self.balance = balance
    
#    def __add__(self, other):
#        print('Метод __add__ был создан')
#        if (isinstance(other, BankAccount)):
#            return self.balance + other.balance
#        if (isinstance(other, (int, float))):
#            return BankAccount(self.name, self.balance+other)
#        raise NotImplemented

#    def __repr__(self):
#        return F"Клиент {self.name} с балансом {self.balance}"

#    def __mul__(self, other):
#        print('Метод __mul__ был создан')
#        if (isinstance(other, BankAccount)):
#            return self.balance * other.balance
#        if (isinstance(other, (int, float))):
#            return BankAccount(self.name, self.balance*other)
#        raise NotImplemented

#    def __sub__(self, other):
#        print('Метод __add__ был создан')
#        if (isinstance(other, BankAccount)):
#            return self.balance - other.balance
#        if (isinstance(other, (int, float))):
#            return BankAccount(self.name, self.balance-other)
#        raise NotImplemented

#    def __truediv__(self, other):
#        print('Метод __add__ был создан')
#        if (isinstance(other, BankAccount)):
#            return self.balance / other.balance
#        if (isinstance(other, (int, float))):
#            return BankAccount(self.name, self.balance/other)
#        raise NotImplemented

#t = BankAccount('anon', 230)
#q = BankAccount('Seva',1000)
#a = BankAccount('Misha', 100)



#Магические методы __eq__ и __hash__. Dunder methods в Python########################################

#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
    
#    def __eq__(self, value): #__eq__ Позволяет реализовать проверку на равенство для экземпляров пользовательских типов. self : Ссылка на экземпляр. value : Объект с которым следует произвести сравнение (справа от оператора сравнения)
#        return isinstance(value, Point) and \
#            self.x == value.x and self.y == value.y 
    
#    def __hash__(self): #hash = нужен для роботы со словорями и обращением к ним
#        return hash((self.x, self.y))  
    
#p = Point(1,2)
#print(hash(p))


#Магический метод __bool__ Правдивость объектов в Python###############################################

#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
    
#    def __bool__(self):
#        print('call __bool__')
#        return self.x != 0 or self.y != 0

#p = Point(1,2)
#print(bool(p))


#Полиморфизм в Python #########################################################

#Полиморфизм - это способность выполнять действие над объектом независимо от его типа

#class Rectangle:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y
    
#    def __str__(self):
#        return f"Rectangle {self.x}x{self.y}"
#
#    def get_area(self):
#        return self.x * self.y

#class Square:
#    def __init__(self, x):
#        self.x = x
    
#    def __str__(self):
#        return f"Square {self.x}x{self.x}"

#    def get_area(self):
#        return self.x ** 2

#class Circle:
#    def __init__(self, r):
#        self.r = r
    
#    def __str__(self):
#        return f"Circle radius = {self.r}"

#    def get_area(self):
#        return 3,14 * self.r ** 2

#cr1 = Circle(5)

#rect1 = Rectangle(1,2)
#rect2 = Rectangle(3,4)

#sq1 = Square(4)

#figures = [rect1, rect2, sq1, cr1]
#for i in figures:
#    print(i ,i.get_area())
