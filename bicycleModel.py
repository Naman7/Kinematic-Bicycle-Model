import pygame
import math
import numpy as np

class Bicycle():
    def __init__(self, screen):
        self.pos = [80,40]
        self.theta = 0
        self.vel = 0
        self.acc = 0
        self.delta = 0
        self.length = 250
        self.screen = screen
            
    def getInput(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            self.acc= 0.3
        elif pressed[pygame.K_DOWN]:
            self.acc= -0.3
        else:
            self.acc= 0
            
        if pressed[pygame.K_LEFT]:
            if self.delta > -0.8:
                self.delta -= 0.02
        elif pressed[pygame.K_RIGHT]:
            if self.delta < 0.8:
                self.delta +=0.02
        
    def Update(self):
        self.vel += self.acc
        if self.vel > 15 or self.vel < -15:
            self.vel -= self.acc
            
        self.pos[0] += self.vel * math.cos(self.theta)
        self.pos[1] += self.vel * math.sin(self.theta)
        self.theta += (self.vel * math.tan(self.delta)) / self.length
        self.vel *= 0.95
    
    
    def display(self):
        x=int(self.pos[0])
        y=int(self.pos[1])
        z=self.length
        a=np.full((150, 5), 200)
        b=np.full((25, 15), 150)
        c=np.full((25, 15), 150)
        d=np.full((170, 28), 0)
        d=pygame.surfarray.make_surface(d).convert_alpha()
        a=pygame.surfarray.make_surface(a).convert_alpha()
        b=pygame.surfarray.make_surface(b).convert_alpha()
        c=pygame.surfarray.make_surface(c).convert_alpha()
        c=pygame.transform.rotate(c, -self.delta*180/3.14)
        r=c.get_rect(midleft=(140,12))
        d.blit(a,(0, 10))
        d.blit(b, (0, 5))
        d.blit(c, r)
        d=pygame.transform.rotate(d, -self.theta*180/3.14)
        self.screen.blit(d, (0+x, 0+y))
        
def main():
    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    done = False
    vehicle = Bicycle(screen)
    while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        screen.fill((0,0,0))
        vehicle.getInput()
        vehicle.Update()
        vehicle.display()
        pygame.display.flip()
        
        
if __name__ == '__main__':

    try:
        main()
    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')
          