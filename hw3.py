from collections import Counter
from hw2 import split_text

if __name__ == '__main__':
    user_input = input('Введите текст:\n')
    words_list = split_text(user_input)
    words_count = Counter(words_list).most_common()
    if words_count:
        max_count = words_count[0][1]
        for word, word_count in words_count:
            if word_count == max_count:
                max_count = word_count
                print(f'{word} - {word_count}')


