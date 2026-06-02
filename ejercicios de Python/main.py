# =====================================================================
# ESTRUCTURAS DE DATOS INICIALES (Base de datos simulada)
# =====================================================================

inventario_inicial = {
    "101": {"nombre": "Ibuprofeno 400mg", "precio": 450.0, "stock": 15, "categoria": "Analgésico"},
    "102": {"nombre": "Paracetamol 500mg", "precio": 350.0, "stock": 3, "categoria": "Analgésico"},
    "103": {"nombre": "Amoxicilina 500mg", "precio": 1200.0, "stock": 8, "categoria": "Antibiótico"},
    "104": {"nombre": "Loratadina 10mg", "precio": 600.0, "stock": 25, "categoria": "Antihistamínico"},
    "105": {"nombre": "Desloratadina 5mg", "precio": 850.0, "stock": 0, "categoria": "Antihistamínico"}
}

registro_ventas_inicial = [
    {"id_venta": 1, "medicamento_id": "101", "cantidad": 2, "total": 900.0},
    {"id_venta": 2, "medicamento_id": "104", "cantidad": 1, "total": 600.0}
]

# =====================================================================
# SECCIÓN DE EJERCICIOS (FUNCIONES A COMPLETAR POR EL ESTUDIANTE)
# =====================================================================

def buscar_medicamento(inventario, id_buscar):
    try:
        return inventario[id_buscar]
    except KeyError:
        return None

def calcular_descuento(precio_base, categoria_cliente):
    categoria_cliente = categoria_cliente.lower().strip()
    match categoria_cliente:
        case "jubilado":
            return precio_base - (precio_base * 0.30)
        case "afiliado":
            return precio_base - (precio_base * 0.15)
        case "particular":
            return precio_base
        case _:
            return precio_base


def actualizar_stock(inventario, id_med, cantidad):
    try:
        cantidad = int(cantidad)
    except:
        return False
    try:
        if cantidad <= 0:
            raise KeyError
        inventario[id_med]["stock"] += cantidad
        return True
    except KeyError:
        return False

def registrar_venta(inventario, lista_ventas, id_med, cantidad):
    try:
        return True, importe_total

    except:
        return False, 0.0

def calcular_total_ventas(lista_ventas):
    pass

def obtener_bajo_stock(inventario, limite_critico):
    pass

def filtrar_por_categoria(inventario, categoria_buscar):
    pass

def importar_lote(inventario, lista_lote):
    pass

def calcular_precio_promedio(inventario):
    pass

def buscar_por_nombre_coincidente(inventario, fragmento_nombre):
    pass

# =====================================================================
# MENÚ DEL SISTEMA (YA RESUELTO PARA INTERACTUAR)
# =====================================================================

def mostrar_menu():
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN - FARMACIA PY-SALUD")
    print("="*50)
    print("1.  Buscar medicamento por ID")
    print("2.  Calcular descuento para un cliente")
    print("3.  Ingresar mercadería (Sumar Stock)")
    print("4.  Registrar una nueva venta")
    print("5.  Ver facturación total histórica")
    print("6.  Alerta de medicamentos con bajo stock")
    print("7.  Filtrar catálogo por categoría")
    print("8.  Importar lote masivo de medicamentos")
    print("9.  Calcular el precio promedio del catálogo")
    print("10. Buscar medicamentos por coincidencia de nombre")
    print("0.  Salir del sistema")
    print("="*50)

