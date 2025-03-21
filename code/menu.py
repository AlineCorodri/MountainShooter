#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font
from const import WIN_WIDTH, COLOR_ORANGE, MENU_OPTION, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        """ Renderiza texto na tela """
        text_font: Font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(text_surf, text_rect)

    def run(self, ):
        menu_option = 0
        """ Executa o menu principal """
        try:
            pygame.mixer_music.load('./asset/Menu.mp3')
            pygame.mixer_music.play(-1)
        except pygame.error as e:
            print(f"Erro ao carregar música: {e}")

        while True:
            self.window.blit(self.surf, self.rect)  # Desenha o fundo
            self.menu_text(50, "Mountain", COLOR_ORANGE, (WIN_WIDTH / 2, 70))
            self.menu_text(50, "Shooter", COLOR_ORANGE, (WIN_WIDTH / 2, 120))

            # Posiciona os itens do menu abaixo do título
            start_y = 180  # Posição inicial dos itens
            spacing = 40  # Espaçamento entre itens

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_YELLOW, (WIN_WIDTH / 2, start_y + spacing * i))

                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, (WIN_WIDTH / 2, start_y + spacing * i))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()  # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1

                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[menu_option]
