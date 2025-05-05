# Pong game OOP solution
import pygame  # imports pygame used terminal pip to install
import sys


class Settings:
    # constructor parameterization with default arguments
    def __init__(
        self, WIDTH=1000, HEIGHT=600
    ):  # Default parameter values in the constructor
        self.colors = {
            # colors using rgb
            "WHITE": (255, 255, 255),
            "PINK": (255, 192, 203),
            "BLACK": (0, 0, 0),
        }
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.caption = pygame.display.set_caption("Pong Game, LBoogie Way")
        self.clock = pygame.time.Clock()
        self.window_color = self.colors["BLACK"]


# Inheritance should model “is-a” relationships. Since Ball and Paddle aren't Settings we won't use inheritance

# Use Composition
# Make an instance of settings in Ball, Paddle, Setting class. This is called Composition
class Ball:
    def __init__(
        self,
        settings,
        radius=15,
    ):
        self.radius = radius
        self.ball_x, self.ball_y = settings.WIDTH // 2, settings.HEIGHT // 2
        self.ball_vel_x, self.ball_vel_y = 2, 2

    def ball_movement(self, settings):
        # move ball
        self.ball_x += self.ball_vel_x
        self.ball_y += self.ball_vel_y

        # bounce off top/bottom walls
        if (
            self.ball_y - self.radius <= 0
            or self.ball_y + self.radius >= settings.HEIGHT
        ):
            self.ball_vel_y *= -1

        # reset ball if it goes off screen (left or right)
        if (
            self.ball_x - self.radius <= 0
            or self.ball_x + self.radius >= settings.WIDTH
        ):
            self.ball_x, self.ball_y = settings.WIDTH // 2, settings.HEIGHT // 2
            self.ball_vel_x *= -1
            self.ball_vel_y *= -1


class Paddle:
    # Composition: settings is passed as a parameter in the Paddle class constructor 
    # ensuring that when Paddle is instantiated in the game loop it has access to settings
    def __init__(self, settings):
        self.paddle_width, self.paddle_height = 20, 120  # paddle measurements
        self.left_paddle_y = settings.HEIGHT // 2 - self.paddle_height // 2
        self.right_paddle_y = settings.HEIGHT // 2 - self.paddle_height // 2
        self.left_paddle_x = 100
        self.right_paddle_x = settings.WIDTH - 10
        self.left_paddle_vel = 0
        self.right_paddle_vel = 0

    # Composition
    def paddle_movement(self, settings):
        # update paddle positions
        self.left_paddle_y += self.left_paddle_vel
        self.right_paddle_y += self.right_paddle_vel

        # keep paddles on screen
        self.left_paddle_y = max(
            0, min(settings.HEIGHT - self.paddle_height, self.left_paddle_y)
        )
        self.right_paddle_y = max(
            0, min(settings.HEIGHT - self.paddle_height, self.right_paddle_y)
        )

    def key_pressed(self):
        # check which keys are pressed
        keys = pygame.key.get_pressed()
        self.left_paddle_vel = -5 if keys[pygame.K_w] else 5 if keys[pygame.K_s] else 0
        self.right_paddle_vel = (
            -5 if keys[pygame.K_UP] else 5 if keys[pygame.K_DOWN] else 0
        )


class PaddleCollision:
    def __init__(self, settings, ball, paddle):
        pass

    def ball_and_paddle_collision(self, settings, ball, paddle):
        if (
            paddle.left_paddle_x
            <= ball.ball_x - ball.radius
            <= paddle.left_paddle_x + paddle.paddle_width
        ):
            if (
                paddle.left_paddle_y
                <= ball.ball_y
                <= paddle.left_paddle_y + paddle.paddle_height
            ):
                ball.ball_vel_x *= -1
        if (
            paddle.right_paddle_x
            <= ball.ball_x + ball.radius
            <= paddle.right_paddle_x + paddle.paddle_width
        ):
            if (
                paddle.right_paddle_y
                <= ball.ball_y
                <= paddle.right_paddle_y + paddle.paddle_height
            ):
                ball.ball_vel_x *= -1


class Draw:
    # Composition: settings is passed as a parameter in the Draw class constructor 
    # along with instances of ball and paddle
    def __init__(self, settings, ball, paddle):
        self.settings = settings
        self.ball = ball
        self.paddle = paddle

    # Composition
    def draw_all(self, settings, ball, paddle):
        # draw everything
        pygame.draw.circle(
            settings.window,
            settings.colors["WHITE"],
            (int(ball.ball_x), int(ball.ball_y)),
            ball.radius,
        )  # draw ball
        pygame.draw.rect(
            settings.window,
            settings.colors["PINK"],
            (
                paddle.left_paddle_x,
                paddle.left_paddle_y,
                paddle.paddle_width,
                paddle.paddle_height,
            ),
        )
        pygame.draw.rect(
            settings.window,
            settings.colors["PINK"],
            (
                paddle.right_paddle_x,
                paddle.right_paddle_y,
                paddle.paddle_width,
                paddle.paddle_height,
            ),
        )


# OOP menu
class Menu:
    def __init__(self):
        self.menu_choices = {1: "Play Game", 2: "Exit Game", 3: "Restart Game"}

    def show_menu(self):
        print("--- Pong Main Menu ---")
        for key, choices in self.menu_choices.items():
            print(f"{key}. {choices}")

    def game_start(self):
        while True:
            choice = int(input("Please enter your choice: "))
            try:
                if choice == 1:
                    # Instantiate Settings, Ball, Paddle, and PaddleCollison in the main game loop
                    # Composition: after instantiating Settings pass the instance of settings as an argument into the Ball, Paddle, PaddleCollision, and Draw classes
                    # This ensures Ball, Paddle, PaddleCollision, and Draw classes have access to Settings
                    pygame.init()
                    game_defaults = Settings()
                    pong_ball = Ball(game_defaults)
                    pong_paddles = Paddle(game_defaults)
                    pong_gameplay = PaddleCollision(
                        game_defaults, pong_ball, pong_paddles
                    )
                    draw_game = Draw(game_defaults, pong_ball, pong_paddles)
                    run = True
                    while run:
                        # Handles the user closing the game 
                        # Use a for loop to loop through pygame's events and the .get() method to get all of the events
                        # Add a conditional to get the .QUIT event
                        # if a user clicks x the window closes and run is now False
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                                        
                        game_defaults.clock.tick(60)  # 60 frames per second
                        game_defaults.window.fill(game_defaults.window_color)
                        pong_ball.ball_movement(game_defaults)
                        pong_paddles.paddle_movement(game_defaults)
                        pong_paddles.key_pressed()
                        pong_gameplay.ball_and_paddle_collision(game_defaults, pong_ball, pong_paddles)

                        # Draw everything
                        draw_game.draw_all(game_defaults, pong_ball, pong_paddles)
                        
                        pygame.display.update()
                elif choice == 2:
                    print("Goodbye!")
                    sys.exit()
                    break
                elif choice == 3:
                    print("Restarting Game...")
                    main_game()
                    break
                else:
                    print("Invalid choice")
            except ValueError:
                print("Please enter a valid number")


def main_game():
    game_menu = Menu()
    game_menu.show_menu()
    game_menu.game_start()


if __name__ == "__main__":
    main_game()
