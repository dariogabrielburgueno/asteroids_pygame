from circleshape import *
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius=radius
        
    
    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,3)

    def update(self, dt):
        self.position+=self.velocity*dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
             
            asteroide3=Asteroid(self.position.x,self.position.y,2,)
            asteroide3.velocity=self.velocity.rotate(90)
            
                
           
            return
        else: 
            random_angle=random.uniform(20,50)
            vec1=self.velocity.rotate(random_angle)
            vec2=self.velocity.rotate(-random_angle)
            new_radius=self.radius-ASTEROID_MIN_RADIUS

            asteroide1=Asteroid(self.position.x,self.position.y,new_radius)
            asteroide2=Asteroid(self.position.x,self.position.y,new_radius)

            asteroide1.velocity=vec1*1.2
            asteroide2.velocity=vec2*1.2



    
    



    
