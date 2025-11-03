import pygame
from pygame.locals import *
import sys
from core.first_eye import Screen_Manager
from core.handler import Manager

def main():
    pygame.init()  
    pygame.font.init()  

    mr = Screen_Manager()  
    mg = Manager()  
    while 1:
        if mr.status == 0: 
            mr.open_game_init()
        if mg.status == 1:  
            mg.reset_animal()  
            AnimalSpriteGroup = mg.start_game_init()
            mg.clear_ele()  
        for event in pygame.event.get():  # 事件的监听与循环
            if event.type == KEYDOWN:
                if event.key == K_q or event.key == K_ESCAPE:
                    sys.exit()
            if event.type == QUIT:
                sys.exit()
            mg.mouse_select(event) 
            mr.mouse_select(event)  