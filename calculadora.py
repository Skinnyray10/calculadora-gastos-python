registro_gastos = {} 
while True:
  nombre_gasto = input("¿En qué gastaste? (o escribe 'salir'): ")
  if nombre_gasto == "salir":
    break
  try: 
   precio = float(input("¿Cuánto costó?: "))
   registro_gastos[nombre_gasto] = precio
  except:
    print("Ingrea un numero valido")
print("--- TICKET DE GASTOS ---")
print("Detalle:", registro_gastos)
print("Total gastado: $", sum(registro_gastos.values()))