def main():
    inventario = inventario_inicial.copy()
    ventas = registro_ventas_inicial.copy()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-10): ").strip()
        
        if opcion == "0":
            print("\n¡Gracias por utilizar el sistema de la Farmacia Py-Salud! Hasta luego.")
            break
            
        elif opcion == "1":
            print("\n--- [EJERCICIO 1: BUSCAR MEDICAMENTO POR ID] ---")
            id_ingresado = input("Ingrese el ID del medicamento a buscar: ").strip()
            resultado = buscar_medicamento(inventario, id_ingresado)
            if resultado:
                print(f"-> Encontrado: {resultado['nombre']} | Precio: ${resultado['precio']} | Stock: {resultado['stock']} unidades.")
            else:
                print("Error: El ID ingresado no corresponde a ningún producto registrado.")
                
        elif opcion == "2":
            print("\n--- [EJERCICIO 2: CALCULAR DESCUENTO] ---")
            try:
                precio = float(input("Ingrese el precio base del medicamento: $"))
                if precio < 0:
                    raise ValueError
                print("Categorías válidas: jubilado, afiliado, particular")
                categoria = input("Ingrese la categoría del cliente: ")
                precio_final = calcular_descuento(precio, categoria)
                print(f"-> Precio Base: ${precio:.2f} | Precio con Descuento: ${precio_final:.2f}")
            except ValueError:
                print("Error: Por favor, ingrese un precio numérico válido y positivo.")
                
        elif opcion == "3":
            print("\n--- [EJERCICIO 3: ACTUALIZAR STOCK] ---")
            id_med = input("Ingrese el ID del medicamento a reponer: ").strip()
            cantidad = input("Ingrese la cantidad de unidades que ingresan: ").strip()
            exito = actualizar_stock(inventario, id_med, cantidad)
            if exito:
                nuevo_stock = inventario[id_med]["stock"]
                print(f"-> ¡Stock actualizado! Nuevo stock de '{inventario[id_med]['nombre']}': {nuevo_stock} uds.")
            else:
                print("Error: Verifique que el ID exista y la cantidad sea un entero positivo.")
                
        elif opcion == "4":
            print("\n--- [EJERCICIO 4: REGISTRAR VENTA] ---")
            id_med = input("Ingrese el ID del medicamento a vender: ").strip()
            cantidad = input("Ingrese la cantidad a comprar: ").strip()
            exito, total_cobrado = registrar_venta(inventario, ventas, id_med, cantidad)
            if exito:
                print(f"-> ¡Venta Registrada! Medicamento: {inventario[id_med]['nombre']}.")
                print(f"   Monto cobrado: ${total_cobrado:.2f} | Stock restante: {inventario[id_med]['stock']} uds.")
            else:
                print("Error: Venta rechazada. Stock insuficiente, ID inválido o cantidad errónea.")
                
        elif opcion == "5":
            print("\n--- [EJERCICIO 5: FACTURACIÓN TOTAL] ---")
            total = calcular_total_ventas(ventas)
            print(f"-> Facturación acumulada histórica del sistema: ${total:.2f}")
            print(f"-> Cantidad total de operaciones registradas: {len(ventas)}")
            
        elif opcion == "6":
            print("\n--- [EJERCICIO 6: ALERTA DE BAJO STOCK] ---")
            try:
                limite = int(input("Ingrese el umbral de unidades para considerar 'Bajo Stock' (ej. 5): "))
                if limite < 0:
                    raise ValueError
                alertas = obtener_bajo_stock(inventario, limite)
                if alertas:
                    print("⚠️  PRODUCTOS EN ALERTA DE REPOSICIÓN:")
                    for nombre, stock in alertas:
                        print(f"   * {nombre} (Quedan solo {stock} unidades)")
                else:
                    print("-> Excelente: Todos los productos están por encima del límite.")
            except ValueError:
                print("Error: Debe ingresar un número entero positivo.")
                
        elif opcion == "7":
            print("\n--- [EJERCICIO 7: FILTRAR POR CATEGORÍA] ---")
            cat_buscar = input("Ingrese la categoría a filtrar: ").strip()
            resultados = filtrar_por_categoria(inventario, cat_buscar)
            if resultados:
                print(f"Medicamentos encontrados en la categoría '{cat_buscar}':")
                for prod in resultados:
                    print(f"   ID {prod['id']}: {prod['nombre']} | Precio: ${prod['precio']:.2f} | Stock: {prod['stock']} uds.")
            else:
                print(f"-> No se encontraron medicamentos registrados en '{cat_buscar}'.")
                
        elif opcion == "8":
            print("\n--- [EJERCICIO 8: IMPORTAR LOTE MASIVO] ---")
            lote_ejemplo = [
                ("106", "Omeprazol 20mg", 480.0, 50, "Gastrointestinal"),
                ("107", "Losartan 50mg", 920.0, 30, "Cardiología"),
                ("101", "Ibuprofeno Clonado", 100.0, 10, "Analgésico"),
                ("108", "Vitamina C 1g", "Gratis", 100, "Suplemento"),
                ("109", "Paracetamol Jarabe", 310.0, -5, "Analgésico"),
                ("110", "Dexametasona 4mg", 750.0)
            ]
            print("Procesando lote simulado de 6 registros...")
            exitos, fallas = importar_lote(inventario, lote_ejemplo)
            print(f"-> Carga finalizada. Agregados: {exitos} | Rechazados: {fallas}")
            
        elif opcion == "9":
            print("\n--- [EJERCICIO 9: PRECIO PROMEDIO] ---")
            promedio = calcular_precio_promedio(inventario)
            print(f"-> El precio promedio de los medicamentos ofrecidos es: ${promedio:.2f}")
            
        elif opcion == "10":
            print("\n--- [EJERCICIO 10: BUSCADOR POR NOMBRE] ---")
            busqueda = input("Ingrese el nombre (o parte del nombre) a buscar: ").strip()
            coincidencias = buscar_por_nombre_coincidente(inventario, busqueda)
            if coincidencias:
                print(f"Resultados de la búsqueda para '{busqueda}':")
                for prod in coincidencias:
                    print(f"   * ID {prod['id']} | {prod['nombre']} | Precio: ${prod['precio']:.2f} (Stock: {prod['stock']})")
            else:
                print(f"-> No se encontraron medicamentos con esa coincidencia.")
        else:
            print("\nError: Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()