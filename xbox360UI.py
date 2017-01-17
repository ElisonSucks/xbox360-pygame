import pygame
pygame.init()
pygame.joystick.init()
count = pygame.joystick.get_count()

end = False
clock = pygame.time.Clock()

screenSize = [500,500]
screen = pygame.display.set_mode(screenSize)

background = pygame.Surface(screen.get_size())
background.fill((0,0,0))

font = pygame.font.SysFont('Consolas', 15)

buttonList = [0,0,0,0,0,0,0,0,0,0]
axesList = [0,0,0,0,0]
hatList = [(0,0)]
circleCoords = [250,250]
size = 10
color = [255,255,255]

def controllerCheck():
    global count
    if count == 0:
        print('Controller.py could not find a connected controller!')
        print('Please connect a controller...')
        while count == 0:
            pygame.joystick.init()
            count = pygame.joystick.get_count()
            pygame.joystick.quit()
        pygame.joystick.init()

    if count != 0:
        print('Controllers Connected : ' + str(count))

def controllerData():
    global count
    global circleCoords
    global size
    global color
    
    # -- Data --
    for i in range(count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()

        name = joystick.get_name()

        axes = joystick.get_numaxes()
        for i in range( axes ):
            axis = joystick.get_axis( i )
            axesList[i] = axis

        buttons = joystick.get_numbuttons()
        for i in range( buttons ):
            button = joystick.get_button( i )
            buttonList[i] = button

        hats = joystick.get_numhats()
        for i in range( hats ):
            hat = joystick.get_hat( i )
            hatList[i] = hat

    # -- Manipulate Data --
    
    if axesList[0] > .25:
        circleCoords[0] += 5
    elif axesList[0] < -.25:
        circleCoords[0] -= 5

    if axesList[1] > .25:
        circleCoords[1] += 5
    elif axesList[1] < -.25:
        circleCoords[1] -= 5

    if axesList[2] > .5:
        size += 2
    elif axesList[2] < -.5:
        if size <= 2:
            size = 2
        else:
            size -= 2

    if buttonList[0] == 1:
        color = (0,255,0)
    elif buttonList[1] == 1:
        color = [255,0,0]
    elif buttonList[2] == 1:
        color = [0,0,255]
    elif buttonList[3] == 1:
        color = [255,204,0]

    pygame.draw.circle(screen, color, (circleCoords), size, 1)
    
controllerCheck()

while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
            
    screen.blit(background, (0, 0))
    controllerData()

    pygame.display.update()
    clock.tick(32)

pygame.quit()
    
    
            
