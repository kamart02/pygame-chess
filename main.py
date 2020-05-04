import random
import pygame


# constants

FIELD_COLOR_1 = (199, 129, 64)
FIELD_COLOR_2 = (140, 87, 38)
FIELD_SIZE = 100

FIGURE_SIZE = 50
TEMP_WHITE_FIGURE_COLOR = (255, 0, 0)
TEMP_BLACK_FIGURE_COLOR = (0, 0, 255)

WINDOW_HEIGHT = 800
WINDOW_LENGHT = 800

# variables

field_state = []
figure_rect = []
figures = []

fields=[]

last_move=0

white_move=True



def is_attacked(x, y, color):
    for fig in figures:
        if color == fig.color:
            if fig.can_attack(x, y) and not fig.down:
                return True
    return False


class Fig:

    def __init__(self, x, y, color, typee, idd):
        self.x = x
        self.y = y
        self.color = color
        self.type = typee
        self.idd = idd
        self.moved = 0
        self.down = False

    def go_down(self):
        self.down = True
        self.moved = True
        field_state[self.x][self.y]=0
        self.x = -1
        self.y = -1
        figure_rect[self.idd].center=(-10,-10)
        

    def can_attack(self,x,y):
        if self.color == 'w':
            if self.type == 'p':
                if self.x-1 == x or self.x+1 == x:
                    if True:
                        if self.y-1 == y:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.type == 'r':
                if self.x == x:
                    if self.y > y:
                        for i in range(y+1, self.y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            return True
                    elif self.y < y:
                        for i in range(self.y+1, y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            return True
                    else:
                        return False
                elif self.y == y:
                    if self.x > x:
                        for i in range(x+1, self.x):
                            if field_state[i][y] > 0:
                                return False
                        else:
                            return True
                    elif self.x < x:
                        for i in range(self.x+1, x):
                            if field_state[i][x] > 0:
                                return False
                        else:
                            return True
                    else:
                        return False
                else:
                    return False
            elif self.type == 'b':
                if abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                    if True:
                        if self.x < x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                        elif self.x > x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                    else:
                        return False

                else:
                    return False
            elif self.type == 'n':
                if self.x+1 == x or self.x-1 == x:
                    if self.y+2 == y or self.y-2 == y:
                        if True:
                            return True
                        else:
                            return False
                    else:
                        return False
                elif self.y+1 == y or self.y-1 == y:
                    if self.x+2 == x or self.x-2 == x:
                        if True:
                            return True
                        else:
                            return False
                    else:
                        return False
            elif self.type == 'q':
                if self.x == x:
                    if self.y > y:
                        for i in range(y+1, self.y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            if True:
                                return True
                    elif self.y < y:
                        for i in range(self.y+1, y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            if True:
                                return True
                    else:
                        return False
                elif self.y == y:
                    if self.x > x:
                        for i in range(x+1, self.x):
                            if field_state[i][y] > 0:
                                return False
                        else:
                            if True:
                                return True
                    elif self.x < x:
                        for i in range(self.x+1, x):
                            if field_state[i][x] > 0:
                                return False
                        else:
                            if True:
                                return True
                    else:
                        return False
                elif abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                    if True:
                        if self.x < x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                        elif self.x > x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                    else:
                        return False
                else:
                    return False
            elif self.type == 'k':
                if abs(self.x-x) < 2 and abs(self.y-y) < 2 and not (self.x == x and self.y == y):
                    if True:
                        if True:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
        elif self.color == 'b':
            if self.type == 'p':
                if self.x-1 == x or self.x+1 == x:
                    if True:
                        if self.y+1 == y:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            elif self.type == 'r':
                if self.x == x:
                    if self.y > y:
                        for i in range(y+1, self.y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            if True:
                                return True
                    elif self.y < y:
                        for i in range(self.y+1, y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            if True:
                                return True
                    else:
                        return False
                elif self.y == y:
                    if self.x > x:
                        for i in range(x+1, self.x):
                            if field_state[i][y] > 0:
                                return False
                        else:
                            if True:
                                return True
                    elif self.x < x:
                        for i in range(self.x+1, x):
                            if field_state[i][x] > 0:
                                return False
                        else:
                            if True:
                                return True
                    else:
                        return False
                else:
                    return False
            elif self.type == 'b':
                if abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                    if True:
                        if self.x < x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                        elif self.x > x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                    else:
                        return False

                else:
                    return False
            elif self.type == 'n':
                if self.x+1 == x or self.x-1 == x:
                    if self.y+2 == y or self.y-2 == y:
                        if True:
                            return True
                        else:
                            return False
                    else:
                        return False
                elif self.y+1 == y or self.y-1 == y:
                    if self.x+2 == x or self.x-2 == x:
                        if True:
                            return True
                        else:
                            return False
                    else:
                        return False
            elif self.type == 'q':
                if self.x == x:
                    if self.y > y:
                        for i in range(y+1, self.y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            if True:
                                return True
                    elif self.y < y:
                        for i in range(self.y+1, y):
                            if field_state[x][i] > 0:
                                return False
                        else:
                            if True:
                                return True
                    else:
                        return False
                elif self.y == y:
                    if self.x > x:
                        for i in range(x+1, self.x):
                            if field_state[i][y] > 0:
                                return False
                        else:
                            if True:
                                return True
                    elif self.x < x:
                        for i in range(self.x+1, x):
                            if field_state[i][x] > 0:
                                return False
                        else:
                            if True:
                                return True
                    else:
                        return False
                elif abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                    if True:
                        if self.x < x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x+i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                        elif self.x > x:
                            if self.y < y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y+i] > 0:
                                        return False
                                else:
                                    return True
                            elif self.y > y:
                                for i in range(1, abs(self.x-x)):
                                    if field_state[self.x-i][self.y-i] > 0:
                                        return False
                                else:
                                    return True
                    else:
                        return False
                else:
                    return False
            elif self.type == 'k':
                if abs(self.x-x) < 2 and abs(self.y-y) < 2 and not (self.x == x and self.y == y):
                    if True:
                        if True:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False

    def can_move(self, x, y):
        if self.color == 'w':
            #simulating movment
            xyid=field_state[x][y]
            currentx=self.x
            currnety=self.y

            figures[xyid].x=-1
            figures[xyid].y=-1
            figures[xyid].down=True

            field_state[x][y]=self.idd
            field_state[currentx][currnety]=0

            self.x=x
            self.y=y

            if not is_attacked(figures[1].x,figures[1].y,'b'):
                    #returning state
                field_state[currentx][currnety]=self.idd
                field_state[x][y]=xyid

                self.x=currentx
                self.y=currnety
                if xyid>0:
                    figures[xyid].x=x
                    figures[xyid].y=y
                    figures[xyid].down=False

                if self.type == 'p':
                    if self.x == x:
                        if field_state[x][y] == 0:
                            if self.y-1 == y:
                                return True
                            elif self.y-2 == y:
                                if self.moved == False:
                                    if field_state[x][self.y-1]==0:
                                        return True
                                    else:
                                        return False
                            else:
                                return False
                        else:
                            return False
                    elif self.x-1 == x or self.x+1 == x:
                        if field_state[x][y] > 0 and figures[field_state[x][y]].color == 'b':
                            if self.y-1 == y:
                                return True
                            else:
                                return False
                        elif self.y==3:
                            if field_state[x][y+1] > 0:
                                if figures[field_state[x][y+1]].type=='p' and figures[field_state[x][y+1]].moved==1 and last_move==field_state[x][y+1]:
                                    return 'fly'
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                elif self.type == 'r':
                    if self.x == x:
                        if self.y > y:
                            for i in range(y+1, self.y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        elif self.y < y:
                            for i in range(self.y+1, y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        else:
                            return False
                    elif self.y == y:
                        if self.x > x:
                            for i in range(x+1, self.x):
                                if field_state[i][y] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        elif self.x < x:
                            for i in range(self.x+1, x):
                                if field_state[i][x] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        else:
                            return False
                    else:
                        return False
                elif self.type == 'b':
                    if abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                        if figures[field_state[x][y]].color != 'w':
                            if self.x < x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                            elif self.x > x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                        else:
                            return False

                    else:
                        return False
                elif self.type == 'n':
                    if self.x+1 == x or self.x-1 == x:
                        if self.y+2 == y or self.y-2 == y:
                            if figures[field_state[x][y]] != 'w':
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif self.y+1 == y or self.y-1 == y:
                        if self.x+2 == x or self.x-2 == x:
                            if figures[field_state[x][y]] != 'w':
                                return True
                            else:
                                return False
                        else:
                            return False
                elif self.type == 'q':
                    if self.x == x:
                        if self.y > y:
                            for i in range(y+1, self.y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        elif self.y < y:
                            for i in range(self.y+1, y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        else:
                            return False
                    elif self.y == y:
                        if self.x > x:
                            for i in range(x+1, self.x):
                                if field_state[i][y] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        elif self.x < x:
                            for i in range(self.x+1, x):
                                if field_state[i][x] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'w':
                                    return True
                        else:
                            return False
                    elif abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                        if figures[field_state[x][y]].color != 'w':
                            if self.x < x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                            elif self.x > x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                        else:
                            return False
                    else:
                        return False
                elif self.type == 'k':
                    if abs(self.x-x) < 2 and abs(self.y-y) < 2 and not (self.x == x and self.y == y):
                        if figures[field_state[x][y]].color != 'w':
                            if not is_attacked(x, y, 'b'):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif self.moved==False:
                        if x==6:
                            if figures[field_state[7][7]].type=='r':
                                if figures[field_state[7][7]].moved==False:
                                    if not (is_attacked(4,7,'b') or is_attacked(5,7,'b') or is_attacked(6,7,'b'))and (field_state[5][7]==0 and field_state[6][7]==0):
                                        return 'r'
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        elif x==2:
                            if figures[field_state[0][7]].type=='r':
                                if figures[field_state[0][7]].moved==False:
                                    if not (is_attacked(4,7,'b') or is_attacked(3,7,'b') or is_attacked(2,7,'b'))and (field_state[1][7]==0 and field_state[3][7]==0 and field_state[2][7]==0):
                                        return 'r'
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                    else:
                        return False
            else:
                #returning state
                field_state[currentx][currnety]=self.idd
                field_state[x][y]=xyid

                self.x=currentx
                self.y=currnety
                if xyid>0:
                    figures[xyid].x=x
                    figures[xyid].y=y
                    figures[xyid].down=False

        elif self.color == 'b':
            #simulating movment
            xyid=field_state[x][y]
            currentx=self.x
            currnety=self.y

            figures[xyid].x=-1
            figures[xyid].y=-1
            figures[xyid].down=True

            field_state[x][y]=self.idd
            field_state[currentx][currnety]=0

            self.x=x
            self.y=y

            if not is_attacked(figures[1+16].x,figures[1+16].y,'w'):
                    #returning state
                field_state[currentx][currnety]=self.idd
                field_state[x][y]=xyid

                self.x=currentx
                self.y=currnety
                if xyid>0:
                    figures[xyid].x=x
                    figures[xyid].y=y
                    figures[xyid].down=False

                if self.type == 'p':
                    if self.x == x:
                        if field_state[x][y] == 0:
                            if self.y+1 == y:
                                return True
                            elif self.y+2 == y:
                                if self.moved == False:
                                    if field_state[self.x][self.y+1]==0:
                                        return True
                                    else:
                                        return False
                            else:
                                return False
                        else:
                            return False
                    elif self.x-1 == x or self.x+1 == x:
                        if field_state[x][y] > 0 and figures[field_state[x][y]].color == 'w':
                            if self.y+1 == y:
                                return True
                            else:
                                return False
                        elif self.y==4:
                            if field_state[x][y-1] > 0:
                                if figures[field_state[x][y-1]].type=='p' and figures[field_state[x][y-1]].moved==1 and last_move==field_state[x][y-1]:
                                    return 'fly'
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                    
                    else:
                        return False
                elif self.type == 'r':
                    if self.x == x:
                        if self.y > y:
                            for i in range(y+1, self.y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        elif self.y < y:
                            for i in range(self.y+1, y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        else:
                            return False
                    elif self.y == y:
                        if self.x > x:
                            for i in range(x+1, self.x):
                                if field_state[i][y] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        elif self.x < x:
                            for i in range(self.x+1, x):
                                if field_state[i][x] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        else:
                            return False
                    else:
                        return False
                elif self.type == 'b':
                    if abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                        if figures[field_state[x][y]].color != 'b':
                            if self.x < x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                            elif self.x > x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                        else:
                            return False

                    else:
                        return False
                elif self.type == 'n':
                    if self.x+1 == x or self.x-1 == x:
                        if self.y+2 == y or self.y-2 == y:
                            if figures[field_state[x][y]] != 'b':
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif self.y+1 == y or self.y-1 == y:
                        if self.x+2 == x or self.x-2 == x:
                            if figures[field_state[x][y]] != 'b':
                                return True
                            else:
                                return False
                        else:
                            return False
                elif self.type == 'q':
                    if self.x == x:
                        if self.y > y:
                            for i in range(y+1, self.y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        elif self.y < y:
                            for i in range(self.y+1, y):
                                if field_state[x][i] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        else:
                            return False
                    elif self.y == y:
                        if self.x > x:
                            for i in range(x+1, self.x):
                                if field_state[i][y] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        elif self.x < x:
                            for i in range(self.x+1, x):
                                if field_state[i][x] > 0:
                                    return False
                            else:
                                if figures[field_state[x][y]].color != 'b':
                                    return True
                        else:
                            return False
                    elif abs(self.x-x) == abs(self.y-y) and abs(self.x-x) >= 1:
                        if figures[field_state[x][y]].color != 'b':
                            if self.x < x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x+i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                            elif self.x > x:
                                if self.y < y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y+i] > 0:
                                            return False
                                    else:
                                        return True
                                elif self.y > y:
                                    for i in range(1, abs(self.x-x)):
                                        if field_state[self.x-i][self.y-i] > 0:
                                            return False
                                    else:
                                        return True
                        else:
                            return False
                    else:
                        return False
                elif self.type == 'k':
                    if abs(self.x-x) < 2 and abs(self.y-y) < 2 and not (self.x == x and self.y == y):
                        if figures[field_state[x][y]].color != 'b':
                            if not is_attacked(x, y, 'w'):
                                return True
                            else:
                                return False
                        else:
                            return False
                    elif self.moved==False:
                        if x==6:
                            if figures[field_state[7][0]].type=='r':
                                if figures[field_state[7][0]].moved==False:
                                    if not (is_attacked(4,0,'w') or is_attacked(5,0,'w') or is_attacked(6,0,'w')) and (field_state[5][0]==0 and field_state[6][0]==0):
                                        return 'r'
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                        elif x==2:
                            if figures[field_state[0][0]].type=='r':
                                if figures[field_state[0][0]].moved==False:
                                    if not (is_attacked(4,0,'w') or is_attacked(3,0,'w') or is_attacked(2,0,'w'))and (field_state[1][0]==0 and field_state[3][0]==0 and field_state[2][0]==0):
                                        return 'r'
                                    else:
                                        return False
                                else:
                                    return False
                            else:
                                return False
                    else:
                        return False
            else:
                #returning state
                field_state[currentx][currnety]=self.idd
                field_state[x][y]=xyid

                self.x=currentx
                self.y=currnety
                if xyid>0:
                    figures[xyid].x=x
                    figures[xyid].y=y
                    figures[xyid].down=False


    def move(self, x, y):
        global last_move
        
        if self.can_move(x, y)==True:
            if field_state[x][y] > 0:
                figures[field_state[x][y]].go_down()
            field_state[x][y] = self.idd
            field_state[self.x][self.y] = 0
            self.x = x
            self.y = y
            self.moved = True
            if self.type=='p':
                if self.color=='w':
                    if self.y==0:
                        self.type='q'
                elif self.color=='b':
                    if self.y==7:
                        self.type='q'
            
            last_move=self.idd
            return True
        elif self.can_move(x,y)=='r':
            if field_state[x][y] > 0:
                figures[field_state[x][y]].go_down()
            field_state[x][y] = self.idd
            field_state[self.x][self.y] = 0
            self.x = x
            self.y = y
            self.moved += 1

            if x==6:
                ttt=7
                tt=-1
            else:
                ttt=0
                tt=1
            
            field_state[x+tt][self.y]=field_state[ttt][self.y]
            field_state[ttt][self.y]=0
            figures[field_state[x+tt][self.y]].x=x+tt
            figures[field_state[x+tt][self.y]].moved+=1

            figure_rect[figures[field_state[x+tt][self.y]].idd].center=fields[x+tt][self.y].center
            
            last_move=self.idd
            return True
        elif self.can_move(x,y)=='fly':
            if field_state[x][y] > 0:
                figures[field_state[x][y]].go_down()
            field_state[x][y] = self.idd
            field_state[self.x][self.y] = 0
            self.x = x
            self.y = y
            self.moved +=1

            if self.color=='w':
                figures[field_state[x][y+1]].go_down()
            elif self.color=='b':
                figures[field_state[x][y-1]].go_down()

            
            last_move=self.idd
            return True

        else:
            return False


def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_LENGHT))
    running = True

    need_update=True

    global fields

    moving = 0
    last_pos = [0, 0]

    clock = pygame.time.Clock()

    screen.fill((255, 255, 255))
    pygame.display.flip()

    for x in range(0, 8):
        temp = []
        for y in range(0, 8):
            temp.append(0)
        field_state.append(temp)

    for x in range(0, 33):
        figure_rect.append(pygame.Rect(x,y,FIGURE_SIZE,FIGURE_SIZE))
        

    #setting up the board

    field_state[0][0]=23
    field_state[1][0]=21
    field_state[2][0]=19
    field_state[3][0]=18
    field_state[4][0]=17
    field_state[5][0]=20
    field_state[6][0]=22
    field_state[7][0]=24

    for x in range(0,8):
        field_state[x][1]=x+25

    field_state[0][7]=7
    field_state[1][7]=5
    field_state[2][7]=3
    field_state[3][7]=2
    field_state[4][7]=1
    field_state[5][7]=4
    field_state[6][7]=6
    field_state[7][7]=8

    for x in range(0,8):
        field_state[x][6]=x+9

    print(field_state)

    # pattern

    fields = []

    for x in range(0, FIELD_SIZE*8+1, FIELD_SIZE):
        temp = []
        for y in range(0, FIELD_SIZE*8+1, FIELD_SIZE):
            temp.append(pygame.Rect(x, y, FIELD_SIZE, FIELD_SIZE))

        fields.append(temp)

    figures.append(Fig(-1, -1, 'pink', 'mandatory', 0))
    figures[0].down = True

    # white figures

    figures.append(Fig(4, 7, 'w', 'k', 1))
    figures.append(Fig(3, 7, 'w', 'q', 2))
    figures.append(Fig(2, 7, 'w', 'b', 3))
    figures.append(Fig(5, 7, 'w', 'b', 4))
    figures.append(Fig(1, 7, 'w', 'n', 5))
    figures.append(Fig(6, 7, 'w', 'n', 6))
    figures.append(Fig(0, 7, 'w', 'r', 7))
    figures.append(Fig(7, 7, 'w', 'r', 8))

    for x in range(0, 8):
        figures.append(Fig(x, 6, 'w', 'p', x+9))

    # black figures

    figures.append(Fig(4, 0, 'b', 'k', 1+16))
    figures.append(Fig(3, 0, 'b', 'q', 2+16))
    figures.append(Fig(2, 0, 'b', 'b', 3+16))
    figures.append(Fig(5, 0, 'b', 'b', 4+16))
    figures.append(Fig(1, 0, 'b', 'n', 5+16))
    figures.append(Fig(6, 0, 'b', 'n', 6+16))
    figures.append(Fig(0, 0, 'b', 'r', 7+16))
    figures.append(Fig(7, 0, 'b', 'r', 8+16))

    for x in range(0, 8):
        figures.append(Fig(x, 1, 'b', 'p', x+9+16))

    # figures 

    for it,figure in enumerate(figures):
        if it!=0:
            figure_rect[figure.idd].center=fields[figure.x][figure.y].center

    while running:
        global white_move
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    for it,x in enumerate(fields):
                        for it2,y in enumerate(x):
                            if y.collidepoint(event.pos):
                                if figures[moving].move(it,it2):
                                    figure_rect[moving].center=y.center
                                    moving=0
                                    white_move = not white_move
                                else:
                                    figure_rect[moving].centerx=last_pos[0]
                                    figure_rect[moving].centery=last_pos[1]
                                    moving=0
                                break
                    need_update=True


            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for it,y in enumerate(figure_rect):
                        if y.collidepoint(event.pos):
                            if (figures[it].color=='w' and white_move) or (figures[it].color=='b' and not white_move):
                                last_pos[0]=y.centerx
                                last_pos[1]=y.centery
                                moving=it
                    need_update=True

                    

        # clock.tick(60)

        screen.fill((255, 255, 255))

        for it, column in enumerate(fields):
            for it_2, pl in enumerate(column):
                if it % 2 == 0:
                    if it_2 % 2 == 0:
                        pygame.draw.rect(screen, FIELD_COLOR_1, pl)
                    else:
                        pygame.draw.rect(screen, FIELD_COLOR_2, pl)
                else:
                    if it_2 % 2 == 1:
                        pygame.draw.rect(screen, FIELD_COLOR_1, pl)


                    else:
                        pygame.draw.rect(screen, FIELD_COLOR_2, pl)

        #print(figure_rect)

        font=pygame.font.Font('freesansbold.ttf',32)

        for it, figure in enumerate(figures):
            if not figure.down:
                txt=font.render(figure.type,True,(255,255,255))
                if figure.color=='w':
                    pygame.draw.rect(screen, TEMP_WHITE_FIGURE_COLOR, figure_rect[it])
                elif figure.color=='b':
                    pygame.draw.rect(screen, TEMP_BLACK_FIGURE_COLOR, figure_rect[it])
                screen.blit(txt,figure_rect[it])


        if moving > 0:
            need_update=True
            figure_rect[moving].center = pygame.mouse.get_pos()
            
        if need_update:
            pygame.display.flip()
            need_update=False


main()
