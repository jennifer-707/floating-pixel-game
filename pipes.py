import pygame
import random
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT,
    TUBO_ANCHO, TUBO_VELOCIDAD, TUBO_ESPACIO,
    COLOR_MORADO, COLOR_MORADO_OSCURO,
    CREAR_TUBO_EVENT, TUBO_INTERVALO
)


class PipeManager:
    """
    Gestiona la creacion, movimiento, puntuacion y dibujo
    de todos los tubos en la pantalla
    """

    def _init_(self):
        self.tubos: list[pygame.Rect] = []
        self.city_height = SCREEN_HEIGHT - GROUND_HEIGHT

    
    # Control del temporizador

    def iniciar_timer(self):
        """Activa el evento de creacion de tubos"""
        pygame.time.set_timer(CREAR_TUBO_EVENT, TUBO_INTERVALO)

    def detener_timer(self):
        """Desactiva el evento de creacion de tubos"""
        pygame.time.set_timer(CREAR_TUBO_EVENT, 0)

    
    # Creacion de tubos

    def crear_par(self):
        """
        Genera tubos (arriba y abajo) con una
        altura aleatoria y los agrega a la lista
        """
        altura_top = random.randint(60, self.city_height - TUBO_ESPACIO - 60)

        tubo_top = pygame.Rect(SCREEN_WIDTH, 0, TUBO_ANCHO, altura_top)

        y_bottom = altura_top + TUBO_ESPACIO
        alto_bottom = self.city_height - y_bottom
        tubo_bottom = pygame.Rect(SCREEN_WIDTH, y_bottom, TUBO_ANCHO, alto_bottom)

        self.tubos.append(tubo_top)
        self.tubos.append(tubo_bottom)


    # Actualizaciones

    def update(self, bird_x: int) -> int:
        """
        Mueve todos los tubos hacia la izquierda, elimina los
        que salen de pantalla y cuenta los puntos ganados

        Retorna: cantidad de puntos ganados(0 o 1)
        """
        puntos_ganados = 0

        for tubo in self.tubos:
            # Detectar cuando el tubo de arriba cruza al personaje
            if (tubo.y == 0
                    and tubo.x + tubo.width // 2 <= bird_x
                    and tubo.x + tubo.width // 2 > bird_x - TUBO_VELOCIDAD):
                puntos_ganados += 1

            tubo.x -= TUBO_VELOCIDAD

        # Eliminar tubos fuera de pantalla
        self.tubos = [t for t in self.tubos if t.right > 0]

        return puntos_ganados


    # Colision

    def colisiona_con(self, player_rect: pygame.Rect) -> bool:
        """
        Comprueba si el rectangulo del jugador colisiona con
        alguno de los tubos activos

        Retorna True si hay colisión, False en caso contrario
        """
        for tubo in self.tubos:
            if player_rect.colliderect(tubo):
                return True
        return False


    # Reset

    def reset(self):
        """Elimina todos los tubos de la lista"""
        self.tubos.clear()


    # Dibujo

    def draw(self, screen: pygame.Surface):
        """Dibuja todos los tubos activos"""
        for tubo in self.tubos:
            pygame.draw.rect(screen, COLOR_MORADO, tubo)
            pygame.draw.rect(screen, COLOR_MORADO_OSCURO, tubo, 3)