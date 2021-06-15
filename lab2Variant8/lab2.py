import re


def check_without_input(address):
    print(f'{address} - Да, является' if re.match(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})(\.(?!$)|$)){4}",
                                                  address) else f'{address} - Нет, не является')


def check_with_input():
    print(f'Да, является' if re.match(r"((25[0-5]|2[0-4][0-9]|[01]?[0-9]{1,2})(\.(?!$)|$)){4}",
                                      input()) else f'Нет, не является')


ip_address1 = '127.0.0.1'
ip_address2 = '255.255.255.0'
ip_address3 = '1300.6.7.8'
ip_address4 = 'abc.def.gha.bcd'
x = input('Хотите ли вы ввести свои значения?\n1 - Да\n2 - Нет\n')
if x == '1':
    check_with_input()
else:
    check_without_input(ip_address1)
    check_without_input(ip_address2)
    check_without_input(ip_address3)
    check_without_input(ip_address4)
