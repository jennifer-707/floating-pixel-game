def mover_arriba(indice, opciones):
    return (indice - 1) % len(opciones)

def mover_abajo(indice, opciones):
    return (indice + 1) % len(opciones)

menu_opciones = [
    "Inicio",
    "Personaje",
    "Salir"
]

pause_opciones = [
    "Continuar",
    "Volver al menu"
]

gameover_opciones = [
    "Reintentar",
    "Volver al menu"
]