class Employees:
    def __init__(self):
        self.office = []
        self.schedule = []
        self.name = ""
    def get_office(self):
        return self.office
    
    def set_office(self, office):
        self.office.append(office)
        
    def get_schedule(self):
        return self.schedule
    
    def set_schedule(self, schedule):
        self.schedule.append(schedule)
        
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
