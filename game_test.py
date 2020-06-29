import random
import unittest

import main
import ball
import brick
import button


class GameTest(unittest.TestCase):
    def setUp(self):
        self.gra = main.Game()

    def test_kolizja_zachodzi(self):
        ball_x = 200
        ball_y = 120
        brick_x = 205
        brick_y = 120
        brick_test = brick.Brick(self.gra, brick_x, brick_y)
        ball_test = ball.Ball(self.gra, ball_x, ball_y)
        X_move = ball_test.moveX
        Y_move = ball_test.moveY
        self.gra.collision(ball_test, brick_test)
        self.assertNotEqual(ball_test.moveY, -1 * Y_move)
        self.assertNotEqual(ball_test.moveX, -1 * X_move)

    def test_kolizja_nie_zachodzi(self):
        ball_x = 500
        ball_y = 500
        brick_x = 300
        brick_y = 300
        brick_test = brick.Brick(self.gra, brick_x, brick_y)
        ball_test = ball.Ball(self.gra, ball_x, ball_y)
        X_move = ball_test.moveX
        Y_move = ball_test.moveY
        self.gra.collision(ball_test, brick_test)
        self.assertEqual(ball_test.moveY, Y_move)
        self.assertEqual(ball_test.moveX, X_move)

    def test_funkcji_wait(self):
        """
        Funkcja wait na czas wykonania sie petli wstrzymuje ruch pilki. Po tym czasie ustawia predkosc jej poruszania na podana wartosc.
        Test_wait_dynamic sprawdza czy po przejsciu petli, funkcja wait, ustawia odpowiednie wartosci dla pilki.
        """
        self.gra.ball = ball.Ball(self.gra, 0, 0)
        x1 = random.randint(0, 5)
        y1 = random.randint(0, 5)
        for self.gra.i in range(101):
            self.gra.wait(x1, y1)
        self.assertEqual(x1, self.gra.ball.moveX)
        self.assertEqual(y1, self.gra.ball.moveY)

    def test_isOver_zachodzi(self):
        """
        Test dla funkcji isOver sprawdzajacej czy kursor myszki znajduje sie nad przyciskiem.
        """
        button_test = button.Button(0, 0, 400, 100, True)
        mouse_position_test = (200, 50)
        wynik = self.gra.isOver(button_test, mouse_position_test)
        self.assertTrue(wynik)

    def test_isOver_nie_zachodzi(self):
        button_test = button.Button(0, 0, 400, 100, True)
        mouse_position_test = (500, 500)
        wynik = self.gra.isOver(button_test, mouse_position_test)
        self.assertFalse(wynik)


if __name__ == '__main__':
    unittest.main()
