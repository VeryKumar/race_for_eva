import pygame
import time
pygame.init()

game_width= 800
game_height= 600

black = (0,0,0)
white = (255,255,255)
green = (161,185,81)
blue = (161,185,253)
brown = (62,26,1)

car_width = 32
gameDisplay = pygame.display.set_mode((game_width,game_height))

pygame.display.set_caption ('Chimera Ants: Racing edition')

clock = pygame.time.Clock()

shinjiImg = pygame.image.load('Hunchback Shinji Suit.gif')

def car (x,y):
    gameDisplay.blit(shinjiImg, (x,y))

    #What is .blit / what is blitting?#
    #Blittting is copying one set of pixels (an object) onto another (your surface)#
    #(x,y) is a tuple, or a collection that is ordered and unchangeable#

    #(shingjiImg,) is a parameter.#
    #A parameter is the part of the function that tells us
        #what argument#
        #a function can accept.#
def text_objects (text, font):
    textSurface = font.render (text, True, green)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((game_width/2), (display_height/2))

    gameDisplay.blit(TextSurf, TextRect)

    pygame.gameDisplay.update()

    time.sleep(2)

    game_loop()

def crash():
    message_display('Shinji Get in the Robot?')

def game_loop():

    x = (game_width * 0.45)
    y = (game_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change += -5
                elif event.key == pygame.K_RIGHT:
                    x_change += +5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change += +5
                if event.key == pygame.K_RIGHT:
                    x_change += -5

        x += x_change

        print(event)
        gameDisplay.fill(white)
        car(x,y)

        if x > game_width - car_width or x < 0:
            gameExit = True

        pygame.display.update()

        #this is to update the display. Could also use pygame.display.flip

        #pygame.display.update would update (whatever lies within a defined parameter)#
        #pygame.display.update will update everyting on the surface if there is no parameter#
        #pygame.display.flip will update everything on the surface#

        clock.tick(60)

        #This defines how many fps our game runs at#
game_loop()
pygame.quit()
quit()