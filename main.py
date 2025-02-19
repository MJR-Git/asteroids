import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet


def main():
    pygame.init()
    screen = get_screen()
    clock, dt = get_clock()
    updatable, drawable, asteroids, bullets = get_groups()
    player = get_player()
    asteroid_field = get_asteroid_field()

    start()
    game_loop(screen, clock, dt, updatable, drawable, asteroids, asteroid_field, bullets, player)

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

def get_asteroid_field():
    return AsteroidField()

def get_groups():
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Bullet.containers = (updatable, drawable, bullets)
    return updatable, drawable, asteroids, bullets

def game_loop(screen, clock, dt, updatables, drawables, asteroids, asteroid_field, bullets, player):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatables.update(dt)

        for i in asteroids:
            if i.collision(player):
                print("Game over!")
                return
            for j in bullets:
                if j.collision(i):
                    i.kill()
                    j.kill()
                    
 
        screen.fill("black")
        for i in drawables:
            i.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    
if __name__ == "__main__":
    main()
