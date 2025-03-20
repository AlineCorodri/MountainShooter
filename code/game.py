#!/usr/bin/python
# -*- coding: utf-8 -*-
from idlelib import window

import pygame

from code.menu import Menu
from const import WIN_WIDTH, WIN_HEIGHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

