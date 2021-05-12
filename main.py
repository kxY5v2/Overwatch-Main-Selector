import random

# Lists of Tank heroes
Tank = ['D.Va', 'Orisa', 'Reinhardt', 'Roadhog', 'Sigma', 'Winston', 'Wrecking Ball',
        'Zarya']
# Main Tank
M_Tank = ['Orisa', 'Reinhardt', 'Sigma', 'Winston']
# Off Tank
O_Tank = ['D.va', 'Roadhog', 'Zarya', 'Wrecking Ball']

# List of DPS heroes
DPS = ['Ashe', 'Bastion', 'Doomfist', 'Echo', 'Genji', 'Hanzo', 'Junkrat', 'McCree',
       'Mei', 'Phara', 'Reaper', 'Soldier: 76', 'Sombra', 'Symmetra', 'Torbjorn',
       'Tracer', 'Widowmaker']
# Hitscan DPS
H_DPS = ['Ashe', 'Bastion', 'McCree', 'Reaper', 'Soldier: 76', 'Sombra', 'Tracer', 'Widowmaker']
# Projectile DPS
P_DPS = ['Doomfist', 'Echo', 'Genji', 'Hanzo', 'Junkrat', 'Mei', 'Phara', 'Symmetra', 'Torbjorn']

# List of Support heroes
Support = ['Ana', 'Baptiste', 'Brigitte', 'Lucio', 'Mercy', 'Moira', 'Zenyatta']
# Main support
M_Support = ['Ana', 'Baptiste', 'Mercy', 'Moira']
# Off support
O_Support = ['Brigitte', 'Lucio', 'Zenyatta']

# All heroes
All = Tank + DPS + Support


# Get main role
def get_main_role():
    roles = ['Tank', 'DPS', 'Support', 'Any']
    print('Welcome to Overwatch main picker.')
    print('Select a role to pick a main from.')
    roles = list(enumerate(roles, 1))
    for count, item in roles:
        print(' ' + str(count) + ')' + item)
    role = int(input('> '))
    return role


def get_sub_role(role):
    r = {
        1: 'Tank',
        2: 'DPS',
        3: 'Support',
        4: 'Any'
    }
    print(f'You selected {r[role]}.')
    print('Select a sub-role.')
    if role == 1:
        roles = ['Main', 'Off', 'Any']
        roles = list(enumerate(roles, 1))
        for count, item in roles:
            print(' ' + str(count) + ')' + item)
        s = int(input('> '))
        return s
    elif role == 2:
        roles = ['Hitscan', 'Projectile', 'Any']
        roles = list(enumerate(roles, 1))
        for count, item in roles:
            print(' ' + str(count) + ')' + item)
        s = int(input('> '))
        return s
    elif role == 3:
        roles = ['Main', 'Off', 'Any']
        roles = list(enumerate(roles, 1))
        for count, item in roles:
            print(' ' + str(count) + ')' + item)
        s = int(input('> '))
        return s
    else:
        return 4


def get_hero_list(role, sub_role):
    # any
    if role == 4:
        return All
    # main tank
    if role == 1 and sub_role == 1:
        return M_Tank
    # off tank
    elif role == 1 and sub_role == 2:
        return O_Tank
    # any tank
    elif role == 1 and sub_role == 3:
        return Tank
    else:
        if role == 1:
            return Tank
    # hitscan dps
    if role == 2 and sub_role == 1:
        return H_DPS
    # projectile dps
    elif role == 2 and sub_role == 2:
        return P_DPS
    # any dps
    elif role == 2 and sub_role == 3:
        return DPS
    else:
        if role == 2:
            return DPS
    # main support
    if role == 3 and sub_role == 1:
        return M_Support
    # off support
    elif role == 3 and sub_role == 2:
        return O_Support
    # any support
    else:
        if role == 3:
            return Support


def print_list(l):
    #print('Here are the heroes in the role you selected:')
    heroes = list(enumerate(l, 1))
    for count, hero in heroes:
        print('  ' + str(count) + ') ' + hero)


def edit_list(l):
    copy_l = l
    print('Enter the number of the hero you want to remove from consideration.')
    print('Enter 0 to continue.')
    choice = int(input('> '))
    while choice != 0:
        if choice == 0:
            break
        else:
            del copy_l[choice -1]
            print_list(copy_l)
        choice = int(input('> '))
    return copy_l


# pick 3 random heroes in the edited list.
def get_random_heroes(l):
    copy_l = l
    random_heroes = []
    if len(copy_l) >= 3:
        for i in range(3):
            r = random.randint(1, len(copy_l)-1)
            r_hero = copy_l[r]
            random_heroes.append(r_hero)
            del copy_l[r]
        return random_heroes
    else:
        r = random.randint(1, len(copy_l))
        return copy_l[r]


if __name__ == '__main__':
    go = True
    while go:
        main_role = get_main_role()
        sub_role = get_sub_role(main_role)
        my_list = get_hero_list(main_role, sub_role)
        print('Here are the heroes in the role you selected:')
        print_list(my_list)
        edited_list = edit_list(my_list)
        print('Your New Main(s): ')
        random_mains = get_random_heroes(edited_list)
        print_list(random_mains)
        go_again = input('Role again? (y)/(n) ')
        if go_again.lower() == 'y' or go_again.lower() == 'yes':
            continue
        else:
            go = False
            break


