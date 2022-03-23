HEIGHT = 500
WIDTH = 900

class Collision:

    def collision_ball_paddle1(self, ball, left_paddle):
        if ball.position[1] + ball.radius >= left_paddle.position[1] and ball.position[1] - ball.radius <= left_paddle.position[1] + left_paddle.position[3]:
            if abs((ball.position[0] - ball.radius) - (left_paddle.position[0] + left_paddle.position[2])) <= 5:
                return True
        return False

    def collision_ball_paddle2(self, ball, right_paddle):
        if ball.position[1] + ball.radius >= right_paddle.position[1] and ball.position[1] - ball.radius <= right_paddle.position[1] + right_paddle.position[3]:
            if abs((ball.position[0] + ball.radius) - right_paddle.position[0]) <= 5:
                return True
        return False

    def collision_ball_walls(self, ball):
        # Top collision:
        if ball.position[1] - ball.radius <= 0:
            return True
        # Bottom collision
        if ball.position[1] + ball.radius >= HEIGHT:
            return True
        return False

    def collision_ball_portal(self, ball, portal):
        if abs(ball.position[1] - portal.portal_rect.centery) < 30 and abs(ball.position[0] - portal.portal_rect.centerx) < 30:
            return True
        return False

    def check_goal(self, ball):
        if ball.position[0] > WIDTH - 10:
            return 1 # goal of player 1
        elif ball.position[0] < 0 + 10:
            return 2 # goal of player 2
        return 0

    def check_portal_limit(self, portal):
        if portal.portal_rect.centerx > 700 or portal.portal_rect.centerx < 200:
            return True
        return False

