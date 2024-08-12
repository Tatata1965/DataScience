search_queries = ["watch new movies", "coffee near me", "how to find the determinant", "python",
                  "data science jobs in UK", "courses for data science", "taxi", "google", "yandex",
                  "bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free",
                  "Statistics courses online from top universities"]
len_queries = len(search_queries)


def zapros(a):
    rez1 = int
    rez2 = int
    rez3 = int
    rez4 = int
    rez5 = int
    rez6 = int
    for i, v in enumerate(a):
        a_split = v.split()
        l = len(a_split)
        b = l / len_queries * 100
        rezult = int(b)
        if l == 1:
            rez1 = rezult
        elif l == 2:
            rez2 = rezult
        elif l == 3:
            rez3 = rezult
        elif l == 4:
            rez4 = rezult
        elif l == 5:
            rez5 = rezult
        elif l == 6:
            rez6 = rezult

    print(f" 1 слово: {rez1}%")
    print(f" 2 словa: 0 %")
    print(f" 3 слова: {rez3}%")
    print(f" 4 слова: {rez4}%")
    print(f" 5 слов: {rez5}%")
    print(f" 6 слов: {rez6}%")


zapros(search_queries)
