import pygame
from constants import *
from player import *
from circleshape import *
from asteroidfield import *
from shot import *
from asteroid import *

def main():
    pygame.init()
    pygame.display.set_caption("ASTEROIDS!")
    reloj=pygame.time.Clock()
    dt=0
    print("Starting asteroids!")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    jugador=Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    updatable=pygame.sprite.Group()
    drawable=pygame.sprite.Group()
    updatable.add(jugador)
    drawable.add(jugador)
    asteroids=pygame.sprite.Group()
    Asteroid.containers=(asteroids,updatable,drawable)
    AsteroidField.containers=(updatable)
    asteroid_field=AsteroidField()
    shots=pygame.sprite.Group()
    Shot.containers=(shots,updatable,drawable)
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('ASTEROIDS', True, 'red', 'blue')
    textRect = text.get_rect()
    textRect.center = (600, 200/6 )
    contador_asteroide=0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
       # jugador.update(dt)
        screen.fill((0,0,0))
        screen.blit(text, textRect)
        #jugador.draw(screen)
        updatable.update(dt)
        for ast in asteroids:
            if ast.collision(jugador)==True:

                
                raise SystemExit("Game Over")
        
        for drawa in drawable:
            drawa.draw(screen)
        
        for ast in asteroids:
            for bullet in shots:
                if ast.collision(bullet)==True:
                    pygame.draw.circle(screen, 'yellow' ,(ast.position.x, ast.position.y), 50, 2, True, False, True, False)
                    pygame.draw.circle(screen, 'yellow' ,(ast.position.x, ast.position.y), 30, 1, False, True, False, True)
                    
                    ast.split()
                    bullet.kill()
        
            
        pygame.display.flip()
        

        
        dt=reloj.tick(60)/1000
        #last
        






if __name__=="__main__":
    main()