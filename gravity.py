import pygame


WHITE = (255, 255, 255)
RED = (200, 0, 0)
GREEN1 = (0, 200, 0)
GREEN2 = (0, 250, 90)
BLACK = (0, 0, 0)


class Object:
    def __init__(self, x, y, velocity=0):
        self.x = x
        self.y = y
        self.velocity = velocity

    def createobject(self, setscreen, color):
        pass

    def fallundergravity(self, time):
        pass


class Ball(Object):
    def __init__(self, x, y, radius, velocity=0):
        super().__init__(x, y, velocity)
        self.radius = radius

    def createobject(self, setscreen, color):
        pygame.draw.circle(setscreen, color, (self.x, self.y), self.radius)

    def fallundergravity(self, time):
        if self.y < (600 - self.radius):
            self.y = self.y + (self.velocity * time + 0.5 * 10 * time * time)*10
            self.velocity = self.velocity + 10 * time

        elif self.y >= (600 - self.radius):
            self.velocity = -self.velocity
            self.y = self.y + (self.velocity * time + (0.5 * 10 * time * time))*10
            self.velocity = self.velocity + 10 * time


pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
ball1 = Ball(100, 100, 10,5)
ball2 = Ball(234, 123, 30)
ball3 = Ball(300, -200,60)
ball4 = Ball(400, 123, 30,10)
ball5 = Ball(600, 300, 10,50)
ball6 = Ball(500, 400, 100,80)
ball7 = Ball(200, 50, 8,0)
ball8 = Ball(458, 25, 15,4)
ball9 = Ball(550, 90, 12,0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    ball1.fallundergravity(0.02)
    ball2.fallundergravity(0.02)
    ball3.fallundergravity(0.02)
    ball4.fallundergravity(0.02)
    ball5.fallundergravity(0.02)
    ball6.fallundergravity(0.02)
    ball7.fallundergravity(0.02)
    ball8.fallundergravity(0.02)
    ball9.fallundergravity(0.02)
    ball1.createobject(screen, GREEN1)
    ball2.createobject(screen, GREEN2)
    ball3.createobject(screen,RED)
    ball4.createobject(screen,WHITE)
    ball5.createobject(screen,WHITE)
    ball6.createobject(screen,GREEN2)
    ball7.createobject(screen,RED)
    ball8.createobject(screen,WHITE)
    ball9.createobject(screen,RED)
    pygame.display.flip()
    clock.tick(50)
    print(clock.get_fps())


# Quit Pygame
pygame.quit()
