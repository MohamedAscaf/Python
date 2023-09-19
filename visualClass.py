
""" from ipaddress import collapse_addresses


class newclass:
    def __init__ (self,a,b):
        self.firstvalue=a
        self.secondvalue=b
    def add (self):
        return self.firstvalue+self.secondvalue
    

senthil=newclass(1,2)
print(senthil.add())

karthik=newclass(4,5)
print(karthik.add()) """

'''
class CalculatorSub:
    def __init__(self,x,y):
        self.firstvalue=x
        self.secondvalue=y
    def sub (self):
        return self.firstvalue-self.secondvalue
    
jack=CalculatorSub(1,2)
print(jack.sub())

rose=CalculatorSub(3,4)
print(rose.sub())

'''
'''
class CalculatorMul:
    def __init__(self,a,b):
        self.multiplication1=a
        self.multiplication2=b
    def mul(self):
        return self.multiplication1*self.multiplication2
    
harry=CalculatorMul(1,2)
print(harry.mul())

potter=CalculatorMul(3,4)
print(potter.mul())

'''

'''
class CalculatorDiv:
    def __init__(self,x,y):
        self.division1=x
        self.division2=y
    def div(self):
        return self.division1/self.division2
sir=CalculatorDiv(7,8)
print(sir.div())

mam=CalculatorDiv(3,4)
print(mam.div())

'''

"""
class calculator:
    def __init__(self,a,b):
        self.firstvalue=a
        self.secondvalue=b
    def add(self):
        return self.firstvalue+self.secondvalue
    def sub(self):
        return self.firstvalue-self.secondvalue
    def mul(self):
        return self.firstvalue*self.secondvalue
    def div(self):
        return self.firstvalue/self.secondvalue
    
harry=calculator(1,2)
print(harry.add())
print(harry.sub())
print(harry.mul())
print(harry.div())

"""

'''
 potter=calculator(3,4)
print(potter.mul()) 
'''

""" class classmate:
    def __init__(self,a,b):
        self.FirstStudent=a
        self.SecondStudent=b
    def add(self):
        return self.FirstStudent+self.SecondStudent
a=int(input("Enter the First Student Value:"))
b=int(input("Enter the Second Student Value:"))
karthikeiyan=classmate(a,b)
print(karthikeiyan.add())
AnanthanRaman=classmate(a,b)
print(AnanthanRaman.add()) """

""" class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name : ",self.name," \nAge : ",self.age) 

class student(person):
    pass
ascaf=student("Ascaf",26)
ascaf.show() """

#example of class

""" class student:
    def StudentMark(self,x,y):
        self.firstvalue=x
        self.secondvalue=y
        print(self.firstvalue,self.secondvalue)

karthikeiyan=student()
karthikeiyan.StudentMark(12,21)
anantharaman=student()
anantharaman.StudentMark(45,54) """

"""
class classmate:
    def __init__(self,m,n):
        self.FirstClassMate=m
        self.SecoundClassMate=n
    def div(self):
        return self.FirstClassMate/self.SecoundClassMate
    
anbu=classmate(12,34)
print(anbu.div())

guna=classmate(56,78)
print(guna.div())

"""

#instance method

""" class person():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
    def show(self):
        print("Name :" , self.name , " \n Age :" , self.age)

karthikeiyan=person("karthikeiyan" , 20)
karthikeiyan.show() """

#inheridance

""" class person():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age

class student(person):
    def __init__(self, Name, Age,department):
        person.__init__(self,Name,Age)
        self.department=department
    def show(self):
        print("Name : ",self.name,"\nAge : ",self.age,"\nDepartment : ",self.department)



karthikeiyan=student("karthikeiyan" , 20,"m.sc")
karthikeiyan.show()
 """
#Example Student IDCard

""" class single():
    def __init__(self,Male,Female):
        self.male=Male
        self.female=Female

class student(single):
    def __init__(self,Male,Female,Trans):
        single.__init__(self,Male,Female)
        self.trans=Trans

    def show(self):
        print("Male   : " , self.male , "\nFemale : " , self.female ,  "\ntrans  :" , self.trans)

ID=student("kumarakanan" ,"thenmoli"," kumarikanan")
ID.show() """


""" class person():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age

class student(person):
    def __init__(self,Name,Age,Place):
        person.__init__(self,Name,Age)
        self.place=Place

    def show(self):
        print("Name   : " , self.name , "\nAge    : " , self.age ,  "\nPlace  :" , self.place)

ID=student("karthikeiyan" ,20," madurai")
ID.show() """

#father
class students():
    def __init__(self,Name,Age):
        self.name=Name
        self.age=Age
        
#son
class  LiveWireStudent(students):
    def __init__(self,Name,Age,Mark,Grade,Department):
        students.__init__(self,Name,Age)
        self.mark=Mark
        self.grade=Grade
        self.department=Department

    def show(self):
        print("Name       : " , self.name , "\nAge        : " , self.age , "\nMark       : " , self.mark , "\nGrade      : " , self.grade , "\nDepartment : " , self.department)

print("-------------------------------")

MarkSheet=LiveWireStudent("Anantharaman" , 21 , 80 , "B" , "BBA" )
MarkSheet.show()

print("-------------------------------")

MarkSheet=LiveWireStudent("karthikeiyan" , 20 , 100 , "A" , "Msc" )
MarkSheet.show()

print("-------------------------------")

MarkSheet=LiveWireStudent("Ascaf" , 26 , 90 , "A" , "BE,IT" )
MarkSheet.show()

print("-------------------------------")

MarkSheet=LiveWireStudent("awinas" , 21 , 70 , "C" , "BCom" )
MarkSheet.show()

print("-------------------------------")

MarkSheet=LiveWireStudent("depak" , 23 , 80 , "B" , "Bsc" )
MarkSheet.show()

print("-------------------------------")