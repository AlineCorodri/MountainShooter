#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.enityFactory import EntityFactory
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        entity = EntityFactory.get_entity('Level1Bg')
        if isinstance(entity, list):  # Se já for uma lista, extend()
            self.entity_list.extend(entity)
        else:  # Se for um único objeto, adiciona com append()
            self.entity_list.append(entity)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Sai do loop quando fechar a janela

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
