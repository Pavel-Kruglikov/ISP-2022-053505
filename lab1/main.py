import re
from collections import Counter
import statistics as st


# количество повторений слов в тексте
def number_repetitions_words(text):
    text = text.lower()
    my_list = re.split(" |; |, |\\. |! |\\? ", text)
    c = Counter(my_list)
    print("количество повторений слов в тексте: ", end="")
    for a in set(my_list):
        print(a + " - " + str(c[a]), end=' || ')

# среднее количество слов в предложении:
def average_number_words_sentence(line):
    sum = 0
    my_list = re.split('\\. |! ', line)
    for a in range(len(my_list)):
        sum += len(re.split(" |; |, ", my_list[a]))
    return str((sum / len(my_list)))


# медианное среднее
def median_mean(text):
    word_lens = []
    for word in text.split():
        word_lens.append(len(word))
    return str(st.median(word_lens))

# топ K повторяющихся буквенных N-грамм
def top_letter_combinations(text, N=4, K=10):
    my_dick = {}
    text = text.lower()
    my_str = "".join(re.split(" |; |, |\\. |! |\\? ", text))# избавление от знаков припянания и пробелов
    chunks = [my_str[i:i + N] for i in range(0, len(my_str), N)]# раздеение сроки на буквенные N-граммы
    c = Counter(chunks)
    for a in set(chunks):# цикл нахождения количества каждой N-граммы
        my_dick[a] = str(c[a])
    top_list = sorted(my_dick.items(), key=lambda x: x[1], reverse=True)# сортировка словаря с значению
    del top_list[K:]# удаление элементов не входящих в топ
    print("топ " + str(K) + " повторяющихся буквенных " + str(N) + "-грамм: ", end="")
    for a in top_list:
        print(a[0] + " - " + a[1], end=" || ")

file_name = input("название файла: ")
K = int(input("значение K: "))
N = int(input("значение N: "))

# открытие файла
with open(file_name + '.txt') as f:
  text = f.read()

number_repetitions_words(text)
print("\nсреднее количество слов в предложении: " + average_number_words_sentence(text))
print("медианное среднее: " + median_mean(text))
top_letter_combinations(text, N, K)