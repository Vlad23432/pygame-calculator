numbers = '1234567890'
operands = {
    '=': 'equals',
    '+': 'plus',
    '-': 'minus',
    '%': 'percent',
    '/': 'digit',
    'x': 'X'
}
methods = {
    ',': 'comma',
    'AC': 'reset',
    '+/-': 'change'
}

def getTypeCommand(text):
    if text in numbers:
        return 'number'
    if text in methods.keys():
        return 'method'
    if text in operands.keys():
        return 'operand'