#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame

from code import entity
from code.entityFactory import EntityFactory
from code.entity import Entity
from const import COLOR_WHITE, WIN_HEIGHT, MENU_OPTION, EVENT_ENEMY, SPAWN_TIME


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.timeout = 20000  # 20 segundos
        self.add_entity('Level1Bg')
        self.add_entity('Player1')
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.add_entity('Player2')
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

    def add_entity(self, entity_name: str):
        entity = EntityFactory.get_entity(entity_name)
        if isinstance(entity, list):
            self.entity_list.extend(entity)
        else:
            self.entity_list.append(entity)

    def run(self):
        """Executa o loop principal do nível."""
        try:
            music_path = f'./asset/{self.name}.mp3'
            pygame.mixer_music.load(music_path)
            pygame.mixer_music.play(-1)
        except pygame.error as e:
            print(f"Erro ao carregar música {music_path}: {e}")

        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    print(f"Inimigo gerado: {choice}")  # Debug: mostra qual inimigo foi gerado
                    self.entity_list.append(EntityFactory.get_entity(choice))  # Adiciona o inimigo à lista

            self.window.fill((0, 0, 0))  # Limpa a tela antes de desenhar

            for ent in self.entity_list:
                self.window.blit(ent.surf, ent.rect)
                ent.move()

            # Exibir informações na tela antes de encerrar
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            pygame.display.flip()

        pygame.quit()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        """Renderiza e exibe texto na tela."""
        text_font = pygame.font.SysFont("Lucida Sans Typewriter", text_size)
        text_surf = text_font.render(text, True, text_color)
        text_rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(text_surf, text_rect)
