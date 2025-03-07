import matplotlib.pyplot as plt


# Функція для візуалізації топ-слів
def visualize_top_words(word_counts, top_n=10):
    top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
    words, counts = zip(*top_words)

    plt.figure(figsize=(10, 5))
    bars = plt.barh(words, counts, color='skyblue')
    plt.xlabel('Частота')
    plt.ylabel('Слова')
    plt.title(f'Топ-{top_n} найчастіших слів')
    plt.gca().invert_yaxis()

    # Додавання числових значень на кінці стовпчиків
    for bar, count in zip(bars, counts):
        plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, str(count), va='center')

    plt.show()
