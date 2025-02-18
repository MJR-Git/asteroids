# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
pygame.init()
from constants import *

screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    game_loop()


#def time():
    #clock = pygame.time.Clock
    #clock.tick(60)
    #dt = 0
    

def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        clock.tick(60)
        dt = (clock.tick()) / 1000
        pygame.display.flip()

    

if __name__ == "__main__":
    main()
