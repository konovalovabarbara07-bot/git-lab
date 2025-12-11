class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id
    def get_info(self):
        return f"Сотрудник:{self.name}, ID {self.id}"
class Manager:
    def __init__(self, departament):
        self.departament = departament
    def manage_project(self):
        return f"Менеджер отдела:{self.departament}"
class Technician:
    def __init__(self, specialization):
        self.specialization =specialization
    def do_work(self):
        return f"Техник:{self.specialization}"
class TechManager(Employee, Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        Employee.__init__(self, name, emp_id)
        Manager.__init__(self, department)
        Technician.__init__(self, specialization)
        self.team = []
    def add_employee(self,emp):
        if isinstance(emp, Employee):
            self.team.append(emp)
            print(f"добавить сотрудника:{emp.name}")
        else:
            print("Ошибка")
    def get_team_info(self):
        print(f"\nкоманда{self.name}:")
        if self.team:
            for emp in self.team:
              print("-", emp.get_info())
        else:
            print('нет сотрудников')
    def get_info(self):
        return (f'технический менеджер:{self.name}, ID:{self.id},отдел:{self.departament},специализация:{self.specialization}')
if __name__=="__main__":
    emp1= Employee ("Саша", "01")
    print(emp1.get_info())
    mgr1 = Manager("Петя")
    print(mgr1.manage_project())
    tm1 = TechManager("Боря", "02", "IT", "серверы")
    print(tm1.get_info())
    print(tm1.manage_project())
    print(tm1.do_work())

    tm1.add_employee(emp1)
    tm1.get_team_info()