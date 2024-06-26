# E/19/310 - RANAGE R.D.P.R
# E/10/409 - UDAGAMASOORIYA D.P.

def evaluate_postfix(expression):
    stack = []

    operators = set(['+', '-', '*', '/'])

    for element in expression:
        if element.isdigit():
            stack.append(int(element))
        elif element in operators:

            operand2 = stack.pop()
            operand1 = stack.pop()

            if element == '+':
                result = operand1 + operand2
            elif element == '-':
                result = operand1 - operand2
            elif element == '*':
                result = operand1 * operand2
            elif element == '/':
                result = operand1 / operand2  # Integer division

            stack.append(result)

    return stack[-1]

N = int(input())
equations = [input() for _ in range(N)]

results = []
for equation in equations:
    expression = equation.split()
    result = evaluate_postfix(expression)
    results.append(result)

for result in results:
    print(int(result))