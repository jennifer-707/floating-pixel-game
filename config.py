import pygame

# Pantalla
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Personaje
BIRD_WIDTH = 60
BIRD_HEIGHT = 60

# Física
GRAVEDAD = 0.5
FUERZA_SALTO = -8

# Tubos
TUBO_ANCHO = 60
TUBO_VELOCIDAD = 3
TUBO_ESPACIO = 150

# Suelo
GROUND_HEIGHT = 31
GROUND_SPEED = 3

# Colores
COLOR_MORADO = (148, 0, 211)
COLOR_MORADO_OSCURO = (75, 0, 130)

# Estados
MENU = "menu"
JUGANDO = "jugando"
PERSONAJE = "personaje"
PAUSA = "pausa"
GAMEOVER = "gameover"

# Evento personalizado
CREAR_TUBO_EVENT = pygame.USEREVENT + 1