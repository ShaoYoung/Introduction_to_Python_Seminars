from datetime import datetime as dt

def operation_logger(op, result):
    # получаем время в необходимом формате (здесь часы:минуты)
    time = dt.now().strftime('%D - %H:%M')
    with open('log.csv', 'a') as file:
        file.write(f'{time}: {op} = {result}\n')

