import pygame
import random
import os

pygame.mixer.init()
pygame.mixer.music.load('D:\Snake Game Items\Game_Welcome.mp3.mp3')
pygame.mixer.music.play(-1)

pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
DARK_PURPLE = (75, 0, 130)
DARK_BLUE = (0, 0, 139)
DARK_SKY_BLUE = (0, 139, 139)
GREEN = (0, 128, 0)
YELLOW = (255, 255, 0)

# Creating window
SCREEN_WIDTH = 1360
SCREEN_HEIGHT = 768
gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Background Image  
bgimg = pygame.image.load('D:\Snake Game Items\Game_Main_Image.jpg')
bgimg = pygame.transform.scale(bgimg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()


# Game Title
pygame.display.set_caption("Snake Game Made By:-Prince")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Monotype Corsiva', 85)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, head_color, body_color, snk_list, snake_size):
    for i, (x, y) in enumerate(snk_list):
        if i == len(snk_list) - 1:
            pygame.draw.circle(gameWindow, head_color, (x, y), snake_size)
        else:
            pygame.draw.circle(gameWindow, body_color, (x, y), snake_size)
            
def welcome():
    exit_game = False
    while not exit_game:
        # gameWindow.fill(DARK_PURPLE)
        img = pygame.image.load('D:\Snake Game Items\Game_Welcome_Image.jpg')
        img = pygame.transform.scale(bgimg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
        gameWindow.blit(img, (0,0))
        
        # Load and display the new welcome screen image
        welcome_img = pygame.image.load('D:\Snake Game Items\Game_Welcome_Image.jpg')  # Update the path
        welcome_img = pygame.transform.scale(welcome_img, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()  # Adjust size as needed
        gameWindow.blit(welcome_img, (0,0))  # Adjust position as needed
                
        text_screen("Welcome to Snake Game", DARK_BLUE, 480, 250)
        text_screen("Made By:-'Prince'", DARK_BLUE, 560, 320)
        text_screen("Press 'Space Key' To Play", DARK_BLUE, 450, 400)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    
                        pygame.mixer.music.load('D:\Snake Game Items\Ki-Jab-Main-Hadd-Se.mp3.mp3')
                        pygame.mixer.music.play(-1)
                        gameloop()

        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    # Check if hiscore file exists
    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        hiscore = f.read()

    food_x = random.randint(50, SCREEN_WIDTH - 50)
    food_y = random.randint(50, SCREEN_HEIGHT - 50)
    Score = 0
    init_velocity = 5
    snake_size = 15 # Adjust the size of the snake's circle
    fps = 60

    snake_head_color = RED  # Color of the snake's head
    snake_body_color = GREEN  # Color of the snake's body

    while not exit_game:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            # gameWindow.fill(DARK_BLUE)
            img = pygame.image.load('D:\Snake Game Items\Game_Over_Image.jpg')
            img = pygame.transform.scale(bgimg, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()
            gameWindow.blit(img, (0,0))
        
            # Load and display the new welcome screen image
            welcome_img = pygame.image.load('D:\Snake Game Items\Game_Over_Image.jpg')  # Update the path
            welcome_img = pygame.transform.scale(welcome_img, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert_alpha()  # Adjust size as needed
            gameWindow.blit(welcome_img, (0,0))  # Adjust position as needed
            text_screen("Game Over!", RED, 490, 210)
            text_screen("Score: " + str(Score), BLACK, 550, 270)
            text_screen("Highscore: " + str(hiscore), BLACK, 490, 330)
            text_screen("Press 'Enter Key' To Continue", RED, 310, 420)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('D:\Snake Game Items\Game_Welcome.mp3.mp3')
                        pygame.mixer.music.play(-1)
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                        
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                       
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                    
            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < snake_size and abs(snake_y - food_y) < snake_size:
                Score += 1
                food_x = random.randint(20, SCREEN_WIDTH - 20)
                food_y = random.randint(20, SCREEN_HEIGHT - 20)
                snk_length += 5
                
                # Snake Speed incresing after 10 food eating
                if Score < 10:
                    init_velocity*5
            else: Score > 10
            init_velocity == init_velocity
                
            if Score < 20:
               init_velocity*10
            else: Score > 20
            init_velocity == init_velocity*5
                   
            if Score < 30:
                init_velocity*15
            else: Score > 30
            init_velocity == init_velocity*10
                
            if Score < 40:
                 init_velocity*20
            else: Score > 40
            init_velocity == init_velocity*15

            if Score < 50:
                 init_velocity*25
            else: Score > 50
            init_velocity == init_velocity*20

            if Score < 60:
                 init_velocity*30
            else: Score > 60
            init_velocity == init_velocity*25

                        
            if Score < 70:
             init_velocity*35
            else: Score > 70
            init_velocity == init_velocity*30

            if Score < 80:
             init_velocity*40
            else: Score > 80
            init_velocity == init_velocity*35

            if Score < 90:
             init_velocity*45
            else: Score > 90
            init_velocity == init_velocity*40

            if Score < 100:
                 init_velocity*50
            else: Score > 100
            init_velocity == init_velocity*45
                
            if Score > int(hiscore):
                    hiscore = Score

            gameWindow.fill(BLACK)
            gameWindow.blit(bgimg, (0,0))
            text_screen("Score: " + str(Score) + "  Highscore: " + str(hiscore), RED, 5, 5)
            pygame.draw.circle(gameWindow, YELLOW, (food_x, food_y), snake_size)  # Draw food
            plot_snake(gameWindow, snake_head_color, snake_body_color, snk_list, snake_size)  # Draw snake

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('D:\Snake Game Items\Game_over.mp3.mp3')
                pygame.mixer.music.play(-1)

            if snake_x < 0 or snake_x > SCREEN_WIDTH or snake_y < 0 or snake_y > SCREEN_HEIGHT:
                game_over = True
                
                pygame.mixer.music.load('D:\Snake Game Items\Game_over.mp3.mp3')
                pygame.mixer.music.play(-1)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()