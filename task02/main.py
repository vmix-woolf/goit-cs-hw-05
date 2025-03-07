import requests
from fetch import fetch_text
from map_reduce import mapreduce
from visualize import visualize_top_words

if __name__ == '__main__':
    default_url = "https://www.gutenberg.org/cache/epub/75539/pg75539.txt"
    url = input("Введіть URL для аналізу (або натисніть Enter для використання стандартного): ").strip()
    if not url:
        url = default_url

    try:
        text = fetch_text(url)
        word_counts = mapreduce(text)
        visualize_top_words(word_counts)
    except requests.RequestException as e:
        print(f"Помилка при завантаженні тексту: {e}")