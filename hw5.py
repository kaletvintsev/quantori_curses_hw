import re

if __name__ == '__main__':
    user_input = input('Введите неотрицательные целые числа, разделенные через пробел\n')
    try:
        integers_list = [int(i) for i in user_input.split(' ') if i]
        start_min = 1
        for i in range(100):
            if start_min not in integers_list:
                print(start_min)
                break
            start_min += 1
    except ValueError:
        print('Впишите только цифры')
