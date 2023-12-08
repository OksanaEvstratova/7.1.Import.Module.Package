import pprint
from application.salary import calculate_salary
from application.db.people import get_employees


# if __name__ == '__main__':
print(f'---begin - from dirty_main.py')
calculate_salary(['Kim'])
pprint.pprint(get_employees(), width=10)
calculate_salary(get_employees())
print(f'---end - from dirty_main.py')
