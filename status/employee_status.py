
def em_st(name,hours):
    if hours==8:
        print(f'employee {name} is a full-time employee')
    elif hours<8:
        print(f'employee {name} is a part-time employee')
    else:
        print(f'{name} is a full time employee with additional hours')

def bonus(name,experience,salary):
    if experience > 5:
        bonus_val=0.5*salary
    else:
        bonus_val = 0.2 * salary

    print(f'{name}  employee gets {bonus_val} tk bonus')

