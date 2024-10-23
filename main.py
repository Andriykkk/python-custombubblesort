import re


def read_first_sentence(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            first_sentence = re.split(r"[.!?]", text)[0]
            print("Перше речення:")
            print(first_sentence.strip())
            return first_sentence.split(" ")
    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")


def sort_key(word):
    if re.match(r"[а-яА-Я]", word):
        return (0, word.lower())
    elif re.match(r"[a-zA-Z]", word):
        return (1, word.lower())
    else:
        return (2, word.lower())


def bubble_sort(words):
    n = len(words)

    for i in range(n):
        for j in range(0, n - i - 1):
            if sort_key(words[j]) > sort_key(words[j + 1]):
                words[j], words[j + 1] = words[j + 1], words[j]

    return words


def sort_words(words):
    print(words)
    sorted_words = bubble_sort(words)
    return sorted_words


if __name__ == "__main__":
    file_path = "text.txt"
    words = read_first_sentence(file_path)
    if words:
        sorted_words = sort_words(words)

    print("Відсортовані слова: ", sorted_words)
