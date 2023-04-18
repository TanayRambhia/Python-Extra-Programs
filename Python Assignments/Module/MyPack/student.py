class Student:
    def __init__(self, id, name, sem, city):
        self.id = id
        self.name = name
        self.sem = sem
        self.city = city

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_sem(self):
        return self.sem

    def set_sem(self, sem):
        self.sem = sem

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city
