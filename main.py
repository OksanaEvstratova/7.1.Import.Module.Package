import pprint
import datetime
import investorzilla
import application.salary as salary
import application.db.people as people


if __name__ == '__main__':
    print(datetime.date.today())
    print(f'---begin - from main.py')
    salary.calculate_salary(['Kim'])
    pprint.pprint(people.get_employees(), width=10)
    salary.calculate_salary(people.get_employees())
    print(f'---end - from main.py')

    investorzilla.Portfolio