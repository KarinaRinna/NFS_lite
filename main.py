import  pygame
import pygame.freetype


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode(500, 800)
pygame.display.set_caption('NFS_lite')
background_color = (0, 0, 0)

def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image

my_car_image = get_car_image( filename: 'images/mercedes.png', size: (50, 50), -90)

running = True
while running:
