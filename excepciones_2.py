def divide():

    try:

        op1=float(input("Introduce un numero: "))
        op2=float(input("Introduce otro: "))

        print("La division es: "+str(op1/op2))

    except ValueError:
        print("Valor no es correcto")
    
    except ZeroDivisionError:
        print("No se puede dividir entre cero!!!")

    finally:
        print("Calculo finalizado")


divide()