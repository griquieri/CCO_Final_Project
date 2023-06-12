def divided_difference(x, y):
    n = len(x)
    divided_diff = [y[:]]  # Create a copy of y as the first row of divided differences

    for j in range(1, n):
        divided_diff_j = []
        for i in range(n - j):
            diff = (divided_diff[j - 1][i + 1] - divided_diff[j - 1][i]) / (
                x[i + j] - x[i]
            )
            divided_diff_j.append(diff)
        divided_diff.append(divided_diff_j)

    return divided_diff


def newton_interpolation(x, y, xi):
    n = len(x)
    divided_diff = divided_difference(x, y)
    yi = divided_diff[0][0]

    for j in range(1, n):
        term = divided_diff[j][0]
        product = 1.0
        for i in range(j):
            product *= xi - x[i]
        yi += term * product

    return yi


# A entrada de valores é dada pelos valores de x, seguidos pelos valores de y.
# Para finalizar a entrada dos valores de x, basta entrar com um valor vazio.
# Os valores de Y devem ter a mesma quantidade que os de X.
# Por fim, com os valores dados, um ultimo valor é solicitado, o valor a ser
# interpolado.
# Para acelrar testes, é possível usar redirecionamento de stdin, ex:
# python3 lagrange.py < input.txt
# O arquivo de entrada pode possuir varios casos teste.


def interpolate():
    x_values = []

    while True:
        inp = input("")
        if inp == "":
            break
        x_values.append(float(inp))

    if len(x_values) == 0:
        raise Exception("Valores inválidos")

    y_values = []

    for _ in range(len(x_values)):
        inp = input()
        y_values.append(float(inp))

    value_to_interpolate = float(input())

    print("Valores de X: ", x_values)
    print("Valores de Y: ", y_values)
    print("Valor a ser interpolado: ", value_to_interpolate)
    print(
        "Valor interpolado: ",
        newton_interpolation(x_values, y_values, value_to_interpolate),
    )


try:
    while True:
        interpolate()
except EOFError:
    pass
