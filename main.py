import pygame
import pygame.freetype
from my_car import MyCar


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('NFS_lite')
background_color = (0, 0, 0)

def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image

my_car_image = get_car_image('images/mercedes.png', (50, 50), -90)

my_car = MyCar((250, 600), my_car_image)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_color)
    my_car.draw(screen)
    pygame.display.flip()
    clock.tick(60)
