import pygame
# import sys
from constants import *
import colorsys


def hilbert(order, i):
    hilbert_curve= [
        (0,0),
        (0,1),
        (1,1),
        (1,0)
    ]
    x = hilbert_curve[i & 3][0]
    y = hilbert_curve[i & 3][1]
    
    def zero_fill_right_shift(val, n):
        return (val >> n) if val >= 0 else ((val + 0x100000000) >> n)
    
    i = i >> 2
    
    sqN = 2**order
    
    n = 4
    
    while n <= sqN:
        n2 = n / 2
        if (i & 3) == 0: # Case A: Left-Bottom
            x, y = y,x
        if (i & 3) == 1: # Case A: Left-Bottom
            x, y = x,y+n2
        if (i & 3) == 2: # Case A: Left-Bottom
            x, y = x+n2,y+n2
        if (i & 3) == 3: # Case A: Left-Bottom
            x, y = (n2-1)- y + n2, (n2 - 1) - x
        n *= 2
        i = i >> 2

    return (x,y)

class myApp():
    def __init__(self, title, width, height):
        pygame.init()
        pygame.font.init()
        self.title = title
        self.width = width
        self.height = height
        self.screen = pygame.display
        self.canvas = self.screen.set_mode((width,height))
        self.is_running = True
        self.time_reset = False
        self.order = 1

    def show(self):
        self.canvas.fill((0,0,0))
        # pygame.draw.rect(self.canvas, (255,255,255), (100,100,200,200))
        points = [hilbert(self.order, i) for i in range(2**(2*self.order))]
        for i in range(len(points)-1):
            color = tuple([x*255 for x in colorsys.hsv_to_rgb(i / len(points), 1, 1)])
            pos_1 = (
                int((points[i][0] + 0.5) * self.width/(2**self.order)),
                int((points[i][1] + 0.5) * self.height/(2**self.order))
                )
            pos_2 = (
                int((points[i+1][0] + 0.5) * self.width/(2**self.order)),
                int((points[i+1][1] + 0.5) * self.height/(2**self.order))
                )
            pygame.draw.line(self.canvas,color,pos_1,pos_2)
            self.screen.update()
            # pygame.time.delay(50)
        self.screen.update()
        
        
    def update(self):
        for event in pygame.event.get():
            
            if event.type == pygame.USEREVENT+1:
                print('something')
            
            if event.type == pygame.QUIT:
                self.is_running = False
                
        
        self.show()
        pygame.time.delay(1000)
        self.order += 1


myApp = myApp('Hilbert Curve', WIDTH, HEIGHT)

def p():
    print('something')


while myApp.is_running:
    myApp.update()
    pygame.time.delay(10)
    
pygame.quit()