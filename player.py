import pygame
from config import *

class Player:

    def __init__(self):
        self.x = 100
        self.y = 250
        self.velocidad_y = 0

    def saltar(self):
        self.velocidad_y = FUERZA_SALTO

    def actualizar(self):
        self.velocidad_y += GRAVEDAD
        self.y += self.velocidad_y

        if self.y < 0:
            self.y = 0
            self.velocidad_y = 0

    def obtener_rect(self):
        return pygame.Rect(
            self.x + 5,
            self.y + 5,
            BIRD_WIDTH - 10,
            BIRD_HEIGHT - 10
        )

    def reiniciar(self):
        self.y = 250
        self.velocidad_y = 0