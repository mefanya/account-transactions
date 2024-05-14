import json
from utils import filtered_and_sorted, get_data_correct_format, read_file


def main():
    data = read_file()

    print("Сколько последних операций хотите получить?")
    user_input = int(input("Введите число: "))

    item = filtered_and_sorted(data)

    if user_input > len(item):
        user_input = len(item)

    for i in range(int(user_input)):
        print()
        print(get_data_correct_format(item[i]))


if __name__ == "__main__":
    main()
