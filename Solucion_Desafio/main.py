import time

print("Calculadora de Promedio de Calificaciones")

time.sleep(2)

nota1 = float(input("Ingrese la primera calificación: "))
while nota1 < 0 or nota1 > 100:
    print("Error. La nota debe estar entre 0 y 100.")
    nota1 = float(input("Ingrese la primera calificación nuevamente: "))


nota2 = float(input("Ingrese la segunda calificación: "))
while nota2 < 0 or nota2 > 100:
    print("Error. La nota debe estar entre 0 y 100.")
    nota2 = float(input("Ingrese la segunda calificación nuevamente: "))


nota3 = float(input("Ingrese la tercera calificación: "))
while nota3 < 0 or nota3 > 100:
    print("Error. La nota debe estar entre 0 y 100.")
    nota3 = float(input("Ingrese la tercera calificación nuevamente: "))
    


nota4 = float(input("Ingrese la cuarta calificación: "))
while nota4 < 0 or nota4 > 100:
    print("Error. La nota debe estar entre 0 y 100.")
    nota4 = float(input("Ingrese la cuarta calificación nuevamente: "))


nota5 = float(input("Ingrese la quinta calificación: "))
while nota5 < 0 or nota5 > 100:
    print("Error. La nota debe estar entre 0 y 100.")
    nota5 = float(input("Ingrese la quinta calificación nuevamente: "))


promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5


print(f"El promedio es: {promedio:.2f}")

if promedio >= 60:
    print("Aprobado")
elif promedio >= 40:
    print("En recuperación")
else:
    print("Reprobado")