monto_cuenta= float(input("Ingrese el monto de la cuenta"))
print ("El monto total de la cuenta es de $", monto_cuenta)

propina=monto_cuenta*0.10
propina2=monto_cuenta*0.15

total_pagar= round(monto_cuenta+propina,2)
total_pagar_15= round(monto_cuenta+propina2,2)
print (f"propina sugerida (10%) $ {propina:.2f}" )
print (f"El monto final c/ propina es de: , {total_pagar:.2f}")
print()
print (f"propina sugerida (15%) $ {propina2:.2f}" )
print (f"El monto final c/ propina es de: , {total_pagar_15:.2f}")