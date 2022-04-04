from datetime import datetime
from employee import Employees

def singleton(cls):
    instances = dict()
    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return wrap

@singleton           
class File:    
     
    def __init__(self):
        self.name_file = ""
        self.file = None
        
    def set_name_file(self, name_file):
        self.name_file = name_file
    
    def get_name_file(self):
        return self.name_file
    
    def set_file(self, file):
        self.file = file
        
    def get_file(self):
        return self.file
    
    def open_text_file(self, name_file):
        try:
            self.file = open(name_file)  
            self.read__text_file()   
        except:
            print("Something went wrong when opening the file")
            
    def read__text_file(self):
        try:
            controller = Controller()
            content = self.file.readlines()
            list_employees = controller.classify_data(content)
            print(*controller.compare_data_employee(list_employees), sep = '\n')                 
        except:
                print("Something went wrong when reading to the file")
        finally:
                
                self.file.close()  


@singleton
class Controller:
    
    hours = '0123456789:'
    letters = 'ABCDEFGHIJKLMNOPQRSTUVXYZ'
    
    def __init__(self):
        pass
    
    def classify_data(self, content):  
        list_employees = []
        for line in content:
            employee = Employees()
            identifier = 'name' 
            employee_schedule = ''
            employee_office = ''
            employee_name = ''
            for character in line:
                if character in self.letters:
                    if identifier == 'name':
                        employee_name += character
                    elif identifier == 'office':  
                        employee_office += character
                        if employee_office.__len__() == 2:
                            employee.set_office(employee_office)
                            employee_office = ''
                elif character in self.hours:
                    employee_schedule += character
                elif character == '=':
                    employee.set_name(employee_name)
                    identifier = 'office'
                elif character == '-': 
                    employee.set_schedule([employee_schedule])
                    employee_schedule = ''  
                elif character == ',' or character == '\n':
                    employee.get_schedule()[-1].append(employee_schedule)
                    employee_schedule = ''
                    identifier = 'office'
            employee.get_schedule()[-1].append(employee_schedule)    
            list_employees.append(employee)
        return list_employees
        
    def compare_data_employee(self,list_employees ):
        list_employee_share_office = []
        for i in range(0, list_employees.__len__()):
            for j in range(i+1, list_employees.__len__()): 
                if i != j:
                    list_employee_share_office.append(self.compare_office(list_employees[i], list_employees[j]))
        return list_employee_share_office
                    
    def compare_office(self, employee_1, employee_2):
        count = 0
        for index_employee_1 in range(0, employee_1.get_office().__len__()):
            for index_employee_2 in range(0, employee_2.get_office().__len__()):
                if employee_1.get_office()[index_employee_1] == employee_2.get_office()[index_employee_2]:
                    count += self.compare_schedule(employee_1, employee_2, index_employee_1, index_employee_2)
        return employee_1.get_name() + '-' + employee_2.get_name() + ': ' + str(count)
        
    def compare_schedule(self,employee_1, employee_2, index_employee_1, index_employee_2):             
        hour_employee_initial_1 = datetime.strptime(employee_1.get_schedule()[index_employee_1][0], "%H:%M").time()
        hour_employee_final_1 = datetime.strptime(employee_1.get_schedule()[index_employee_1][1], "%H:%M").time()
        hour_employee_initial_2 = datetime.strptime(employee_2.get_schedule()[index_employee_2][0], "%H:%M").time()
        hour_employee_final_2= datetime.strptime(employee_2.get_schedule()[index_employee_2][1], "%H:%M").time()
        if hour_employee_final_1 > hour_employee_initial_1 and hour_employee_final_2 > hour_employee_initial_2 :
            if hour_employee_initial_1 >= hour_employee_final_2 and hour_employee_final_1 >= hour_employee_initial_2:
                return 0
            elif hour_employee_initial_1 <= hour_employee_final_2 and hour_employee_final_1 <= hour_employee_initial_2:
                return 0
            else:
                return 1
        else:
            return 0