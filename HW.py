
#Q1
# class CI(object):
#     def __init__(self, principal, rate, time):
#         self.principal = principal
#         self.rate = rate
#         self.time = time
#     def find_compound_intrest(self):
#         return (self.principal * (1 + self.rate/100)) * self.time
# my_loan = CI(100, .1, 50)
# print(my_loan.find_compound_intrest())


#Q2
# def ascii_calc(text):
#     list_tracker = []
#     calc = 0
#     for x in text:
#         calc += ord(x)
#         list_tracker.append(f'{x} = {ord(x)}')
#     return calc, list_tracker
# print(ascii_calc('hello'))
# def ascii_list(lst):
#     greatest = 0
#     greatest_index = 0
#     for index, text in enumerate(lst):
#         calc = 0
#         for x in text:
#             calc += ord(x)
#         if calc > greatest:
#             greatest = calc
#             greatest_index = index
#     return(f'After calculating all the ascii codes "{lst[greatest_index]}" was the word with the highest value')
# print(ascii_list(['hello', 'goodbye', 'you', 'people']))


#Q3
# from dateutil import rrule
# from datetime import datetime

# def find_ambiguous(date):
#     first = int(date[:2])
#     second = int(date[3:5])
#     if first == second or first > 12 or second > 12:
#         print('the date you entered is non-ambiguous')
#     else:
#         print('the date you entered is ambiguous')
# find_ambiguous('01.05.1995')

# def find_ambig_year(year):
#     a = f'{year}0101'
#     b = f'{year + 1}0101'
#     ambiguous_days = []
#     for dt in rrule.rrule(rrule.DAILY, dtstart=datetime.strptime(a, '%Y%m%d'), until=datetime.strptime(b, '%Y%m%d')):
#         the_day = dt.strftime('%m.%d.%Y')
#         first = int(the_day[:2])
#         second = int(the_day[3:5])
#         if first == second or first > 12 or second > 12:
# #             print(f'{the_day} is non-ambiguous')
#             pass
#         else:
# #             print(f'{the_day} is ambiguous')
#             ambiguous_days.append(the_day)
#     return f'the ambiguous days are {ambiguous_days}'
# print(find_ambig_year(1995))

# def ordinal(n):
#     return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")

# def give_date(date):
#     months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
#     first = int(date[:2])
#     second = int(date[3:5])
#     if first == second:
#         print(f'The {ordinal(first)} of {months[first]}, {date[6:]}')
#     elif first > 12:
#         print(f'The {ordinal(first)} of {months[second]}, {date[6:]}')
#     elif second > 12:
#         print(f'The {ordinal(second)} of {months[first]}, {date[6:]}')
#     else:
#         print(f'The date you entered is ambiguous. so it may be "The {ordinal(second)} of {months[first]}, {date[6:]}" or "The {ordinal(first)} of {months[second]}, {date[6:]}"')
# give_date('05.03.2021')


#Q4
# def find_double_letters(word):
#     for x in range(len(word)-1):
#         if word[x] == word[x+1]:
#             return True
#     return False
# print(find_double_letters('racecar'))


#Q5
# import numpy as np

# tempuratures = ['76.5', '79.1','80.3', '78.3','75.6', '73.2']

# def string_list_temps(lst):
#     num_lst = [float(x) for x in lst]
#     print(round(sum(num_lst)/ len(num_lst), 2))
# string_list_temps(tempuratures)