import pygame
import random
from config import *

def crear_tubos(city_height):

    altura_top = random.randint(
        60,
        city_height - TUBO_ESPACIO - 60
    )

    tubo_top = pygame.Rect(
        SCREEN_WIDTH,
        0,
        TUBO_ANCHO,
        altura_top
    )

    y_bottom = altura_top + TUBO_ESPACIO

    tubo_bottom = pygame.Rect(
        SCREEN_WIDTH,
        y_bottom,
        TUBO_ANCHO,
        city_height - y_bottom
    )

    return tubo_top, tubo_bottom


def mover_tubos(tubos):

    for tubo in tubos:
        tubo.x -= TUBO_VELOCIDAD

    return [
        tubo for tubo in tubos
        if tubo.right > 0
    ]