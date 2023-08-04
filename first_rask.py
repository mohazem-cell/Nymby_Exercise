def reading():
    name_1=input('The name of the first person: ')
    age_1=input('\nThe age of the first person: ')
    name_2=input('\nThe name of the second person: ')
    age_2=input('\nThe age of the second person: ')
    if age_1 > age_2:
        print('{} is older than {}.'.format(*tubl))
    elif age_1 < age_2:
        print('{} is younger than {}'.format(*(tubl)))
    else:
        print('{} and {} are equal'.format(*(tubl)))
    return name_1,age_1,name_2,age_2
    
tubl=tuple(reading())
print(tubl)

