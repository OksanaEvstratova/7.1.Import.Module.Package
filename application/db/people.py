import pprint

def get_employees():
    return ['Ivanov', 'Petrov', 'Sidorov']

if __name__ == '__main__':
    print(f'---begin - from people.py')
    pprint.pprint(get_employees(), width=10)
    print(f'---end - from people.py')


