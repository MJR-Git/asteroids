import pygame
from constants import *
from player import Player


def main():
    pygame.init()
    screen = get_screen()
    clock, dt = get_clock()
    player = get_player()

    start()
    game_loop(screen, clock, dt, player)

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

def get_player():
    return Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

def game_loop(screen, clock, dt, player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        player.update(dt)

        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()
