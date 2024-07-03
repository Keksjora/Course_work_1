import json

import pandas as pd

from src.reports import spending_by_workday


def test_spending_by_workday():
    data = {
        "Дата операции": [
            "01.06.2024 12:00:00",
            "02.06.2024 12:00:00",
            "15.05.2024 08:30:00",
            "10.05.2024 15:45:00",
            "25.04.2024 18:20:00",
            "15.04.2024 09:10:00",
            "16.04.2024 09:10:00",
        ],
        "Сумма операции": [1000, 500, 300, 700, 400, 100, 500],
    }
    transactions = pd.DataFrame(data)
    result_current_date = spending_by_workday(transactions)
    expected_result_current_date = {
        "Рабочий": 400.0,  # Средняя сумма операций по рабочим дням
        "Выходной": 750.0,  # Средняя сумма операций по выходным дням
    }
    assert json.loads(result_current_date) == expected_result_current_date

    result_given_date = spending_by_workday(transactions, "2024.06.15")
    expected_result_given_date = {
        "Рабочий": 400.0,  # Средняя сумма операций по рабочим дням
        "Выходной": 750.0,  # Средняя сумма операций по выходным дням
    }
    assert json.loads(result_given_date) == expected_result_given_date
