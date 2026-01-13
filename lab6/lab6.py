#1
class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password
        print('Пароль изменен')
        
    def check_password(self, remain_password):
        return self.__password == remain_password
        
UserAccount1 = UserAccount("Irina", "irina@gmail.com", "qwerty123")

print(UserAccount1.check_password('qwerty123'))
print(UserAccount1.check_password('qwerty12'))
UserAccount1.set_password('qwertyuiop')
print(UserAccount1.check_password('qwertyuiop'))
print(UserAccount1.check_password('qwertyuioq'))

#2
class Vehicle :
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def get_info(self):
        return f"Марка: {self.make}, Модель: {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type
    
    def get_info(self):
        return super().get_info() + f" Тип топива: {self.fuel_type}"

A = Car("Porshe", "Carrera 911", "petrol95")

print(A.get_info())
