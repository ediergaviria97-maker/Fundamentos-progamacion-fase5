# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# Problema 1: Evaluación del nivel de compromiso de sesiones de clientes

def clasificar_compromiso(duracion, clics):
    """
    Evalúa el nivel de compromiso de una sesión según su duración (segundos) y clics.
    """
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"

def generar_informe(matriz_sesiones):
    """
    Recorre la matriz de sesiones e imprime el informe de compromiso por cliente.
    """
    print("=" * 48)
    print(f"{'ID DEL CLIENTE':<18} | {'NIVEL DE COMPROMISO':<25}")
    print("=" * 48)
    
    for sesion in matriz_sesiones:
        id_cliente = sesion[0]
        duracion = sesion[1]
        clics = sesion[2]
        
        nivel = clasificar_compromiso(duracion, clics)
        print(f"{id_cliente:<18} | {nivel:<25}")
        
    print("=" * 48)

def main():
    # Matriz inicial: [ID del Cliente, Duración en segundos, Número de clics]
    sesiones_clientes = [
        ["CLI-001", 210, 12],  # Cumple: Duración > 180 y Clics > 8 -> Alto
        ["CLI-002", 45, 5],    # Cumple: Duración < 60 -> Bajo
        ["CLI-003", 120, 6],   # No cumple Alto ni Bajo -> Medio
        ["CLI-004", 300, 2],   # Cumple: Clics < 3 -> Bajo
        ["CLI-005", 195, 10],  # Cumple: Duración > 180 y Clics > 8 -> Alto
        ["CLI-006", 90, 4]     # No cumple Alto ni Bajo -> Medio
    ]
    
    print("\nINFORME DE COMPROMISO DE USUARIOS EN PLATAFORMA\n")
    generar_informe(sesiones_clientes)

if __name__ == "__main__":
    main()