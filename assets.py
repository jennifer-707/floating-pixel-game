import pygame

def cargar_fondo():
    return pygame.image.load(
        "fondo_juego/fondo_pixel_bird.png"
    ).convert()

def cargar_personajes():
    nombres = [
        "personajes/miku.png",
        "personajes/len.png",
        "personajes/usagi.png",
        "personajes/pucca.png"
    ]

    personajes = []

    for nombre in nombres:
        img = pygame.image.load(nombre).convert_alpha()
        img = pygame.transform.scale(img, (60, 60))
        personajes.append(img)

    return personajes

def cargar_musica():
    pygame.mixer.init()
    pygame.mixer.music.load(
        "sounds/The_Last_Quarter.mp3"
    )
    pygame.mixer.music.play(-1)