# importing modules
import pygame
import random
pygame.init()

display_width = 1150
display_height = 750
gameDisplay = pygame.display.set_mode((int(display_width), int(display_height)))
pygame.display.set_caption("Slither!!!")
icon_img = pygame.image.load("snake_icon.png")
pygame.display.set_icon(icon_img)

# variables for holding clock
clock = pygame.time.Clock()

# variable for frames per second
FPS = 20

# function for apple
apple_img = pygame.image.load("apple.png")

def apple(randomAppleX, randomAppleY):
    gameDisplay.blit(apple_img, [randomAppleX, randomAppleY])

# a function for pausing the game
def pause():
    paused = False
    while not paused:
        message_to_center_of_screen("PAUSED", blue, 45, -35)
        message_to_center_of_screen("PRESS C TO CONTINUE AND Q TO QUIT", black, 25, 0)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = True
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

# a function for text object
# function for displaying message to screen
def text_object(msg, color, size):
    font = pygame.font.SysFont(None, size)
    textSurface = font.render(msg, True, color)
    return textSurface, textSurface.get_rect()

def message_to_center_of_screen(msg, color, size, y_displace):
    textSurface, textRect = text_object(msg, color, size)
    textRect.center = int(display_width/2), int(display_height/2) + y_displace
    gameDisplay.blit(textSurface, textRect)

def message_to_screen(msg, color, size, X_position = 0, Y_position = 0):
    gameDisplay.fill(white)
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [X_position, Y_position])
    pygame.display.update()

