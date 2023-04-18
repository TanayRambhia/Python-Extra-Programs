class BMI:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
    
    def set_height(self, height):
        self.height = height
    
    def set_weight(self, weight):
        self.weight = weight
    
    def get_height(self):
        return self.height
    
    def get_weight(self):
        return self.weight
    
    def calBMI(self):
        height_m = self.height / 100.0 # convert height from cm to meters
        bmi = self.weight / (height_m ** 2)
        return bmi
    
# create an empty list to hold instances of BMI class
people = []

# prompt the user to input data for each person and create instances of BMI class
while True:
    height = input("Enter height in cm (or 'quit' to exit): ")
    if height == 'quit':
        break
    weight = input("Enter weight in kg: ")
    person = BMI(float(height), float(weight))
    people.append(person)

# calculate BMI for each person and print the result
for i, person in enumerate(people):
    print(f"Person {i+1} BMI: {person.calBMI()}")

# print the BMI category for each person
for i, person in enumerate(people):
    bmi = person.calBMI()
    if bmi < 18.5:
        print(f"Person {i+1} is underweight")
    elif bmi < 25:
        print(f"Person {i+1} has normal weight")
    elif bmi < 30:
        print(f"Person {i+1} is overweight")
    else:
        print(f"Person {i+1} is obese")
