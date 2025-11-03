import sys
import pygame
from core.base import Base
from core.entity import Font_Fact, Element
from core.handler import Manager

class Score_Manager(Base):
    def __init__(self):
        super(Score_Manager, self).__init__()

    def choice_game_init(self):
        if self.status == 2:
            Element(Element.bg_choice_image, (0, 0)).draw(self.screen)
            li = sorted(Manager.score_list, reverse=True)
            for k, item in enumerate(li[:8]):
                Font_Fact(str(item) + "  Score", \
                          (Element.score_order_rect[0] + 50, \
                           Element.score_order_rect[1] + \
                           k * 50), 35, (0, 0, 0)).draw(self.screen)
            pygame.display.flip()

    def mouse_select(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if self.status == 2:
                if Font_Fact.again_game_posi[0] < mouse_x < \
                        Font_Fact.again_game_posi[0] + 200 and \
                        Font_Fact.again_game_posi[1] < mouse_y < \
                        Font_Fact.again_game_posi[1] + 60:
                    Base.status = 1
                    Manager.destory_animal_num = [0, 0, 0, 0, 0, 0]

                    Manager.start_time = pygame.time.get_ticks()

                elif Font_Fact.quit_game_posi[0] < mouse_x < \
                        Font_Fact.quit_game_posi[0] + 200 and \
                        Font_Fact.quit_game_posi[1] < mouse_y < \
                        Font_Fact.quit_game_posi[1] + 60:
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONUP:
                pass
