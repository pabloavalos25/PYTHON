dias_validos=["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

fecha=input("Ingrese la fecha de hoy en formato dia,DD/MM")
dia_semana,fecha_num=fecha.split(",")

dia_semana=dia_semana.strip().lower()
fecha_num=fecha_num.strip()

dia_num , mes_num = fecha_num.strip().split("/")
dia_num=int(dia_num)
mes_num=int(mes_num)

if dia_semana not in dias_validos:
    print("error, el dia no es correcto")
elif dia_num <1 or dia_num >31:
    print("el número es inválido")
elif mes_num <1 or mes_num >12:
    print("El mes es inválido")
else:
    print(f"fecha válida: {dia_semana.capitalize()}, {dia_num:02d}/{mes_num:02d}")

examen=input("Se tomaron examenes ese día? responde con un SI O NO")
print(examen)

nota_apro=int(input("cuantos aprobaron?"))
print(nota_apro)

notas_repro=int(input("cuantos desaprobaron?"))
print(notas_repro)

total=nota_apro+notas_repro
print(total)

porc_aprob= (nota_apro/total) * 100 
porc_desaprob= (notas_repro/total)* 100
print(f"aprobados: {nota_apro} alumnos ({porc_aprob:.2f}%)")
print(f"desaprobados: {notas_repro} alumnos ({porc_desaprob:.2f}%)")
print()
if dia_semana=="jueves":
    asistencia=float(input("ingrese la cantidad en porcentaje de alumnos que asistieron"))

    if asistencia > 50:
        print("asistió la matoria")
    else:
        print("no asistió la mayoria")
print()
#inglés_viajeros
if dia_num==1 and (mes_num==1 or mes_num==7):
    print("comienzo de nuevo ciclo")

    alumnos=int(input("ingrese la cantidad de alumnos"))
    aranceles=float(input("ingrese el valor del arancel por alumno: "))
    valor_total= alumnos * aranceles
    print(f"ingreso total del ciclo nuevo: ${valor_total:.2f}")