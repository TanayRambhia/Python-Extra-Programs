from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    @abstractmethod
    def earnings(self):
        pass
    
class SalariedEmployee(Employee):
    def __init__(self, name, address, weekly_salary):
        super().__init__(name, address)
        self.weekly_salary = weekly_salary
    
    def earnings(self):
        return self.weekly_salary
    
class HourlyEmployee(Employee):
    def __init__(self, name, address, hourly_wage, hours_worked):
        super().__init__(name, address)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked
    
    def earnings(self):
        if self.hours_worked <= 40:
            return self.hourly_wage * self.hours_worked
        else:
            overtime_hours = self.hours_worked - 40
            overtime_pay = overtime_hours * 1.5 * self.hourly_wage
            regular_pay = 40 * self.hourly_wage
            return regular_pay + overtime_pay
    
class CommissionEmployee(Employee):
    def __init__(self, name, address, sales, commission_rate):
        super().__init__(name, address)
        self.sales = sales
        self.commission_rate = commission_rate
    
    def earnings(self):
        return self.sales * self.commission_rate
    
class BasePlusCommissionEmployee(CommissionEmployee):
    def __init__(self, name, address, sales, commission_rate, base_salary):
        super().__init__(name, address, sales, commission_rate)
        self.base_salary = base_salary
    
    def earnings(self):
        return self.base_salary + super().earnings()
    
    def get_base_salary(self):
        return self.base_salary
    
    def set_base_salary(self, base_salary):
        self.base_salary = base_salary

employees = [SalariedEmployee('Tanay', '123 Love Lane.', 1000),
             HourlyEmployee('Vayu', '456 Bhavani Shanakar Lane.', 20, 45),
             CommissionEmployee('Jeeva', '789 Raguleela Lane.', 2000, 0.05),
             BasePlusCommissionEmployee('Raghu', '101 Pipe Lane.', 3000, 0.1, 1000)]

# Increase the base salary of base-salaried commission employees by 10%
for emp in employees:
    if isinstance(emp, BasePlusCommissionEmployee):
        base_salary = emp.get_base_salary()
        emp.set_base_salary(base_salary * 1.1)

print()

print("Employee Details: \n")
print("Name \t Money Earned \t Address")
for emp in employees:
    print(f'{emp.name}\t Rs {emp.earnings()} \t{emp.address} ')
