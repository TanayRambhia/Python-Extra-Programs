num_employees = int(input("Enter number of employees: "))

# Loop through each employee
for i in range(num_employees):
    # Get employee details
    print(f"\nEnter details for employee {i+1}:")
    job_number = input("EnterJob number: ")
    level_number = int(input("Enter Level number: "))
    basic_pay = float(input("Enter Basic pay: "))

    if level_number == 1:
        ca = 1000
        ea = 500
    elif level_number == 2:
        ca = 750
        ea = 200
    elif level_number == 3:
        ca = 500
        ea = 100
    elif level_number == 4:
        ca = 250
        ea = 0

    g_sal = basic_pay + (basic_pay * 0.25) + ca +ea

    if g_sal <= 2000:
        it = 0
    elif 2000< g_sal <= 4000:
        it = 0.03 * g_sal 
    elif 4000< g_sal <= 5000:
        it = 0.05 * g_sal 
    elif g_sal > 5000:
        it = 0.08 * g_sal 

    net_sal = g_sal - it

    print("Gross Salary:" ,g_sal)
    print("Net Salary:" ,net_sal)
