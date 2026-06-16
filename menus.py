import pygame


class Menu:
    """
    Gestiona el renderizado y la navegacion de teclado para
    el menu principal, la selección de personaje, la pausa
    y la pantalla de game over
    """

    def _init_(self, font: pygame.font.Font):
        self.font = font

        # Opciones de cada menu y sus indices de seleccion
        self.menu_opciones = ["Inicio", "Personaje", "Salir"]
        self.menu_index = 0

        self.pause_opciones = ["Continuar", "Volver al menu"]
        self.pause_index = 0

        self.gameover_opciones = ["Reintentar", "Volver al menu"]
        self.gameover_index = 0


    def _render_lista(
        self,
        screen: pygame.Surface,
        opciones: list[str],
        indice_activo: int,
        x: int,
        y_base: int,
        separacion: int = 50,
        color: tuple = (255, 255, 255),
    ):
        """
        Dibuja una lista de opciones en pantalla, marcando la
        opcion activa con "> ".
        """
        for i, texto in enumerate(opciones):
            label = ("> " + texto) if i == indice_activo else texto
            render = self.font.render(label, True, color)
            screen.blit(render, (x, y_base + i * separacion))


    # MENU PRINCIPAL

    def manejar_evento_menu(self, evento: pygame.event.Event) -> str | None:
        """
        Procesa eventos de teclado en el menu principal

        Retorna la opcion seleccionada como string cuando el usuario
        pulsa ENTER, o None si no hay seleccion
        """
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                self.menu_index = (self.menu_index - 1) % len(self.menu_opciones)
            elif evento.key == pygame.K_s:
                self.menu_index = (self.menu_index + 1) % len(self.menu_opciones)
            elif evento.key == pygame.K_RETURN:
                return self.menu_opciones[self.menu_index]
        return None

    def draw_menu(self, screen: pygame.Surface, ground_surface: pygame.Surface, city_height: int):
        """Dibuja el menu principal"""
        titulo = self.font.render("Floating pixel", True, (255, 255, 255))
        screen.blit(titulo, (100, 100))

        self._render_lista(screen, self.menu_opciones, self.menu_index, 100, 220)

        screen.blit(ground_surface, (0, city_height))

    
    # SELECCION DE PERSONAJE

    def draw_personaje(
        self,
        screen: pygame.Surface,
        personajes: list,
        indice: int,
        ground_surface: pygame.Surface,
        city_height: int,
    ):
        """Dibuja la pantalla de seleccion de personaje"""
        screen.blit(personajes[indice], (170, 220))

        flecha_derecha = self.font.render("->", True, (255, 255, 255))
        screen.blit(flecha_derecha, (240, 250))

        flecha_izquierda = self.font.render("<-", True, (255, 255, 255))
        screen.blit(flecha_izquierda, (120, 250))

        instrucciones = self.font.render("ENTER para seleccionar", True, (255, 255, 255))
        screen.blit(instrucciones, (30, 350))

        screen.blit(ground_surface, (0, city_height))

    # PAUSA

    def manejar_evento_pausa(self, evento: pygame.event.Event) -> str | None:
        """
        Procesa eventos de teclado en la pantalla de pausa

        Retorna la opcion seleccionada como string o None
        """
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                self.pause_index = (self.pause_index - 1) % len(self.pause_opciones)
            elif evento.key == pygame.K_s:
                self.pause_index = (self.pause_index + 1) % len(self.pause_opciones)
            elif evento.key == pygame.K_RETURN:
                return self.pause_opciones[self.pause_index]
        return None

    def draw_pausa(
        self,
        screen: pygame.Surface,
        ground_surface: pygame.Surface,
        ground_x: int,
        city_height: int,
        fondo_ancho: int,
    ):
        """
        Dibuja la pantalla de pausa sobre el estado actual del juego
        Recibe ground_x y fondo_ancho para mantener la posición del suelo
        """
        pausa = self.font.render("PAUSA", True, (255, 255, 255))
        screen.blit(pausa, (140, 150))

        self._render_lista(screen, self.pause_opciones, self.pause_index, 70, 250)


    # GAME OVER

    def manejar_evento_gameover(self, evento: pygame.event.Event) -> str | None:
        """
        Procesa eventos de teclado en la pantalla de game over

        Retorna la opcion seleccionada como string o None
        """
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
                self.gameover_index = (self.gameover_index - 1) % len(self.gameover_opciones)
            elif evento.key == pygame.K_s:
                self.gameover_index = (self.gameover_index + 1) % len(self.gameover_opciones)
            elif evento.key == pygame.K_RETURN:
                return self.gameover_opciones[self.gameover_index]
        return None

    def draw_gameover(
        self,
        screen: pygame.Surface,
        puntuacion: int,
        record_maximo: int,
    ):
        """Dibuja la pantalla de game over con puntuación y record"""
        texto_gameover = self.font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(texto_gameover, (120, 110))

        marcador_actual = self.font.render(f"Puntaje: {puntuacion}", True, (255, 255, 255))
        marcador_record = self.font.render(f"Record Maximo: {record_maximo}", True, (255, 215, 0))
        screen.blit(marcador_actual, (120, 160))
        screen.blit(marcador_record, (80, 200))

        self._render_lista(screen, self.gameover_opciones, self.gameover_index, 110, 280)