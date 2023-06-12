# Lê uma linha de números separados por vírgula. Whitespace é ignorado nessa linha.
def read_number_list():
    inp = input()
    numbers = inp.replace(" ", "").split(",")

    try:
        ret_value = [float(number) for number in numbers]
    except ValueError:
        print("Valor inválido na linha")
        print(inp)
        exit(1)

    return ret_value


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


def lagrange_interpolation(x, y, xi):
    n = len(x)
    yi = 0.0

    for i in range(n):
        term = y[i]
        for j in range(n):
            if i != j:
                term *= (xi - x[j]) / (x[i] - x[j])
        yi += term

    return yi


# A entrada de valores é dada pelos valores de x, seguidos pelos valores de y.
# Para finalizar a entrada dos valores de x, basta entrar com um valor vazio.
# Os valores de Y devem ter a mesma quantidade que os de X.
# Por fim, com os valores dados, um ultimo valor é solicitado, o valor a ser
# interpolado.
# Para acelrar testes, é possível usar redirecionamento de stdin, ex:
# python interpolation.py < input.txt
# O arquivo de entrada pode possuir varios casos teste.


def interpolate():
    function_name = input()
    x_values = read_number_list()
    y_values = read_number_list()

    if len(x_values) != len(y_values):
        print("Quantidade de valores de X e Y diferentes")
        exit(1)
    try:
        value_to_interpolate = float(input())
    except EOFError:
        print("Valor a ser interpolado é inválido")
        exit(1)

    print("Nome:", function_name)
    print("Valores de X: ", x_values)
    print("Valores de Y: ", y_values)
    print("Valor a ser interpolado: ", value_to_interpolate)
    print(
        "Valor interpolado por newton: ",
        newton_interpolation(x_values, y_values, value_to_interpolate),
    )
    print(
        "Valor interpolado por lagrange: ",
        lagrange_interpolation(x_values, y_values, value_to_interpolate),
    )


try:
    while True:
        interpolate()
        input()  # Linha vazia entre testes
except EOFError:
    pass
