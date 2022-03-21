import pygame
import sys
import ball
import paddle
import collision
import score


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

WIDTH = 900
HEIGHT = 500
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (0xFF, 0xFF, 0xFF)
COLOR_GREEN = (0x39, 0xFF, 0x14)


# Collecting our screen
surface = pygame.display.set_mode((WIDTH, HEIGHT))

# Customizing our screen
pygame.display.set_caption("Pong Game")

def background():
    # Background color
    surface.fill(COLOR_BLACK)
    # Middle line
    pygame.draw.line(surface, COLOR_GREEN, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 3)
    pygame.draw.circle(surface, COLOR_GREEN, (WIDTH//2, HEIGHT//2), 20, width=20)
    pygame.draw.circle(surface, COLOR_GREEN, (0, HEIGHT//2), 200, width=3)
    pygame.draw.circle(surface, COLOR_GREEN, (WIDTH, HEIGHT // 2), 200, width=3)

def restart():
    background()
    right_score.restart()
    left_score.restart()
    ball.restart()
    left_paddle.restart()
    right_paddle.restart()

background()


# Objects:
ball = ball.Ball(surface, COLOR_WHITE, WIDTH//2, HEIGHT//2, 20)
left_paddle = paddle.Paddle(surface, COLOR_GREEN, 10, HEIGHT//2-50, 20, 100)
right_paddle = paddle.Paddle(surface, COLOR_GREEN, WIDTH - 20 - 10, HEIGHT//2-50, 20, 100)
collision = collision.Collision()
left_score = score.Score(surface, '0', WIDTH//4, 15)
right_score = score.Score(surface, '0', WIDTH - WIDTH//4, 15)

# Variables:
playing = False

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                ball.start_moving()
                playing = True

            if event.key == pygame.K_w:
                left_paddle.state = 'up'

            if event.key == pygame.K_s:
                left_paddle.state = 'down'

            if event.key == pygame.K_UP:
                right_paddle.state = 'up'

            if event.key == pygame.K_DOWN:
                right_paddle.state = 'down'

            if event.key == pygame.K_r:
                restart()
                playing = False


        if event.type == pygame.KEYUP:
            left_paddle.state = 'stopped'
            right_paddle.state = 'stopped'

    if playing:
        background()

        # ball
        ball.move()
        ball.show()

        # left paddle
        left_paddle.move()
        left_paddle.show()

        # right paddle
        right_paddle.move()
        right_paddle.show()

        # checking for goals
        if collision.check_goal(ball) == 1:
            background()
            left_score.increase()
            ball.restart_center()
            left_paddle.restart()
            right_paddle.restart()
            playing = False
        if collision.check_goal(ball) == 2:
            background()
            right_score.increase()
            ball.restart_center()
            left_paddle.restart()
            right_paddle.restart()
            playing = False

        # checking ball-paddles collisions
        if collision.collision_ball_paddle1(ball, left_paddle) or collision.collision_ball_paddle2(ball, right_paddle):
            ball.paddle_collision()

        # checking ball-walls
        if collision.collision_ball_walls(ball):
            ball.wall_collision()



    left_score.show()
    right_score.show()
    pygame.display.update()
    clock.tick(30)

