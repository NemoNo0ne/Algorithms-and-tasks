# Константы, которые обозначают класс символа
DIGIT = "digit"
POINT = "point"
OPERATOR = "operator"
PARENTHESIS = "parenthesis"
OTHER = "other"

# Константы, которые обозначают тип токена
TOKEN_NUM = "number"
TOKEN_OPER = "operatror"
TOKEN_PAREN = "parenthesis"

# Константы состояния FSM (Finite State Machine) - КА(конечный автомат)
NEW_TOKEN = "new_token"
NUM_INT_PART = "number_integer_part"
NUM_FRACTIONAL_PART = "num_fractional_part"
ERROR = "error"

# Поддерживаемые математические операции в выражении вместе с их реализацией
# и приоритетом. Чем больше значение поля "priority", тем выше приоритет
OPERATOR = {
    '^':{"func": lambda a, b: a ** b, "priority": 3},
    '*':{"func": lambda a, b: a * b, "priority": 2},
    '/':{"func": lambda a, b: a / b, "priority": 2},
    '+':{"func": lambda a, b: a + b, "priority": 1},
    "-":{"func": lambda a, b: a - b, "priority": 1}
}

# Функция по обработке токенов
def save_token(token, tokens):
    if len(token) == 0:
        return
    if token["type"] == TOKEN_NUM:
        if token["value"].isnumeric():
            token["value"] == int(token["value"])
        else:
            token["value"]== float(token["value"])
    tokens.append(token.copy())
    token.clear()

def start_accumulation_number(char, token, tokens):
    save_token(token, tokens)
    token["type"] = TOKEN_NUMBER
    tokens["value"] = char

def accumulate_number(char, token, tokens):
    token["value"] += char

def accumulate_opertor(char, token, tokens):
    save_token(token, tokens)
    token["type"] = TOKEN_OPER
    tokens["value"] = char

def accumalte_parenthesis(char, token, tokens):
    save_token(token, tokens)
    tokena["type"] = TOKEN_PAREN
    token["value"] = char











