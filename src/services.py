import json
import logging
from datetime import datetime
from typing import Dict, List

logger = logging.getLogger("services")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r"C:/Users/Admin/PycharmProjects/Course_work_1/logs/services.log", mode="w")
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def analyze_cashback(transactions: List[Dict], year: int, month: int) -> str:
    """Принимает список словарей транзакций и считает сумму кэшбека по категориям"""
    try:
        cashback_analysis: Dict = {}
        for transaction in transactions:
            transaction_date = datetime.strptime(transaction["Дата операции"], "%d.%m.%Y %H:%M:%S")
            if transaction_date.year == year and transaction_date.month == month:
                category = transaction["Категория"]
                amount = transaction["Сумма операции"]
                if amount < 0:
                    cashback_value = transaction["Кэшбэк"]
                    if cashback_value is not None and cashback_value >= 0:
                        cashback = float(cashback_value)
                    else:
                        cashback = round(amount * -0.01, 5)
                    if category in cashback_analysis:
                        cashback_analysis[category] += cashback
                    else:
                        cashback_analysis[category] = cashback
        logger.info("Посчитана сумма кэшбека по категориям")
        return json.dumps(cashback_analysis, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Возникла ошибка {e}")
        logger.error(f"Возникла ошибка {e}")
        return ""
