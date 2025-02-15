from circleshape import *
from constants import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.x=x
        self.y=y
        

        self.rotation=0
        self.timer=0

        # in the player class
    def triangle(self):
        # Calculate direction vector based on rotation
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius * 0.8
        
        # Create the three points of the triangle
        nose = self.position + forward * self.radius * 0.5
        left = self.position - forward * self.radius * 0.5 - right
        right = self.position - forward * self.radius * 0.5 + right
        
        return [nose, left, right]

    def draw(self, screen):
        pygame.draw.polygon(screen, 'green', self.triangle(), 2)


         

    def rotate(self,dt):
        self.rotation+=PLAYER_TURN_SPEED*dt
    
    def update(self, dt):
        self.timer-=dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
                self.rotate(-dt)
        if keys[pygame.K_d]:
                self.rotate(dt) 
        if keys[pygame.K_w]:
             self.move(dt)
        if keys[pygame.K_s]:
             self.move(-dt)
        if keys[pygame.K_SPACE]:
             self.shoot()
        if keys[pygame.K_ESCAPE]:
            raise SystemExit("Bye bye")

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        
        if self.timer<0:
            shoot=Shot(self.position.x,self.position.y,3)

            shoot.velocity=pygame.Vector2(0,1).rotate(self.rotation)*PLAYER_SHOOT_SPEED
            self.timer=PLAYER_SHOOT_COOLDOWN
         