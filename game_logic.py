from config import *

def verificar_colision(
        player_rect,
        tubos,
        bird_y,
        city_height):

    for tubo in tubos:
        if player_rect.colliderect(tubo):
            return True

    if bird_y > city_height - BIRD_HEIGHT:
        return True

    return False


def actualizar_record(
        puntuacion,
        record_maximo):

    if puntuacion > record_maximo:
        return puntuacion

    return record_maximo