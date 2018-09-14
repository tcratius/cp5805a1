import os
import re
import sys
import math
import six

def exit():
    sys.exit(0)

def pause():
    if six.PY2:
        raw_input('Press the <ENTER> key to continue...')
    else:
        input('Press the <ENTER> key to continue...')

def display_instructions():
    print('*' * 68)
    print('*\n')
    print('* Generate a Simple Report')
    print('* ------------------------')
    print('* Generates count of values, sum total of all values and the ')
    print('* average off all five numbers')
    print('* Generate a Full Report')
    print('* ----------------------')
    print('* Input for report')
    print('* ----------------')
    print('* When asked, input 5 positive numbers seperated by a space then ')
    print('* press <ENTER> and the program will read your numbers')
    print('*\n')
    print('*'* 68)

def display_full_stats(Number_of_Values, Min, Max, Mean, Std):
    os.system('cls')
    print('*' * 68)
    print('\n')
    print('Full Statistical Report')
    print('-----------------------')
    print('Number of values: {:.0f}'.format(Number_of_Values))
    print('Minimum: {:.0f}'.format(Min))
    print('Maximum: {:.0f}'.format(Max))
    print('Mean: {:.2f}'.format(Mean))
    print('SD: {:.4f}\n\n'.format(Std))

def display_simple_stats(Number_of_Values , Total, Mean):
    os.system('cls')
    print('*' * 68)
    print('\n')
    print('Simple Statistical Report')
    print('-----------------------')
    print('Number of values: {:.0f}'.format(Number_of_Values))
    print('Total: {:.0f}'.format(Total))
    print('Mean: {:.0f}'.format(Mean))

def welcome_screen():
    print('Wellcome to The Basis Statisitician\n\n')
    print('Please choose from the following options\n\n')
    print('\t1 - Read Instructions\n\n')
    print('\t2 - Generate a Simple Report\n\n')
    print('\t3 - Generate a Full Report\n\n')
    print('\t4 - Quit\n\n')

    result = input('Select Option > ')
    return result

def instructions():
    os.system('cls')
    display_instructions()
    pause()
    main()

def get_numbers():
    print('Type in 5 number seperated by a space')
    result = input('Numbers > ')
    numbers = list(map(str, result.split()))
    return numbers

def next_choice():
    print('\n\nOptions: ')
    print('1 to repeat test')
    print('2 for main menu')
    print('3 to exit\n')
    result = input('Choice > ')
    return result

def choice(number):
    result = next_choice()
    pattern = re.compile(r'[^\1\2\3$]')
    match = re.search(pattern, str(result))
    if match:
        if result == '1':
            print('\n\nNew Statistical test')
            check_list(number)
        elif result == '2':
            main()
        elif result == '3':
            print('\n\nGood-Bye')
            exit()

# Test for divisiable by zero, unlikely but good practice.
# Calcumate the average of all the five numbers in the list.
def mean(List):
    try:
       result = sum(List)/len(List)
    except ZeroDivisionError:
        print('The program can not divide by zero.')
    except:
        print('Something else has happened.')

    return result

 # Calculate the standard deviation of the list.
 # Mean is not of type list therefore put in for loop.
def std(List, Mean):
    for i in range(5):
        result = math.pow((List[i] - Mean),2)/5
        result = math.sqrt(result)
    return result

# Genrate the number of cells in the list.
def num_values(List):
    result = len(List)
    return result

def full_stats(List, number):
    result = [float(i) for i in List]
    Number_of_Values = num_values(result)
    Min = min(result)
    Max = max(result)
    Mean = mean(result)
    Std = std(result, Mean)
    display_full_stats(Number_of_Values, Min, Max, Mean, Std)
    choice(number)

def simple_stats(List, number):
    result = [float(i) for i in List]
    Number_of_Values = num_values(result)
    Total = sum(result)
    Mean = mean(result)
    display_simple_stats(Number_of_Values , Total, Mean)
    choice(number)

def isiterable(obj):
    if iter(obj): # iter function
        return True
    else:  # TypeError: is not iterable
        return False

def check_if_right_input(result):
    pattern = re.compile(r'[?+?\d+(?:\.\d+)?]')
    print(result)
    match = re.search(pattern, str(result))
    # isint
    if match:
        if isiterable(result) and len(result) == 5:
            return True
    else:
        print('Error message: invalid input')
        return False

def check_list(number):
    Escape = False
    while not Escape:
        result = get_numbers()
        Escape = check_if_right_input(result)
        if Escape and number == '2':
            simple_stats(result, number)
        elif Escape and number == '3':
            full_stats(result, number)
        else:
            return False

# Take keyboard input from welcome screen function via parameters raw_input and
# First checks if the input is numerical from 1 - 4. The call a conditional if
# statement to work out where the user wishes to go.
def user_input_option(raw_input):
    pattern = re.compile(r'[^\1\2\3\4$]')
    match = re.search(pattern, str(raw_input))
    if match:
        if raw_input == '1':
            instructions()
        elif raw_input == '2':
            check_list(raw_input)
        elif raw_input == '3':
            check_list(raw_input)
        elif raw_input == '4':
            exit()
        else:
            return False, raw_input

# Conditional loop
def main():
    Escape = False
    while not Escape:
        os.system('cls')
        result = welcome_screen()
        Escape, choice = user_input_option(result)
        Escape = check_list(choice)

main()
