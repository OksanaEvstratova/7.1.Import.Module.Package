from application.db.people import get_employees

def calculate_salary(fio):
    for employee_name in fio: print(f'Calculate salary {employee_name}')


if __name__ == '__main__':
    print(f'---begin - from salary.py')
    calculate_salary(get_employees())
    print(f'---end - from salary.py')