#在core/handler.py文件的Manager类中添加一个destroy_animal_num变量
destory_animal_num=[0,0,0,0,0,0]
#交换的标志，1: 代表交换，-1: 不交换
exchange_status = -1
#记录上一次选中的水果，值为水果索引
last_sel = [-1, -1]
#在core/handler.py文件的Manager类中创建一个clear_ele()方法
def clear_ele(self):
    single_score=self.score
    self.change_value_sign=False
    for i in range(self._height)
        for j in range(self.width):
            if self.exist_right(i,j,5):
                self.change_value_sign=True
                if self.exist_down(i,j+2,3):
                    self.destory_animal_num[self.animal[i][j]]+=7
                    self.change_right(i,j,5)
                    self.change_down(i,j+2,3)
                else:
                    self.destory_animal_num[self.animal[i][j]]+=5
                    self.change_right(i,j,5)

            elif self.exist_right(i,j,4):
                self.change_value_sign=True
                if self.exist_down(i,j+1,3):
                    self.destory_aniaml_num[self.animal[i][j]]+=6
                    self.change_right(i,j,4)
                    self.change_down(i,j+1,3)
                elif self.exist_down(i,j,3):
                    self.destory_aniaml_num[self.animal[i][j]]+= 6
                    self.change_right(i, j, 4)
                    self.change_down(i, j, 3)
                else:
                    self.destory_aniaml_num[self.aniaml[i][j]]+=4
                    self.change_right(i, j, 4)

            elif self.exist_right(i,j,3):
                self.change_value_sign=True
                if self.exist_down(i,j,3):
                    self.destory_aniaml_num[self.animal[i][j]]+=5
                    self.change_right(i,j,3)
                    self.change_down(i,j,3)
                elif self.exist_down(i,j+1,3):
                    self.destory_aniaml_num[self.animal[i][j]]+=5
                    self.change_right(i, j, 3)
                    self.change_down(i, j+1, 3)
                elif self.exist_down(i,j+2,3):
                    self.destory_aniaml_num[self.animal[i][j]]+=5
                    self.change_right(i, j, 3)
                    self.change_down(i, j+2, 3)
                else:
                    self.destory_aniaml_num[self.aniaml[i][j]]+=3
                    self.change_right(i, j, 3)

            elif self.exist_down(i,j,5):
                self.change_value_sign=True
                if self.exist_right(i+2,j,3):
                    self.destory_animal_num[self.animal[i][j]]+=7
                    self.change_down(i, j, 5)
                    self.change_right(i+2,j,3)
                elif self.exist_left(i+2,j,3):
                    self.destory_animal_num[self.animal[i][j]] +=7
                    self.change_down(i, j, 5)
                    self.change_right(i + 2, j, 3)
                else:
                    self.destory_animal_num[self.animal[i][j]] += 5
                    self.change_down(i, j, 5)

            elif self.exist_down(i,j,4):
                self.change_value_sign=True
                if self.exist_right(i+1,j,3):
                    self.destory_animal_num[self.animal[i][j]]+=6
                    self.change_down(i, j, 4)
                    self.change_right(i+1,j,3)
                    elif self.exist_left(i+1,j,3):
                    self.destory_animal_num[self.animal[i][j]] += 6
                    self.change_down(i, j, 4)
                    self.change_right(i + 1, j, 3)
                elif self.exist_right(i+2,j,3):
                    self.destory_animal_num[self.animal[i][j]] += 6
                    self.change_down(i, j, 4)
                    self.change_right(i + 2, j, 3)
                elif self.exist_left(i+2,j,3):
                    self.destory_animal_num[self.animal[i][j]] += 6
                    self.change_down(i, j, 4)
                    self.change_right(i + 2, j, 3)
                else:
                    self.destory_animal_num[self.animal[i][j]] += 4
                    self.change_down(i, j, 4)
            
            # 垂直三连消
            elif self.exist_down(i, j, 3):
                self.change_value_sign = True
                if self.exist_right(i + 1, j, 3):
                    self.destory_animal_num[self.animal[i][j]] += 5
                    self.change_down(i, j, 3)
                    self.change_right(i + 1, j, 3)
                elif self.exist_left(i + 1, j, 3):
                    self.destory_animal_num[self.animal[i][j]] += 5
                    self.change_down(i, j, 3)
                    self.change_left(i + 1, j, 3)
            elif self.exist_right(i + 2, j, 3):
                    self.destory_animal_num[self.animal[i][j]] += 5
                    self.change_down(i, j, 3)
                    self.change_right(i + 2, j, 3)
            elif self.exist_left(i + 2, j, 3):
                    self.destory_animal_num[self.animal[i][j]] += 5
                    self.change_down(i, j, 3)
                    self.change_left(i + 2, j, 3)
            elif self.exist_left(i + 2, j, 2) and \
                        self.exist_right(i + 2, j, 2):
                    self.destory_animal_num[self.animal[i][j]] += 5
                    self.change_down(i, j, 3)
                    self.change_left(i + 2, j, 2)
                    self.change_right(i + 2, j, 2)
            elif self.exist_left(i + 2, j, 2) and \
                        self.exist_right(i + 2, j, 3):
                    self.destory_animal_num[self.animal[i][j]] += 6
                    self.change_down(i, j, 3)
                    self.change_left(i + 2, j, 2)
                    self.change_right(i + 2, j, 3)
            elif self.exist_left(i + 2, j, 3) and \
                        self.exist_right(i + 2, j, 2):
                    self.destory_animal_num[self.animal[i][j]] += 6
                    self.change_down(i, j, 3)
                    self.change_left(i + 2, j, 3)
                    self.change_right(i + 2, j, 2)
            elif self.exist_left(i + 2, j, 3) and \
                        self.exist_right(i + 2, j, 3):
                    self.destory_animal_num[self.animal[i][j]] += 7
                    self.change_down(i, j, 3)
                    self.change_left(i + 2, j, 3)
                    self.change_right(i + 2, j, 3)
            else:
                self.destory_animal_num[self.animal[i][j]] += 3
                self.change_down(i, j, 3)
    self.drop_animal() 

    self.cal_score(self.destory_animal_num)  

    single_score = self.score - single_score

    if single_score < 5:
        pass
    elif single_score < 8: 
        Element(Element.single_score[0], (350, 250)).draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(500)
    elif single_score < 10:  
        Element(Element.single_score[1], (350, 250)).draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(500)
    elif single_score < 15:  
        Element(Element.single_score[2], (350, 250)).draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(500)
    elif single_score < 20:  
        Element(Element.single_score[3], (350, 250)).draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(500)
    elif single_score >= 20: 
        PlaySound()
        Element(Element.single_score[4], (350, 250)).draw(self.screen)
        pygame.display.flip()
        pygame.time.delay(500)

    return self.change_value_sign
