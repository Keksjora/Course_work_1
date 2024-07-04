import pandas as pd

import src.config
from src.reports import spending_by_workday
from src.services import analyze_cashback
from src.views import main, user_choice

# web сервисов
main_page = main(src.config.input_date_str, user_choice, src.config.api_key_currency, src.config.api_key_stocks)
print(main_page)

# сервисы
cashback_analysis_result = analyze_cashback(src.config.transactions, src.config.year, src.config.month)
print(cashback_analysis_result)

# отчёты
df = pd.read_excel(r"../data/operations.xls")
spending_by_workday_result = spending_by_workday(df, "2020.05.20")
print(spending_by_workday_result)
