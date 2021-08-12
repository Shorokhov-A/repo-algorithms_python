# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
# квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
# прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
# среднего.
# ---------------------------------------------------------------------------------------
# Попробовать испоьзовать специализированные типы коллекции из модуля Collections не успеваю.
# Много времени ушло на решение задачи №2. Сдаю то, что наработал.
companies_num = int(input('Количество предприятий: '))
quarters_num = 4
result = {}
total_profit = 0
for number in range(companies_num):
    company_name = input(f'Наименование предприятия №{number + 1}: ')
    quarter_profit = []
    for quarter in range(quarters_num):
        quarter_profit.append(float(input(f'Прибыль предприятия {company_name} за {quarter + 1} квартал: ')))
    result[company_name] = quarter_profit
    total_profit += sum(quarter_profit)
avg_profit = total_profit / companies_num
above_avg_profit = []
below_avg_profit = []
for key in result:
    if sum(result[key]) > avg_profit:
        above_avg_profit.append(key)
    elif sum(result[key]) < avg_profit:
        below_avg_profit.append(key)
above_avg_profit_str = ', '.join(above_avg_profit)
below_avg_profit_str = ', '.join(below_avg_profit)
print(f'Предприятия, прибыль которых выше средней за год:\n{above_avg_profit_str}')
print(f'Предприятия, прибыль которых ниже средней за год:\n{below_avg_profit_str}')
