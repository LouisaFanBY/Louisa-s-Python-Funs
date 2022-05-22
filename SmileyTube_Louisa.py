import pygame
pygame.init()
screen = pygame.display.set_mode([800,600])
keep_going = True
pic = pygame.image.load("CrazySmile.bmp")
# pic2 = pygame.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0,0,0)
timer = pygame.time.Clock()
speedx = 50
speedy = 50

# create a list of pics and locations
pics = list()
# print("pics: ", pics)
pics.append(pic)
# print("pics: ", pics)

locations = list()
# print("locations: ", locations)
locations.append([0,0])
# print("locations: ", locations)

# start
while keep_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
            
    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy

    screen.fill(BLACK)

    # create a new smile, and add its new location
    newPic = pygame.image.load("CrazySmile.bmp")
    pics.append(newPic)

    newLocation = [picx, picy]
    locations.append([picx, picy])

    # print("pics: ", pics)
    # print("locations: ", locations)

    length = len(pics)

    for l in range(length):
        currentPic = pics[l]
        print('currentPic: ', currentPic)
        currentLocation = locations[l]
        print('currentLocation: ', currentLocation)

        screen.blit(currentPic, currentLocation)

    pygame.display.update()
    timer.tick(60)

pygame.quit()