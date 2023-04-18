from MyPack.student import Student

# Create a new student object
student1 = Student(1, "Tanay", 4, "Mumbai")

# Use getter methods to get student details
print("Student ID:", student1.get_id())
print("Student Name:", student1.get_name())
print("Student Semester:", student1.get_sem())
print("Student City:", student1.get_city())

# Use setter methods to update student details
student1.set_id(2)
student1.set_name("Jeeva")
student1.set_sem(6)
student1.set_city("New Delhi")

# Use getter methods to get updated student details
print("Updated Student ID:", student1.get_id())
print("Updated Student Name:", student1.get_name())
print("Updated Student Semester:", student1.get_sem())
print("Updated Student City:", student1.get_city())
