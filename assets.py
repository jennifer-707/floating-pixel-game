import pygame
import sys
from config import (
    SCREEN_HEIGHT, GROUND_HEIGHT, BIRD_WIDTH, BIRD_HEIGHT,
    FONT_NAME, FONT_SIZE
)


def cargar_fuente():
    """Carga la fuente del juego"""
    return pygame.font.SysFont(FONT_NAME, FONT_SIZE)


def cargar_musica():
    """Inicializa el mixer y carga la música de fondo en bucle"""
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/The_Last_Quarter.mp3")
    pygame.mixer.music.play(-1)


def cargar_fondo():
    """
    Carga la imagen de fondo 
    """
    
    try:
        imagen_fondo = pygame.image.load(
            "fondo_juego/fondo_pixel_bird.png"
        ).convert()
    except pygame.error:
        print("Error al cargar la imagen de fondo.")
        pygame.quit()
        sys.exit()

    city_height = SCREEN_HEIGHT - GROUND_HEIGHT

    city_rectangle = pygame.Rect(0, 0, imagen_fondo.get_width(), city_height)
    city_surface = imagen_fondo.subsurface(city_rectangle)

    ground_rectangle = pygame.Rect(
        0, city_height, imagen_fondo.get_width(), GROUND_HEIGHT
    )
    ground_surface = imagen_fondo.subsurface(ground_rectangle)

    return imagen_fondo, city_surface, ground_surface


def cargar_personajes():
    """
    Carga las imágenes de los personajes disponibles,
    las escala al tamaño definido en config y las regresa como una lista

    """
    rutas = [
        "personajes/miku.png",
        "personajes/len.png",
        "personajes/usagi.png",
        "personajes/pucca.png",
    ]

    personajes = []
    try:
        for ruta in rutas:
            img = pygame.image.load(ruta).convert_alpha()
            img = pygame.transform.scale(img, (BIRD_WIDTH, BIRD_HEIGHT))
            personajes.append(img)
    except pygame.error:
        print("Error al cargar personajes.")
        pygame.quit()
        sys.exit()

    return personajes


