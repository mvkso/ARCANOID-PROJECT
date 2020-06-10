import unittest
from main import Game
import ball
import brick
import button
import paddle

class ArcanoidTest(unittest.TestCase):
    def setUp(self):
        self.gra=Game()

    def collision_test(self):
        self.assertRaises(Exception,self.gra.collision,ball,brick)
        self.assertRaises(Exception,self.gra.collision,ball,"test")
        self.assertRaises(Exception,self.gra.collision,5,1)

    def isOver_test(self):
        self.assertRaises(Exception,self.gra.isOver,button,(1,2))
        self.assertRaises(Exception,self.gra.isOver,"test","parowóz")
        self.assertRaises(Exception,self.gra.isOver,2,1)

    def wait_test(self):
        self.assertRaises(Exception, self.gra.wait, button, (1, 2))
        self.assertRaises(Exception, self.gra.wait, "test", "parowóz")
        self.assertRaises(Exception, self.gra.wait, 2, 1)

    def nextlvlbutton_test(self):
        self.assertRaises(Exception, self.gra.nextlevelbutton, button)
        self.assertRaises(Exception, self.gra.nextlevelbutton, 4)
        self.assertRaises(Exception, self.gra.nextlevelbutton, "test")

    def lvlcreator_test(self):
        self.assertRaises(Exception, self.gra.lvl_creator,1,2,3,4,5)
        self.assertRaises(Exception, self.gra.lvl_creator,1,button,3,4,"sowa")
        self.assertRaises(Exception, self.gra.lvl_creator,2,14,3,4,"sowa")



if __name__ == '__main__':
    unittest.main()
