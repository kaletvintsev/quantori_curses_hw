import re

if __name__ == '__main__':
    # в задании было написано неотрицательные, хотя в примере сумма вышла меньше нуля, решил сделать как в
    # тз в виду нехватки времени
    user_input = input('Введите целые неотрицательные числа, разделенные любым не цифровым литералом:\n')
    ints_from_input = [int(x.group()) for x in re.finditer(r'\d+', user_input)]
    print(sum(ints_from_input))
