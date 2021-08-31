def split_text(text):
    return [i for i in text.split(' ') if i]


if __name__ == '__main__':
    users_input = input('Type text to split with spaces:\n')
    users_input_list = split_text(users_input)
    no_duplicate_list = list(dict.fromkeys(users_input_list))
    print(' '.join(no_duplicate_list))
