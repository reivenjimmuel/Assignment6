print('Welcome to Number Sorter!')

N1 = float(input('Enter first number: '))
N2 = float(input('Enter second number: '))
N3 = float(input('Enter third number: '))
N4 = float(input('Enter fourth number: '))

if N1 >= N2 and N1 >= N3 and N1 >= N4: # N1 is the highest number
    if N2 >= N3 and N2 >= N4:
        if N3 >= N4:
            print(f'The sorted numbers from highest to lowest are {N1:.2f}, {N2:.2f}, {N3:.2f}, {N4:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N1:.2f}, {N2:.2f}, {N4:.2f}, {N3:.2f}.')
    elif N3 >= N2 and N3 >= N4:
        if N2 >= N4:
            print(f'The sorted numbers from highest to lowest are {N1:.2f}, {N3:.2f}, {N2:.2f}, {N4:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N1:.2f}, {N3:.2f}, {N4:.2f}, {N2:.2f}.')
    elif N4 >= N2 and N4 >= N3:
        if N2 >= N3:
            print(f'The sorted numbers from highest to lowest are {N1:.2f}, {N4:.2f}, {N2:.2f}, {N3:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N1:.2f}, {N4:.2f}, {N3:.2f}, {N2:.2f}.')
elif N2 >= N1 and N2 >= N3 and N2 >= N4: # N2 is the highest number
    if N1 >= N3 and N1 >= N4:
        if N3 >= N4:
            print(f'The sorted numbers from highest to lowest are {N2:.2f}, {N1:.2f}, {N3:.2f}, {N4:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N2:.2f}, {N1:.2f}, {N4:.2f}, {N3:.2f}.')
    elif N3 >= N1 and N3 >= N4:
        if N1 >= N4:
            print(f'The sorted numbers from highest to lowest are {N2:.2f}, {N3:.2f}, {N1:.2f}, {N4:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N2:.2f}, {N3:.2f}, {N4:.2f}, {N1:.2f}.')
    elif N4 >= N1 and N4 >= N3:
        if N1 >= N3:
            print(f'The sorted numbers from highest to lowest are {N2:.2f}, {N4:.2f}, {N1:.2f}, {N3:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N2:.2f}, {N4:.2f}, {N3:.2f}, {N1:.2f}.')
elif N3 >= N1 and N3 >= N2 and N3 >= N4: # N3 is the highest number
    if N1 >= N2 and N1 >= N4:
        if N2 >= N4:
            print(f'The sorted numbers from highest to lowest are {N3:.2f}, {N1:.2f}, {N2:.2f}, {N4:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N3:.2f}, {N1:.2f}, {N4:.2f}, {N2:.2f}.')
    elif N2 >= N1 and N2 >= N4:
        if N1 >= N4:
            print(f'The sorted numbers from highest to lowest are {N3:.2f}, {N2:.2f}, {N1:.2f}, {N4:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N3:.2f}, {N2:.2f}, {N4:.2f}, {N1:.2f}.')
    elif N4 >= N1 and N4 >= N2:
        if N1 >= N2:
            print(f'The sorted numbers from highest to lowest are {N3:.2f}, {N4:.2f}, {N1:.2f}, {N2:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N3:.2f}, {N4:.2f}, {N2:.2f}, {N1:.2f}.')
elif N4 >= N1 and N4 >= N2 and N4 >= N3: # N4 is the highest number
    if N1 >= N2 and N1 >= N3:
        if N2 >= N3:
            print(f'The sorted numbers from highest to lowest are {N4:.2f}, {N1:.2f}, {N2:.2f}, {N3:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N4:.2f}, {N1:.2f}, {N3:.2f}, {N2:.2f}.')
    elif N2 >= N1 and N2 >= N3:
        if N1 >= N3:
            print(f'The sorted numbers from highest to lowest are {N4:.2f}, {N2:.2f}, {N1:.2f}, {N3:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N4:.2f}, {N2:.2f}, {N3:.2f}, {N1:.2f}.')
    elif N3 >= N1 and N3 >= N2:
        if N1 >= N2:
            print(f'The sorted numbers from highest to lowest are {N4:.2f}, {N3:.2f}, {N1:.2f}, {N2:.2f}.')
        else:
            print(f'The sorted numbers from highest to lowest are {N4:.2f}, {N3:.2f}, {N2:.2f}, {N1:.2f}.')

print('Thank you for using Number Sorter!')