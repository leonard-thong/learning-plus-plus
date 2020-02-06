import json


def main(txt):
    with open("dictionary.json", "r") as file:
        data = json.load(file)
        return data.get(txt.upper())
        # print(data.get(txt.upper()))


if __name__ == '__main__':
    print(main("machine learning"))
