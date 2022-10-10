import os
import requests
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter


def read_archive(url, adress):
    if os.path.exists(adress):
        print("Arquivo já existe, e não será baixado.")
    else:
        print("Arquivo não existe, baixando...")
        upload_archive(url, adress)


def upload_archive(url, adress):
    anwser = requests.get(url, stream=True)
    if anwser.status_code == requests.codes.OK:
        with open(adress, "wb") as new_archive:
            for line in anwser.iter_content(chunk_size=256):
                new_archive.write(line)
    else:
        anwser.raise_for_status()


def frequency_letters(adress, encode):
    with open(adress, encoding=encode) as f:
        text = f.read().lower()
    letters = [c for c in text if c.isalpha()]
    frequency_letters = Counter(letters)
    return frequency_letters


def compare_common_letters(fr_ltr, fr_ltr_2):
    slice_var = 15
    sliced_fr_ltr = fr_ltr.most_common(slice_var)
    dict_to_list = fr_ltr_2.most_common()

    letters = [i[0] for i in sliced_fr_ltr]

    sliced_fr_ltr_2 = [i for i in dict_to_list if i[0] in letters]

    labels, values = zip(*sliced_fr_ltr)
    _, values_2 = zip(*sliced_fr_ltr_2)

    plt.figure(figsize=(10, 5))
    bar_width = 0.25

    r1 = np.arange(len(values))
    r2 = [x + bar_width for x in r1]

    bar_pt = plt.bar(r1, values, color="b", width=bar_width, label="Português")
    bar_es = plt.bar(r2, values_2, color="r", width=bar_width, label="Espanhol")

    plt.xticks([r + bar_width for r in range(len(values))], labels)
    plt.xlabel("Letras")
    plt.ylabel("Frequência de letras")
    plt.legend()
    plt.title(
        "Livro Lusíadas; Frequência das letras em Português comparada em Espanhol"
    )
    plt.show()


def main():

    adress = "lusiadas-pt.txt"
    encode = "ISO 8859-1"
    frenquency_letter_pt = frequency_letters(adress, encode)

    adress = "lusiadas-es.txt"
    encode = "UTF-8"
    frenquency_letter_esp = frequency_letters(adress, encode)
    compare_common_letters(frenquency_letter_pt, frenquency_letter_esp)

    # url = "https://www.gutenberg.org/files/3333/3333-8.txt"
    # read_archive(url, adress)
    # url = "https://www.gutenberg.org/files/64775/64775-0.txt"
    # read_archive(url, adress)


if __name__ == "__main__":
    main()