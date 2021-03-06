import pygame
import sys
import ball
import paddle
import collision
import score
import portal


# Initialize pygame
pygame.init()
clock = pygame.time.Clock()

WIDTH = 900
HEIGHT = 500
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (0xFF, 0xFF, 0xFF)
COLOR_PURPLE = (0x5C, 0x00, 0x7A)


# Collecting our screen
surface = pygame.display.set_mode((WIDTH, HEIGHT + 100))


# Customizing our screen
pygame.display.set_caption("Pong Game")

# Images
center_bg = pygame.image.load("resources/images/center.png")
portal_image = pygame.transform.scale(pygame.image.load("resources/images/portal.png"), (100, 100))


def background():
    # Background color
    surface.fill(COLOR_BLACK)

    # Background center image
    surface.blit(pygame.transform.scale(center_bg, (200, 200)), (WIDTH // 2 - 100, HEIGHT // 2 - 100))
    pygame.draw.circle(surface, COLOR_BLACK, (WIDTH//2, HEIGHT//2), 150, width=50)

    # Middle line
    pygame.draw.line(surface, COLOR_PURPLE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 3)

    # Field marks
    pygame.draw.circle(surface, COLOR_PURPLE, (WIDTH // 2, HEIGHT // 2), 7, width=7)
    pygame.draw.circle(surface, COLOR_PURPLE, (0, HEIGHT // 2), 200, width=3)
    pygame.draw.circle(surface, COLOR_PURPLE, (WIDTH, HEIGHT // 2), 200, width=3)
    pygame.draw.line(surface, COLOR_PURPLE, (0, 0), (900, 0), width=5)
    pygame.draw.line(surface, COLOR_PURPLE, (0, 0), (0, 500), width=3)
    pygame.draw.line(surface, COLOR_PURPLE, (0, 500), (900, 500), width=5)
    pygame.draw.line(surface, COLOR_PURPLE, (900, 0), (900, 500), width=3)


def restart():
    background()
    right_score.restart()
    left_score.restart()
    ball.restart_center()
    left_paddle.restart()
    right_paddle.restart()
    portal1.restart()
    portal2.restart()

background()

# Objects:
ball = ball.Ball(surface, COLOR_WHITE, WIDTH//2, HEIGHT//2, 20)
left_paddle = paddle.Paddle(surface, COLOR_PURPLE, 10, HEIGHT//2-50, 20, 100)
right_paddle = paddle.Paddle(surface, COLOR_PURPLE, WIDTH - 20 - 10, HEIGHT//2-50, 20, 100)
collision = collision.Collision()
left_score = score.Score(surface, '0', WIDTH//4, HEIGHT + 15)
right_score = score.Score(surface, '0', WIDTH - WIDTH//4, HEIGHT + 15)
portal1 = portal.Portal(surface, portal_image, 680, 430)
portal2 = portal.Portal(surface, portal_image, 220, 70)


# Variables:
playing = False

# Timer:
time_delay = 1
timer_event = pygame.USEREVENT + 1


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                ball.restart_center()
                left_paddle.restart()
                right_paddle.restart()
                portal1.restart()
                portal2.restart()
                ball.start_moving()
                portal1.start_moving(5)
                portal2.start_moving(5)
                playing = True

            if event.key == pygame.K_w:
                left_paddle.state_v = 'up'

            if event.key == pygame.K_s:
                left_paddle.state_v = 'down'

            if event.key == pygame.K_d:
                left_paddle.state_h = 'forward'

            if event.key == pygame.K_a:
                left_paddle.state_h = 'back'

            if event.key == pygame.K_UP:
                right_paddle.state_v = 'up'

            if event.key == pygame.K_DOWN:
                right_paddle.state_v = 'down'

            if event.key == pygame.K_LEFT:
                right_paddle.state_h = 'forward'

            if event.key == pygame.K_RIGHT:
                right_paddle.state_h = 'back'

            if event.key == pygame.K_r:
                restart()
                playing = False

        if event.type == pygame.KEYUP:
            left_paddle.state_v = 'stopped'
            right_paddle.state_v = 'stopped'
            left_paddle.state_h = 'stopped'
            right_paddle.state_h = 'stopped'

    if playing:
        background()

        # portal 1
        portal1.move(1)
        portal1.show()

        # portal 2
        portal2.move(2)
        portal2.show()

        # ball
        ball.move()
        ball.show()

        # left paddle
        left_paddle.move_v()
        left_paddle.move_h(1)
        left_paddle.show()

        # right paddle
        right_paddle.move_v()
        right_paddle.move_h(2)
        right_paddle.show()

        # checking for goals
        if collision.check_goal(ball) == 1:
            background()
            left_score.increase()
            ball.restart_center()
            left_paddle.restart()
            right_paddle.restart()
            portal1.restart()
            portal2.restart()
            playing = False
        if collision.check_goal(ball) == 2:
            background()
            right_score.increase()
            ball.restart_center()
            left_paddle.restart()
            right_paddle.restart()
            portal1.restart()
            portal2.restart()
            playing = False

        # checking ball-portal 1 collision:
        if portal1.activated and collision.collision_ball_portal(ball, portal1):
            ball.portal_collision(portal2)
            portal2.activated = False

        # checking ball-portal 2 collision:
        if portal2.activated and collision.collision_ball_portal(ball, portal2):
            ball.portal_collision(portal1)
            portal1.activated = False

        # checking ball-paddles collisions
        if collision.collision_ball_paddle1(ball, left_paddle) or collision.collision_ball_paddle2(ball, right_paddle):
            ball.paddle_collision()
            portal1.activated = True
            portal2.activated = True

        # checking ball-walls
        if collision.collision_ball_walls(ball):
            ball.wall_collision()

        # checking holes limit:
        if collision.check_portal_limit(portal1):
            portal1.limit_collision()
        if collision.check_portal_limit(portal2):
            portal2.limit_collision()

    left_score.show()
    right_score.show()
    pygame.display.update()
    clock.tick(30)

