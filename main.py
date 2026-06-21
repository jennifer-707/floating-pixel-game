import pygame

from config import *
from assets import *
from player import Player
from pipes import *
from game_logic import *

pygame.init()

# cargar recursos
imagen_fondo = cargar_fondo()
personajes = cargar_personajes()
cargar_musica()

# crear jugador
player = Player()

ejecucion = True

while ejecucion:

    for evento in pygame.event.get():
    player.actualizar()

    tubos = mover_tubos(tubos)

    if verificar_colision(
        player.obtener_rect(),
        tubos,
        player.y,
        city_height
    ):
        estado = GAMEOVER

    pygame.display.flip()
