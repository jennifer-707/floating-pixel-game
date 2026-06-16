import pygame
from config import (
    BIRD_X, BIRD_Y, BIRD_WIDTH, BIRD_HEIGHT,
    GRAVEDAD, FUERZA_SALTO, SCREEN_HEIGHT, GROUND_HEIGHT
)


class Player:
    """
    Gestiona la posicion, fisica y colision del personaje jugable
    """

    def _init_(self, personajes: list, indice: int = 0):
        # Posición inicial
        self.x = BIRD_X
        self.y = BIRD_Y

        # Física vertical
        self.velocidad_y = 0
        self.gravedad = GRAVEDAD
        self.fuerza_salto = FUERZA_SALTO

        # Personajes disponibles e índice activo
        self.personajes = personajes
        self.indice = indice

        # Límite superior del suelo (donde el personaje debe detenerse)
        self.city_height = SCREEN_HEIGHT - GROUND_HEIGHT


    # Propiedades de acceso rápido

    @property
    def personaje_actual(self) -> pygame.Surface:
        """Retorna la imagen del personaje actualmente seleccionado."""
        return self.personajes[self.indice]


    # Control

    def saltar(self):
        """Aplica la fuerza de salto al personaje."""
        self.velocidad_y = self.fuerza_salto


    # Actualizacion de fisica

    def update(self) -> bool:
        """
        Aplica gravedad y actualiza la posicion vertical

        Regresa True si el personaje toco el suelo (game over),
        False en caso contrario
        """
        self.velocidad_y += self.gravedad
        self.y += self.velocidad_y

        # Limitar con el techo
        if self.y < 0:
            self.y = 0
            self.velocidad_y = 0

        # Detectar colisión con el suelo
        if self.y > self.city_height - BIRD_HEIGHT:
            self.y = self.city_height - BIRD_HEIGHT
            self.velocidad_y = 0
            return True  # Tocó el suelo → game over

        return False


    # Colision

    def get_rect(self) -> pygame.Rect:
        """
        Retorna el rectangulo de colision del personaje
        """
        return pygame.Rect(
            self.x + 5,
            self.y + 5,
            BIRD_WIDTH - 10,
            BIRD_HEIGHT - 10
        )


    # Reset

    def reset(self):
        """Restaura la posicion y velocidad iniciales del personaje"""
        self.x = BIRD_X
        self.y = BIRD_Y
        self.velocidad_y = 0


    # Dibujo

    def draw(self, screen: pygame.Surface):
        """Dibuja el personaje actual en la pantalla"""
        screen.blit(self.personaje_actual, (self.x, self.y))

