import pygame
import pygame.freetype
from my_car import MyCar
from road import Road


pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption('NFS_lite')
background_color = (0, 0, 0)

my_car_sound = pygame.mixer.Sound('sounds/engine.wav')
my_car_sound.play(-1)

road_group = pygame.sprite.Group()
spawn_road_time = pygame.USEREVENT
pygame.time.set_timer(spawn_road_time, 1000)

def get_car_image(filename, size, angle):
    image = pygame.image.load(filename)
    image = pygame.transform.scale(image, size)
    image = pygame.transform.rotate(image, angle)
    return image


my_car_image = get_car_image('images/mercedes.png', (100, 70), -90)
road_image = pygame.image.load('images/road.png')
road_image = pygame.transform.scale(road_image, (500, 800))

road = Road(road_image, (250, 400))
road_group.add(road)
road = Road(road_image, (250, 0))
road_group.add(road)


def spawn_road():
    road = Road(road_image, (250, -600))
    road_group.add(road)

def draw_all():
    road_group.update()
    road_group.draw(screen)
    my_car.draw(screen)


my_car = MyCar((300, 600), my_car_image)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == spawn_road_time:
            spawn_road()

    screen.fill(background_color)
    draw_all()
    pygame.display.flip()
    clock.tick(60)