# function for controlling snake
snake_img = pygame.image.load("snake_head.png")
def snake(snakeList, blockSize, direction = "up"):
    if direction == "up":
        head_img = pygame.transform.rotate(snake_img, 0)
        gameDisplay.blit(head_img, [snakeList[-1][0], snakeList[-1][1]])
    if direction == "right":
        head_img = pygame.transform.rotate(snake_img, 270)
        gameDisplay.blit(head_img, [snakeList[-1][0], snakeList[-1][1]])
    if direction == "down":
        head_img = pygame.transform.rotate(snake_img, 180)
        gameDisplay.blit(head_img, [snakeList[-1][0], snakeList[-1][1]])
    if direction == "left":
        head_img = pygame.transform.rotate(snake_img, 90)
        gameDisplay.blit(head_img, [snakeList[-1][0], snakeList[-1][1]])
    for XnY in snakeList[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

# colors
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
light_green = (124, 250, 0)
brown = (150, 75, 0)
maroon = (128, 0, 0)

block_size = 20

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = int(display_width/2)
    lead_y = int(display_height/2)

    # variable for holding score
    score = 0

    # variables for holding apple co-ordinates
    random_apple_x = int(round(random.randrange(2 * block_size, display_width - 2 * block_size) / 20) * 20)
    random_apple_y = int(round(random.randrange(2 * block_size, display_height - 2 * block_size) / 20) * 20)

    # list for controlling snakes and a variable for length
    snakeLength = 3
    snake_list = []
    snake_head = []

    lead_x_change = 0
    lead_y_change = -block_size
    gameDisplay.fill(white)
    pygame.display.update()
    dir = "up"
    play = True
    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            message_to_center_of_screen("GAME OVER", red, 45, -35)
            message_to_center_of_screen("PRESS C TO CONTINUE AND Q TO QUIT", blue, 35, 70)
            message_to_center_of_screen("YOUR SCORE: "+str(score), green, 35, 0)
            pygame.display.update()
            game_over_sound = pygame.mixer.Sound("game_over.wav")
            while play:
                pygame.mixer.Sound.play(game_over_sound)
                play = False
            pygame.mixer.Sound.play(game_over_sound)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        gameOver = False
                        gameLoop()
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    lead_x_change = block_size
                    lead_y_change = 0
                    dir = "right"
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    dir = "left"
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    lead_x_change = 0
                    lead_y_change = -block_size
                    dir = "up"
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    lead_x_change = 0
                    lead_y_change = block_size
                    dir = "down"
                if event.key == pygame.K_p:
                    pause()
        message_to_screen("YOUR SCORE: " + str(score), black, 20)
        lead_x += lead_x_change
        lead_y += lead_y_change
        snake_head.append(lead_x)
        snake_head.append(lead_y)
        snake_list.append(snake_head)
        if len(snake_list)>snakeLength:
            del snake_list[0]
        snake(snake_list, block_size, dir)
        snake_head = []
        apple(random_apple_x, random_apple_y)
        if random_apple_x - block_size < lead_x < random_apple_x + 40 and lead_y >  random_apple_y - block_size and lead_y< random_apple_y +40:
            random_apple_x = int(round(random.randrange(0, display_width - block_size) / block_size) * block_size)
            random_apple_y = int(round(random.randrange(0, display_height - block_size) / block_size) * block_size)
            score += 1
            snakeLength += 1
            print("Yum Yum Yum")
            eating_apple_sound = pygame.mixer.Sound("eating_apple.wav")
            pygame.mixer.Sound.play(eating_apple_sound)
        if not((0 <= lead_x <= display_width) and (0 <= lead_y <= display_height)):
            gameOver = True
        if [lead_x, lead_y] in snake_list[:-1]:
            gameOver = True
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

# functions for creating buttons


def button_object(button_text, text_color, size):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(button_text, True, text_color)
    return screen_text, screen_text.get_rect()

def button(button_text, text_color, color, pos_x, pos_y, size):
    pygame.draw.rect(gameDisplay, color, [pos_x, pos_y, 100, 60])
    screen_text, screen_rect = button_object(button_text, text_color, size)
    screen_rect.center = int(pos_x+50), int(pos_y + 30)
    gameDisplay.blit(screen_text, screen_rect)
    pygame.display.update()

def game_intro():
    gameDisplay.fill(white)
    message_to_center_of_screen("WELCOME TO SLITHER!", blue, 45, -180)
    message_to_center_of_screen("DO NOT CROSS THE EDGES OR RUN ONTO YOURSELF!!", black, 25, -130)
    message_to_center_of_screen("USE ARROW KEYS FOR CHANGING DIRECTIONS", black, 25, -100)
    message_to_center_of_screen("THE OBJECTIVE OF THE GAME TO EAT AS MANY APPLES AS YOU CAN", black, 25, -70)
    message_to_center_of_screen("PRESS P TO PAUSE THE GAME WHILE PLAYING, C TO CONTINUE AND Q TO QUIT", black, 25, -40)
    message_to_center_of_screen("PRESS C TO PLAY NOW AND Q TO QUIT", black, 25, 70)
    button("PLAY!!", black, green, 400, 550, 35)
    button("QUIT!!", black, red, 650, 550, 35)

    intro_sound = pygame.mixer.Sound("intro_sound.wav")
    pygame.mixer.Sound.play(intro_sound)
    pygame.display.update()
    gameIntro = True
    while gameIntro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIntro = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    gameLoop()
                if event.key  == pygame.K_q:
                    gameIntro = False
                    pygame.quit()
                    quit()
            button_click = pygame.mixer.Sound("button_click.wav")
            cur = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if 400<= cur[0]<= 400+100 and 550<=cur[1]<=550+60:
                button("PLAY!!", black, light_green, 400, 550, 35)
                pygame.mixer.Sound.play(button_click)
            else:
                button("PLAY!!", black, green, 400, 550, 35)
            if 650<= cur[0]<= 750 and 550<=cur[1]<= 610:
                pygame.mixer.Sound.play(button_click)
                button("QUIT!!", black, maroon, 650, 550, 35)
            else:
                button("QUIT!!", black, red, 650, 550, 35)
            if 400 <= cur[0] <= 400 + 100 and 550 <= cur[1] <= 550 + 60 and click[0] == 1:
                gameIntro = False
                gameLoop()
            if 650 <= cur[0] <= 750 and 550 <= cur[1] <= 610 and click[0] == 1:
                gameIntro = False
                pygame.quit()
                quit()
        pygame.display.update()
        clock.tick(int(FPS/2))
game_intro()

