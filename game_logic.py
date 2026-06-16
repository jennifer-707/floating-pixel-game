import pygame
import sys

from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GROUND_HEIGHT, GROUND_SPEED,
    MENU, JUGANDO, PERSONAJE, PAUSA, GAMEOVER,
    CREAR_TUBO_EVENT
)
from assets import cargar_fuente, cargar_musica, cargar_fondo, cargar_personajes
from player import Player
from pipes import PipeManager
from menus import Menu


class Game:
    """
    Clase principal del juego. Inicializa pygame, carga los assets,
    y ejecuta el bucle principal
    """

    def _init_(self):
        pygame.init()

        # Pantalla y reloj
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Floating Pixel")
        self.clock = pygame.time.Clock()

        # Assets
        cargar_musica()
        self.font = cargar_fuente()
        self.imagen_fondo, self.city_surface, self.ground_surface = cargar_fondo()
        personajes = cargar_personajes()

        # Dimensiones derivadas
        self.city_height = SCREEN_HEIGHT - GROUND_HEIGHT
        self.fondo_ancho = self.imagen_fondo.get_width()

        # Módulos del juego
        self.player = Player(personajes)
        self.pipe_manager = PipeManager()
        self.menu = Menu(self.font)

        # Estado del juego
        self.estado = MENU

        # Puntuación y record
        self.puntuacion = 0
        self.record_maximo = 0

        # Movimiento del suelo
        self.ground_x = 0

        # Tiempo (para el contador en pantalla)
        self.tiempo_inicio = 0
        self.tiempo_pausa = 0
        self.tiempo_acumulado_pausa = 0

        # Bandera de ejecucion
        self.ejecucion = True


    # Iniciar / reiniciar partida

    def _iniciar_partida(self):
        """Prepara el estado para comenzar o reiniciar una partida"""
        self.estado = JUGANDO
        self.tiempo_inicio = pygame.time.get_ticks()
        self.tiempo_acumulado_pausa = 0
        self.puntuacion = 0
        self.player.reset()
        self.pipe_manager.reset()
        self.pipe_manager.iniciar_timer()


    # Manejo de eventos por estado

    def _manejar_eventos(self):
        """Procesa todos los eventos de pygame segun el estado actual"""
        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:
                self.ejecucion = False

            # Generación periódica de tubos
            if evento.type == CREAR_TUBO_EVENT and self.estado == JUGANDO:
                self.pipe_manager.crear_par()

            # MENU
            if self.estado == MENU:
                opcion = self.menu.manejar_evento_menu(evento)
                if opcion == "Inicio":
                    self._iniciar_partida()
                elif opcion == "Personaje":
                    self.estado = PERSONAJE
                elif opcion == "Salir":
                    self.ejecucion = False

            # SELECCION DE PERSONAJE
            elif self.estado == PERSONAJE:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RIGHT:
                        self.player.indice = (self.player.indice + 1) % len(self.player.personajes)
                    elif evento.key == pygame.K_LEFT:
                        self.player.indice = (self.player.indice - 1) % len(self.player.personajes)
                    elif evento.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                        self.estado = MENU

            # JUGANDO
            elif self.estado == JUGANDO:
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_ESCAPE:
                        self.estado = PAUSA
                        self.tiempo_pausa = pygame.time.get_ticks()
                        self.pipe_manager.detener_timer()
                    elif evento.key == pygame.K_SPACE:
                        self.player.saltar()

            # PAUSA
            elif self.estado == PAUSA:
                opcion = self.menu.manejar_evento_pausa(evento)
                if opcion == "Continuar":
                    tiempo_actual = pygame.time.get_ticks()
                    self.tiempo_acumulado_pausa += tiempo_actual - self.tiempo_pausa
                    self.estado = JUGANDO
                    self.pipe_manager.iniciar_timer()
                elif opcion == "Volver al menu":
                    self.estado = MENU

            # GAME OVER
            elif self.estado == GAMEOVER:
                opcion = self.menu.manejar_evento_gameover(evento)
                if opcion == "Reintentar":
                    self._iniciar_partida()
                elif opcion == "Volver al menu":
                    self.estado = MENU


    # Actualizacion de logica

    def _actualizar(self):
        """Actualiza la logica del juego cuando el estado es jugando"""
        if self.estado != JUGANDO:
            return

        # Mover suelo
        self.ground_x -= GROUND_SPEED
        if self.ground_x <= -self.fondo_ancho:
            self.ground_x = 0

        # Actualizar fisica del personaje y detectar colision con suelo
        toco_suelo = self.player.update()
        if toco_suelo:
            self._game_over()
            return

        # Mover tubos y sumar puntos
        puntos = self.pipe_manager.update(self.player.x)
        self.puntuacion += puntos

        # Detectar colision con tubos
        if self.pipe_manager.colisiona_con(self.player.get_rect()):
            self._game_over()

    def _game_over(self):
        """Transiciona al estado de game over y actualiza el record"""
        self.estado = GAMEOVER
        if self.puntuacion > self.record_maximo:
            self.record_maximo = self.puntuacion
        self.pipe_manager.detener_timer()

    
    # Renderizado

    def _dibujar(self):
        """Dibuja el frame actual segun el estado del juego"""

        # Fondo base siempre presente
        self.screen.blit(self.imagen_fondo, (0, 0))
        self.screen.blit(self.city_surface, (0, 0))

        if self.estado == MENU:
            self.menu.draw_menu(self.screen, self.ground_surface, self.city_height)

        elif self.estado == PERSONAJE:
            self.menu.draw_personaje(
                self.screen,
                self.player.personajes,
                self.player.indice,
                self.ground_surface,
                self.city_height,
            )

        elif self.estado == JUGANDO:
            self._dibujar_jugando()

        elif self.estado == PAUSA:
            self._dibujar_pausa()

        elif self.estado == GAMEOVER:
            self._dibujar_gameover()

        pygame.display.flip()

    def _dibujar_jugando(self):
        """Renderiza todos los elementos del estado de jugando"""
        self.pipe_manager.draw(self.screen)

        # Suelo en movimiento (se repite horizontalmente)
        self.screen.blit(self.ground_surface, (self.ground_x, self.city_height))
        self.screen.blit(
            self.ground_surface,
            (self.ground_x + self.fondo_ancho, self.city_height)
        )

        self.player.draw(self.screen)

        # Puntuacion
        puntos_render = self.font.render(f"Puntos: {self.puntuacion}", True, (255, 255, 255))
        self.screen.blit(puntos_render, (140, 20))

        # Temporizador
        tiempo_actual = pygame.time.get_ticks()
        tiempo_total = (tiempo_actual - self.tiempo_inicio - self.tiempo_acumulado_pausa) // 1000
        minutos = tiempo_total // 60
        segundos = tiempo_total % 60
        timer_render = self.font.render(f"{minutos:02}:{segundos:02}", True, (255, 255, 255))
        self.screen.blit(timer_render, (300, 20))

        # Icono de pausa
        pausa_texto = self.font.render("||", True, (255, 255, 255))
        self.screen.blit(pausa_texto, (20, 20))

    def _dibujar_pausa(self):
        """Renderiza la pantalla de pausa sobre el estado congelado"""
        self.pipe_manager.draw(self.screen)

        self.screen.blit(self.ground_surface, (self.ground_x, self.city_height))
        self.player.draw(self.screen)

        self.menu.draw_pausa(
            self.screen,
            self.ground_surface,
            self.ground_x,
            self.city_height,
            self.fondo_ancho,
        )

    def _dibujar_gameover(self):
        """Renderiza la pantalla de game over"""
        self.pipe_manager.draw(self.screen)

        self.screen.blit(self.ground_surface, (self.ground_x, self.city_height))
        self.player.draw(self.screen)

        self.menu.draw_gameover(self.screen, self.puntuacion, self.record_maximo)

    
    # Bucle principal

    def run(self):
        """Ejecuta el bucle principal del juego"""
        while self.ejecucion:
            self._manejar_eventos()
            self._actualizar()
            self._dibujar()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()