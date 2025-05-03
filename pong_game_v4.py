import pygame  # imports pygame used terminal pip to install
import sys
class Settings:
    def game_settings():
        pygame.init()
        WIDTH, HEIGHT = 1000, 600
        window = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pong Game, LBoogie Way")

        WHITE = (255, 255, 255)  # colors using rgb
        PINK = (255, 192, 203)
        BLACK = (0, 0, 0)
        clock = pygame.time.Clock()
        run = True

        while run:
            clock.tick(60)  # 60 frames per second
            window.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

class Draw(Settings):
    def __init__(self, draw_objects):
        super().__init__() #allows us to access settings 
        # draw everything
        pygame.draw.circle(self.window, self.WHITE, (int(self.ball_x), int(self.ball_y)), self.radius)  # draw ball
        pygame.draw.rect(self.window, self.PINK, (self.left_paddle_x, self.left_paddle_y, self.paddle_width, self.paddle_height))
        pygame.draw.rect(self.window, self.PINK, (self.right_paddle_x, self.right_paddle_y, self.paddle_width, self.paddle_height))

        pygame.display.update()

class Ball(Settings):
    def __init__(self):
        super().__init__() #allows us to access settings
        self.radius = 15
        self.ball_x, self.ball_y = self.WIDTH // 2, self.HEIGHT // 2
        self.ball_vel_x, self.ball_vel_y = 2, 2
         # move ball
        self.ball_x += self.ball_vel_x
        self.ball_y += self.ball_vel_y

        # bounce off top/bottom walls
        if self.ball_y - self.radius <= 0 or self.ball_y + self.radius >= self.HEIGHT:
            self.ball_vel_y *= -1

        # reset ball if it goes off screen (left or right)
        if self.ball_x - self.radius <= 0 or self.ball_x + self.radius >= self.WIDTH:
            self.ball_x, self.ball_y = self.WIDTH // 2, self.HEIGHT // 2
            self.ball_vel_x *= -1
            self.ball_vel_y *= -1
# pass is for an empty class or logic

class Paddle(Settings):
    def __init__(self):
        super().__init__() # allows us to access settings
        self.paddle_width, self.paddle_height = 20, 120  # paddle measurements
        self.left_paddle_y = self.HEIGHT // 2 - self.paddle_height // 2
        self.right_paddle_y = self.HEIGHT // 2 - self.paddle_height // 2
        self.left_paddle_x = 100
        self.right_paddle_x = self.WIDTH - 100

        self.left_paddle_vel = 0
        self.right_paddle_vel = 0
    
        keys = pygame.key.get_pressed()
        self.left_paddle_vel = -5 if keys[pygame.K_w] else 5 if keys[pygame.K_s] else 0
        self.right_paddle_vel = -5 if keys[pygame.K_UP] else 5 if keys[pygame.K_DOWN] else 0

        # update paddle positions
        self.left_paddle_y += self.left_paddle_vel
        self.right_paddle_y += self.right_paddle_vel

        # keep paddles on screen
        self.left_paddle_y = max(0, min(self.HEIGHT - self.paddle_height, self.left_paddle_y))
        self.right_paddle_y = max(0, min(self.HEIGHT - self.paddle_height, self.right_paddle_y))

class PaddleCollision(Ball, Paddle):
    def __init__(self):
        super().__init__()    # hit tab for autocomplete
        if self.left_paddle_x <= self.ball_x - self.radius <= self.left_paddle_x + self.paddle_width:
            if self.left_paddle_y <= self.ball_y <= self.left_paddle_y + self.paddle_height:
                self.ball_vel_x *= -1
        if self.right_paddle_x <= self.ball_x + self.radius <= self.right_paddle_x + self.paddle_width:
            if self.right_paddle_y <= self.ball_y <= self.right_paddle_y + self.paddle_height:
                self.ball_vel_x *= -1

# OOP menu
class Menu:
    def __init__(self):
        self.show_menu()

    def show_menu():
        print("--- Pong Main Menu ---")
        print("1. Play Game")
        print("2. Exit Game")
        print("3. Restart Game")

        try:
            choice = int(input("Please enter your choice: "))
            if choice == 1:
                main_game()
            elif choice == 2:
                print("Goodbye!")
                sys.exit()
            elif choice == 3:
                print("Restarting Game...")
                main_game()
            else:
                print("Invalid choice")
        except ValueError:
                print("Please enter a valid number")
    
def main_game():
    main_menu = Menu
    main_menu.show_menu()












 # pygame.init()
    # WIDTH, HEIGHT = 1000, 600
    # window = pygame.display.set_mode((WIDTH, HEIGHT))
    # pygame.display.set_caption("Pong Game, LBoogie Way")

    # WHITE = (255, 255, 255)  # colors using rgb
    # PINK = (255, 192, 203)
    # BLACK = (0, 0, 0)

    #radius = 15  # ball measurements
    # ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    # ball_vel_x, ball_vel_y = 2, 2  # ball speed so ball is visible

    # paddle_width, paddle_height = 20, 120  # paddle measurements
    # left_paddle_y = HEIGHT // 2 - paddle_height // 2
    # right_paddle_y = HEIGHT // 2 - paddle_height // 2
    # left_paddle_x = 100
    # right_paddle_x = WIDTH - 100

    # left_paddle_vel = 0
    # right_paddle_vel = 0

    # clock = pygame.time.Clock()
    # run = True

    # while run:
    #     clock.tick(60)  # 60 frames per second
    #     window.fill(BLACK)

    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False

        # check which keys are pressed
        # keys = pygame.key.get_pressed()
        # left_paddle_vel = -5 if keys[pygame.K_w] else 5 if keys[pygame.K_s] else 0
        # right_paddle_vel = -5 if keys[pygame.K_UP] else 5 if keys[pygame.K_DOWN] else 0

        # # update paddle positions
        # left_paddle_y += left_paddle_vel
        # right_paddle_y += right_paddle_vel

        # # keep paddles on screen
        # left_paddle_y = max(0, min(HEIGHT - paddle_height, left_paddle_y))
        # right_paddle_y = max(0, min(HEIGHT - paddle_height, right_paddle_y))

        # # move ball
        # ball_x += ball_vel_x
        # ball_y += ball_vel_y

        # # bounce off top/bottom walls
        # if ball_y - radius <= 0 or ball_y + radius >= HEIGHT:
        #     ball_vel_y *= -1

        # # reset ball if it goes off screen (left or right)
        # if ball_x - radius <= 0 or ball_x + radius >= WIDTH:
        #     ball_x, ball_y = WIDTH // 2, HEIGHT // 2
        #     ball_vel_x *= -1
        #     ball_vel_y *= -1

        # Paddle collision 
        # if left_paddle_x <= ball_x - radius <= left_paddle_x + paddle_width:
        #     if left_paddle_y <= ball_y <= left_paddle_y + paddle_height:
        #         ball_vel_x *= -1
        # if right_paddle_x <= ball_x + radius <= right_paddle_x + paddle_width:
        #     if right_paddle_y <= ball_y <= right_paddle_y + paddle_height:
        #         ball_vel_x *= -1

    #     # draw everything
    #     pygame.draw.circle(window, WHITE, (int(ball_x), int(ball_y)), radius)  # draw ball
    #     pygame.draw.rect(window, PINK, (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    #     pygame.draw.rect(window, PINK, (right_paddle_x, right_paddle_y, paddle_width, paddle_height))

    #     pygame.display.update()

    # pygame.quit()
