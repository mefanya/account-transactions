import json


def main():
    with open("/home/mefanya/PycharmProjects/account-transactions/data/operations.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    print(data)


if __name__ == "__main__":
    main()
