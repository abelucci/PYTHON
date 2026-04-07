try:
    a = float(input("Ingresá el primer número: "))
    b = float(input("Ingresá el segundo número: "))
    op = input("Ingresá la operación (+, -, *, /): ")

    if op == "+":
        resultado = a + b
    elif op == "-":
        resultado = a - b
    elif op == "*":
        resultado = a * b
    elif op == "/":
        resultado = a / b
    else:
        raise ValueError("Operación inválida")

except ValueError as e:
    print("Error de valor:", e)
except ZeroDivisionError:
    print("Error: no se puede dividir por cero")
else:
    print("Resultado:", resultado)
finally:
    print("Gracias por usar la calculadora")