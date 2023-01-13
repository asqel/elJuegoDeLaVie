import pygame
import json


size=15
scr_size=700
gride =[[0 for i in range(scr_size//size)]for i in range(scr_size//size)]


def update():
    l=born()
    l2=die()
    for i in l:
        gride[l[1]][l[0]]==1
    for i in l2:
        gride[l[1]][l[0]]==0

def born():#retourn la list des coordone des point a faire naitre genre [(3,4),(5,6)] avec (x,y)

def main():
    pygame.init()
    screen=pygame.display.set_mode((scr_size,scr_size))
    while True:
        screen.fill((0,0,0))
        for i in pygame.event.get():
            if i.type==pygame.QUIT:
                exit()
        
        for i in range(len(gride)):
            for k in range(len(gride[i])):
                if gride[i][k]==0:
                    for l in range(5):
                        for m in range(5):
                            screen.set_at((k*size+l,i*size+m),(0,0,0))
                else:
                    for l in range(5):
                        for m in range(5):
                            screen.set_at((k*size+m,i*size+l),(255,255,255))
        pygame.display.update()
        update()

main()

