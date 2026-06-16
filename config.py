# Pantalla
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Suelo
GROUND_HEIGHT = 31

# Personaje
BIRD_WIDTH = 60
BIRD_HEIGHT = 60
BIRD_X = 100
BIRD_Y = 250

# Fisica
GRAVEDAD = 0.5
FUERZA_SALTO = -8

# Tubos
TUBO_ANCHO = 60
TUBO_VELOCIDAD = 3
TUBO_ESPACIO = 150

# Suelo (movimiento)
GROUND_SPEED = 3

# Color tubos
COLOR_MORADO = (148, 0, 211)
COLOR_MORADO_OSCURO = (75, 0, 130)

# Fuente
FONT_NAME = "Arial"
FONT_SIZE = 30

# Estados del juego
MENU = "menu"
JUGANDO = "jugando"
PERSONAJE = "personaje"
PAUSA = "pausa"
GAMEOVER = "gameover"

# crear tubos
import pygame
CREAR_TUBO_EVENT = pygame.USEREVENT + 1
TUBO_INTERVALO = 1500  # milisegundos

