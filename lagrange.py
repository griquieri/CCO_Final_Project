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
        lagrange_interpolation(x_values, y_values, value_to_interpolate),
    )


try:
    while True:
        interpolate()
except EOFError:
    pass
