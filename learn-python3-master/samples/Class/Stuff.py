

class Staff:
    def __init__(self,name,sex,age,salary):#初始化
        self.name = name
        self.age = age
        self.sex = sex
        self.salary =salary
    def coding(self,job):
        print(self.name+"是研发部的，他的职责是："+job)

staff1 = Staff("doudou","male",18,16000)

print(staff1)
print(staff1.coding("cesi"))