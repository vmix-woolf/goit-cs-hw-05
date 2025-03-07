import re
import collections
import concurrent.futures


# Функція Map: розбиває текст на слова і формує список пар (слово, 1)
def map_words(text):
    words = re.findall(r'\b\w+\b', text.lower())  # Виділяємо слова, ігноруючи регістр
    return [(word, 1) for word in words]


# Функція Reduce: підсумовує значення для кожного слова
def reduce_word_counts(mapped_data):
    word_counts = collections.defaultdict(int)
    for word, count in mapped_data:
        word_counts[word] += count
    return word_counts


# Виконує MapReduce паралельно
def mapreduce(text):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        mapped_results = list(executor.map(map_words, [text]))

    mapped_data = [item for sublist in mapped_results for item in sublist]
    reduced_data = reduce_word_counts(mapped_data)

    return reduced_data
