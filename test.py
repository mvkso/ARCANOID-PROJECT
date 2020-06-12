import unittest
from main import Game
from unittest import main
import ball
import brick
import button
import paddle

class TestArcanoid(unittest.TestCase):
    def setUp(self):
        self.gra=Game()

    def test_collision(self):
        self.assertRaises(Exception,self.gra.collision,ball,"test")
        self.assertRaises(Exception,self.gra.collision,"ball",24)
        self.assertRaises(Exception,self.gra.collision,2,1)

    def test_isOver(self):
        self.assertRaises(Exception,self.gra.isOver,"test",1)
        self.assertRaises(Exception,self.gra.isOver,251,button)
        self.assertRaises(Exception,self.gra.isOver,ball,paddle)
        self.assertRaises(Exception,self.gra.isOver,[("tak"),("nie")],10.124)


    def test_nextlvlbutton(self):
        self.assertRaises(Exception, self.gra.nextlevelbutton, "przemyslaw")
        self.assertRaises(Exception, self.gra.nextlevelbutton, ["janusz","warcaba","politechnika"])
        self.assertRaises(Exception, self.gra.nextlevelbutton, ball)
        self.assertRaises(Exception, self.gra.nextlevelbutton, brick)


    def test_lvlcreator(self):
        self.assertEqual(self.gra.lvl_creator(10,1,5,-4,6),0)
        self.assertRaises(Exception, self.gra.lvl_creator,2,14,3,4,"sowa")
        self.assertRaises(Exception, self.gra.lvl_creator,12,4,"adam",412,"sarna")
        self.assertRaises(Exception, self.gra.lvl_creator,[(150+34),("tak")],paddle,brick,ball,11.4)





if __name__ == '__main__':
    unittest.main()
