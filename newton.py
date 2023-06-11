from decimal import Decimal


def newton_method(f, f_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    iteration = 0

    while abs(f(x)) > tol and iteration < max_iter:
        x = x - f(x) / f_prime(x)
        iteration += 1

    if iteration == max_iter:
        print("Maximum number of iterations reached.")

    return x


def read_function():
    exponent = 0
    coefficients = []
    while True:
        coefficient = input(f"Coeficiente para x^{exponent}: ")
        if coefficient == "END":
            break
        coefficients.append(Decimal(coefficient))
        exponent += 1

    if len(coefficients) == 0:
        raise Exception("Função inválida")

    return coefficients


def apply_function(coefficients: list[Decimal], x: Decimal) -> Decimal:
    acc = 0
    for i, c in enumerate(coefficients):
        acc += c * x ** Decimal(i)

    return acc


fl = read_function()
flp = read_function()

print(newton_method(
    lambda x: apply_function(fl, x),
    lambda x: apply_function(flp, x),
    Decimal(1.5),
))
