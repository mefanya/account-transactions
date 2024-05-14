from src.utils import filtered_and_sorted, formated_date, mask_account, mask_curd_number, mask_from_to, get_data_correct_format, read_file


data = read_file()


def test_filtered_and_sorted_executed():
    result = filtered_and_sorted(data)

    assert all(payment["state"] == "EXECUTED" for payment in result)


def test_filtered_and_sorted_date():
    result = filtered_and_sorted(data)
    dates = [payment["date"] for payment in result]

    assert all(dates[i] >= dates[i+1] for i in range(len(dates) - 1))


def test_formated_date():
    assert formated_date("2019-08-26T10:50:58.294041") == "26.08.2019"
    assert formated_date("2019-04-04T23:20:05.206878") == "04.04.2019"
    assert formated_date("2018-07-11T02:26:18.671407") == "11.07.2018"


def test_mask_account():
    assert mask_account("64686473678894779589") == "**9589"
    assert mask_account("41421565395219882431") == "**2431"
    assert mask_account("75651667383060284188") == "**4188"


def test_mask_curd_number():
    assert mask_curd_number("1596837868705199") == "1596 83** **** 5199"
    assert mask_curd_number("7158300734726758") == "7158 30** **** 6758"
    assert mask_curd_number("8990922113665229") == "8990 92** **** 5229"


def test_mask_from_to():
    assert mask_from_to("Visa Platinum 8990922113665229") == "Visa Platinum 8990 92** **** 5229"
    assert mask_from_to("Счет 72082042523231456215") == "Счет **6215"
    assert mask_from_to("MasterCard 3595832182277400") == "MasterCard 3595 83** **** 7400"


def test_get_data_correct_format():
    result = filtered_and_sorted(data)

    assert get_data_correct_format(result[0]) == "08.12.2019 Открытие вклада\nСчет **5907\n41096.24 USD"
    assert get_data_correct_format(result[1]) == ("07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> "
                                                  "Счет **3655\n48150.39 USD")
    assert get_data_correct_format(result[2]) == ("19.11.2019 Перевод организации\nMaestro 7810 84** **** 5568 -> Счет "
                                                  "**2869\n30153.72 руб.")
    assert get_data_correct_format(result[3]) == ("13.11.2019 Перевод со счета на счет\nСчет **9794 -> Счет "
                                                  "**8125\n62814.53 руб.")
    assert get_data_correct_format(result[4]) == "05.11.2019 Открытие вклада\nСчет **8381\n21344.35 руб."

