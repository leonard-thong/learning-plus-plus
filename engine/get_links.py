from googlesearch import search


def links(element):
    l = []
    query = element + " computer science"
    for j in search(query, tld="com", num=3, start=0, stop=3, pause=2.0):
        l.append(j)
    return l


if __name__ == '__main__':
    print(links("olufasio omojokun"))