def exist_right(self, row, col, num):
    if col <= self._width - num:
        for item in range(num):
            if self.animal[row][col] != self.animal[row][col + item] or self.animal[row][col] == -2:
                break
        else:
            return True
        return False
    else:
        return False

def exist_down(self, row, col, num):
    if row <= self._height - num:
        for item in range(num):
            if self.animal[row][col] != self.animal[row + item][col] or self.animal[row][col] == -2:
                break
        else:
            return True
        return False
    else:
        return False

def exist_left(self, row, col, num):
    if col >= num - 1:
        for item in range(num):
            if self.animal[row][col] != self.animal[row][col - item] or self.animal[row][col] == -2:
                break
        else:
            return True
        return False
    else:
        return False
def change_right(self, row, col, num):
    """ 改变当前水果及右边的 num 个水果为消除状态 """
    for item in range(num):
        self.animal[row][col + item] = -2

def change_down(self, row, col, num):
    for item in range(num):
        self.animal[row + item][col] = -2

def change_left(self, row, col, num):
    for item in range(num):
        self.animal[row][col - item] = -2

def drop_animal(self):
    clock = pygame.time.Clock()
    position = [] 
    for i in range(self._width):
        for j in range(self._height):
            if self.animal[i][j] == -2:
                x, y = self.cell_xy(i, j)
                position.append((x, y))
    if position != []:
        for index in range(0, 9):
            # clock.tick(40)
            for pos in position:
                Element(Element.brick, pos).draw(self.screen)
                Element(Element.bling[index], (pos[0], pos[1])).draw(self.screen)
            pygame.display.flip()
    for i in range(self._width):
        brick_position = []
        fall_animal_list = []
        speed = [0, 1]
        for j in range(self._height):
            if self.animal[i][j] == -2:
                x, y = self.cell_xy(i, j)
                brick_position.append((x, y))
                for m in range(i, -1, -1):
                    if m == 0:  
                        self.animal[m][j] = random.randint(0, 5)
                    else:
                        x, y = self.cell_xy(m - 1, j)
                        brick_position.append((x, y))
                        animal = Element(Element.animal[self.animal[m - 1][j]], (x, y))
                        fall_animal_list.append(animal)
                        self.animal[m][j] = self.animal[m - 1][j]
    while speed != [0, 0] and fall_animal_list != []:
        for position in brick_position:
            Element(Element.brick, position).draw(self.screen)
        for animal_sprite in fall_animal_list:
            animal_sprite.move(speed)
            animal_sprite.draw(self.screen)
            speed = animal_sprite.speed
        pygame.display.flip()

