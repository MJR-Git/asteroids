import pygame
from constants import *



def main():
    pygame.init()
    screen = get_screen()
    clock, dt = get_clock()

    start()
    game_loop(screen, clock, dt)


def get_screen():
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    return screen


def get_clock():
    clock = pygame.time.Clock()
    dt = 0
    return clock, dt


def start():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    

def game_loop(screen, clock, dt):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        dt = (clock.tick(60)) / 1000
        pygame.display.flip()

    

if __name__ == "__main__":
    main()
