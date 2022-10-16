import model as mod
import view
import logger as log


def button_click():
    value_a = view.get_value(1)
    value_b = view.get_value(2)
    operation = view.get_operation()
    if operation == '+':
        result = mod.sum_num(value_a, value_b)
    elif operation == '-':
        result = mod.sub_num(value_a, value_b)
    elif operation == '/':
        result = mod.div_num(value_a, value_b)
    elif operation == '*':
        result = mod.mult_num(value_a, value_b)
    # model.init(value_a, value_b)
    op = f'{value_a} {operation} {value_b}'
    view.view_data(op, result)
    log.operation_logger(op, result)
