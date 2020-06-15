import random
import pygame

import unittest
from pygame.math import Vector2

from main import Game
import ball
import brick
import button
import paddle
import colors


class TestArcanoid(unittest.TestCase):
    def setUp(self):
        self.gra = Game()

    def test_colors(self):
        self.assertEqual(colors.Colors.okno_zielone, (0, 255, 0))
        self.assertEqual(colors.Colors.okno_czerwone, (255, 0, 0))
        self.assertEqual(colors.Colors.okno_szare, (150, 150, 150))

    def test_collision(self):
        self.assertRaises(Exception, self.gra.collision, ball, "test")
        self.assertRaises(Exception, self.gra.collision, "ball", 24)
        self.assertRaises(Exception, self.gra.collision, 2, 1)

    def test_collision_dynamic(self):
        ballx = random.randint(100, 400)
        bally = random.randint(100, 400)
        brickx = random.randint(100, 400)
        bricky = random.randint(100, 400)
        brick_test = brick.Brick(self.gra, brickx, bricky)
        ball_test = ball.Ball(self.gra, ballx, bally)
        Xmove = ball_test.moveX
        Ymove = ball_test.moveY
        self.gra.collision(ball_test, brick_test)
        if ball_test.pos.x > (brick_test.pos.x - 5) and ball_test.pos.x < (brick_test.pos.x + 69) and (
                ball_test.pos.y > brick_test.pos.y - 10) and ball_test.pos.y < brick_test.pos.y + 74:
            self.assertEqual(ball_test.moveY, -1 * Ymove)
            self.assertEqual(ball_test.moveX, -1 * Xmove)
        else:
            self.assertEqual(ball_test.moveY, Ymove)
            self.assertEqual(ball_test.moveX, Xmove)

    def test_wait_dynamic(self):
        self.gra.ball=ball.Ball(self.gra,0,0)
        x1=random.randint(0,5)
        y1=random.randint(0,5)
        for self.gra.i in range(0, 101):
            self.gra.wait(x1,y1)
        self.assertEqual(x1,self.gra.ball.moveX)
        self.assertEqual(y1,self.gra.ball.moveY)

    def test_isOver(self):
        self.assertRaises(Exception, self.gra.isOver, "test", 1)
        self.assertRaises(Exception, self.gra.isOver, 251, button)
        self.assertRaises(Exception, self.gra.isOver, ball, paddle)
        self.assertRaises(Exception, self.gra.isOver, ["tak", "nie"], 10.124)

    def test_nextlvlbutton(self):
        self.assertRaises(Exception, self.gra.nextlevelbutton, "przemyslaw")
        self.assertRaises(Exception, self.gra.nextlevelbutton, ["janusz", "warcaba", "politechnika"])
        self.assertRaises(Exception, self.gra.nextlevelbutton, ball)
        self.assertRaises(Exception, self.gra.nextlevelbutton, brick)

    def test_lvlcreator(self):
        self.assertEqual(self.gra.level_creator(10, 1, 5, -4, 6), True)
        self.assertRaises(Exception, self.gra.level_creator, 2, 14, 3, 4, "sowa")
        self.assertRaises(Exception, self.gra.level_creator, 12, 4, "adam", 412, "sarna")
        self.assertRaises(Exception, self.gra.level_creator, [(150 + 34), "tak"], paddle, brick, ball, 11.4)


if __name__ == '__main__':
    unittest.main()
