from typing import Any


def filtered_and_sorted(data: list) -> list[dict]:
    items = [payment for payment in data if payment.get("state") == "EXECUTED"]
    items.sort(key=lambda x: x.get("date"), reverse=True)
    return items


def get_data_correct_format(items: dict[str, Any]) -> str:
    date = formated_date(items.get("date"))
    amount = items.get("operationAmount").get("amount")
    name = items.get("operationAmount").get("currency").get("name")
    description = items.get("description")
    from_ = mask_from_to(items.get("from"))
    to_ = mask_from_to(items.get("to"))

    if from_:
        from_ += ' -> '
    else:
        from_ = ''

    return f"{date} {description}\n{from_}{to_}\n{amount} {name}"


def formated_date(date):
    date_new_format = date[0:10].split('-')

    return f"{date_new_format[2]}.{date_new_format[1]}.{date_new_format[0]}"


def mask_from_to(number):
    if number is None:
        return ''

    msg = number.split()

    if msg[0] == "Счет":
        number_hidden = mask_account(msg[-1])
    else:
        number_hidden = mask_curd_number(msg[-1])

    return ' '.join(msg[:-1]) + ' ' + number_hidden


def mask_account(number: str):
    if number.isdigit() and len(number) >= 20:
        return f"**{number[-4:]}"


def mask_curd_number(number: str):
    if number.isdigit() and len(number) == 16:
        return f"{number[:4]} {number[4:6]}** **** {number[-4:]}"
