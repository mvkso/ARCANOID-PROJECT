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
        ball_x = 210
        ball_y = 130
        brick_x = 205
        brick_y = 120
        brick_test = brick.Brick(self.gra, brick_x, brick_y)
        ball_test = ball.Ball(self.gra, ball_x, ball_y)
        X_move = ball_test.move_x
        Y_move = ball_test.move_y
        self.gra.collision(ball_test, brick_test)
        self.assertEqual(ball_test.move_y, -1 * Y_move)
        self.assertEqual(ball_test.move_x, -1 * X_move)

    def test_kolizja_nie_zachodzi(self):
        ball_x = 500
        ball_y = 500
        brick_x = 300
        brick_y = 300
        brick_test = brick.Brick(self.gra, brick_x, brick_y)
        ball_test = ball.Ball(self.gra, ball_x, ball_y)
        x_move = ball_test.move_x
        y_move = ball_test.move_y
        self.gra.collision(ball_test, brick_test)
        self.assertEqual(ball_test.move_y, y_move)
        self.assertEqual(ball_test.move_x, x_move)

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
        self.assertEqual(x1, self.gra.ball.move_x)
        self.assertEqual(y1, self.gra.ball.move_y)

    def test_is_over_zachodzi(self):
        """
        Test dla funkcji isOver sprawdzajacej czy kursor myszki znajduje sie nad przyciskiem.
        """
        button_test = button.Button(0, 0, 400, 100, True)
        mouse_position_test = (200, 50)
        wynik = self.gra.is_over(button_test, mouse_position_test)
        self.assertTrue(wynik)

    def test_is_over_nie_zachodzi(self):
        button_test = button.Button(0, 0, 400, 100, True)
        mouse_position_test = (500, 500)
        wynik = self.gra.is_over(button_test, mouse_position_test)
        self.assertFalse(wynik)


if __name__ == '__main__':
    unittest.main()