def cal_score(self, destory_animal_num):
    self.score = 0
    for k, num in enumerate(destory_animal_num):
        self.score += self.every_animal_score[k] * num

def mouse_select(self, event):
        if event.type == MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = event.pos  
            if self.status == 1:
                if self.matrix_topleft[0] < mouse_x < \
                    self.matrix_topleft[0] + self._cell_size * self._width \
                    and self.matrix_topleft[1] < mouse_y < \
                    self.matrix_topleft[1] + self._cell_size * self._height:
                    mouse_selected = self.xy_cell(mouse_x, mouse_y)
                    self.cur_sel = mouse_selected

                    if (self.last_sel[0] == self.cur_sel[0] and \
                        abs(self.last_sel[1] - self.cur_sel[1]) == 1) or\
                            (self.last_sel[1] == self.cur_sel[1] and \
                             abs(self.last_sel[0] - self.cur_sel[0]) == 1):
                        self.exchange_status = 1  

                elif Element.stop_position[0] < mouse_x < \
                    Element.stop_position[0] + Manager.stop_width \
                    and Element.stop_position[1] < mouse_y < \
                    Element.stop_position[1] + Manager.stop_width:
                    Base.status = 2
                    self.reset_layout = True  
                else:
                    self.cur_sel = [-1, -1]  
    def exchange_ele(self, AnimalSpriteGroup):
        if self.exchange_status == -1:
            self.last_sel = self.cur_sel
        if self.exchange_status == 1:
            last_x, last_y = self.cell_xy(*self.last_sel)
            cur_x, cur_y = self.cell_xy(*self.cur_sel)
            # 左右 相邻
            if self.last_sel[0] == self.cur_sel[0]: 
                for animal_sur in AnimalSpriteGroup:
                    if animal_sur.rect.topleft == (last_x, last_y):
                        last_sprite = animal_sur
                        last_sprite.speed = [self.cur_sel[1] - \
                                             self.last_sel[1], 0]
                    if animal_sur.rect.topleft == (cur_x, cur_y):
                        cur_sprite = animal_sur
                        cur_sprite.speed = [self.last_sel[1] - \
                                            self.cur_sel[1], 0]
           
            elif self.last_sel[1] == self.cur_sel[1]:
                for animal_sur in AnimalSpriteGroup:
                    if animal_sur.rect.topleft == (last_x, last_y):
                        last_sprite = animal_sur
                        last_sprite.speed = [0, self.cur_sel[0] - \
                                             self.last_sel[0]]
                    if animal_sur.rect.topleft == (cur_x, cur_y):
                        cur_sprite = animal_sur
                        cur_sprite.speed = [0, self.last_sel[0] - \
                                            self.cur_sel[0]]
          
            while last_sprite.speed != [0, 0]:
                pygame.time.delay(5)
                Element(Element.brick, (last_x, last_y)).draw(self.screen)
                Element(Element.brick, (cur_x, cur_y)).draw(self.screen)
                last_sprite.move(last_sprite.speed)
                cur_sprite.move(cur_sprite.speed)
                last_sprite.draw(self.screen)
                cur_sprite.draw(self.screen)
                pygame.display.flip()

            self.change_value()       
            if not self.clear_ele():  
                self.change_value()
            self.exchange_status = -1  
            self.cur_sel = [-1, -1]   
def change_value(self):
        temp = self.animal[self.last_sel[0]][self.last_sel[1]]
        self.animal[self.last_sel[0]][self.last_sel[1]] \
            = self.animal[self.cur_sel[0]][self.cur_sel[1]]
        self.animal[self.cur_sel[0]][self.cur_sel[1]] = temp

def record_score(self):
        if self.score != 0:
            self.score_list.append(self.score)
            self.destory_animal_num = [0, 0, 0, 0, 0, 0]
            self.score = 0    
