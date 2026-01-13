class Employee:
    def __init__(self, name, id, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.id = id

    def get_info(self):
        return f"Id: {self.id}, Имя: {self.name}"

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department
        self.team = []

    def manage_project(self):
        return f"Менеджер: {self.name} управляет проектом в отделе {self.department}"

    def get_info(self):
        return f"{super().get_info()}, Статус: Менеджер, Отдел: {self.department}"

class Technician(Employee):
    def __init__(self, specialization, **kwargs):
        super().__init__(**kwargs)
        self.specialization = specialization

    def perform_maintenance(self):
        return f"Техник: {self.name}, обслуживает по специальности {self.specialization}"

    def get_info(self):
        return f"{super().get_info()}, Статус: Техник, Специализация: {self.specialization}"

class TechManager(Manager, Technician):
    def __init__(self, name, id, department, specialization):
        super().__init__(name=name, id = id, department=department, specialization=specialization)

    def perform_maintenance(self):
        return f"Технический сотрудник {self.name}, обслуживает в специализации: {self.specialization}"

    def get_info(self):
        return f"{super().get_info()}, Специализация: {self.department}"

    def add_employee(self, employee):
        if employee not in self.team:
            self.team.append(employee)
            return f"Сотрудник {employee.name} присоединяется к {self.name}"
        else:
            return f"Сотрудник {employee.name} уже присоединился к {self.name}"

    def get_team_info(self):
        if not self.team:
            return f"У технического менеджера {self.name} отсутствуют подчинённые"
        team_info = [f"Команда {self.name}",
                     f"Кол-во сотрудников: {len(self.team)}"]
        for i, team in enumerate(self.team, 1):
            team_info.append(f" {i}. {team.get_info()}")
        return team_info

print("Class Employee")

empl1 = Employee("Алексей Виноградов", "FS3318")
print(f"Сотрудник: {empl1.get_info()}")

print("Class Manager")

mng1 = Manager (name ="Михаил Иванов", id = "O1349", department="Производственный отдел")
print(f"Менеджер: {mng1.get_info()}")
print(f"Обязанность: {mng1.manage_project()}")


print("Class Technician")
tch1 = Technician(name ="Евгений Петров", id ="JK3215", specialization="Связь")
print(f"Техник: {tch1.get_info()}")
print(f"Операция: {tch1.perform_maintenance()}")


print("Class TechManager")
tech_mgr1 = TechManager( name="Александр Сидоров", id ="ER542", department="Технический отдел", specialization="Безопасность")
print(f"Технический менеджер: {tech_mgr1.get_info()}")
print(f"Операция 1: {tech_mgr1.manage_project()}")
print(f"Операция 2: {tech_mgr1.perform_maintenance()}")

tech_mgr1.add_employee(tch1)
tech_mgr1.add_employee(empl1)
print(tech_mgr1.get_team_info())

employees = [
    Employee(name="Василий Попов", id="UW978"),
    Manager(name ="Илья Демин", id="SS745",department= "Разработка"),
    Technician(name="Сергей Данилов", id= "IM688", specialization="Мониторинг"),
    tech_mgr1
]

print("Информация о сотрудниках")
for i, employee in enumerate(employees, 1):
    print(f"{i}. {employee.get_info()}")






