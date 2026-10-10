# cajero automático


saldo_inicial = float(1000)
contador = 0
print(f"Saldo actual= {saldo_inicial}")

while True:
    oper = (
        input(
            """\t Qué operación desea realizar?
             1. Inresar.
             2. Retirar.
             3. Mostrar saldo restante.
             4. Salir. \n"""
        )
        .upper()
        .strip()
    )
    contador += 1
    if oper == "1":
        inr = float(input("Teclee la cantidad a inresar: "))
        saldo_inicial += inr
        print(f"Su saldo actual es: {saldo_inicial}")
    elif oper == "2":
        inr = float(input("Teclee la cantidad a retirar: "))
        if inr <= saldo_inicial:
            saldo_inicial -= inr
            print(f"Su saldo actual es: {saldo_inicial}")
        else:
            print("Su saldo no es sufuciente")
    elif oper == "3":
        print(f"Su saldo actual es: {saldo_inicial}")
    elif oper != "3" and oper != "1" and oper != "2" and oper != "4":
        print("Caracter no álido.")

    elif oper == "4":
        print(
            f"Ha salido del prorama satisfactoriamente, realizó {contador} operaciones."
        )
        break
