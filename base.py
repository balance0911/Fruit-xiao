import pygame

class Base:
    clock=pygame.time.Clock()
    _screen_size=(900,600)
    status=0

    def __init__(self):
        self.screen=pygame.display.set_mode(self._sreen_size)
    pygame.display.set_caption("水果消消乐游戏")