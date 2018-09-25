import math #lets us use the math module
import unittest #unittest module lets us test small sections of code

def circleArea(radius): 
    return radius * radius * math.pi

def rectArea(base, height):
    return base * height * math.pi

def trapArea(base1, base2, height):
    return base1 * base2 * height * math.pi

def triArea(base,height):
    return base * height * math.pi
    
	
class MyTest(unittest.TestCase):#using testCase class from unittest module
    def testCircleArea(self):
        self.assertAlmostEqual(circleArea(5), 25*math.pi)
        self.assertAlmostEqual(circleArea(10), 100*math.pi)
        
    def testRectArea(self):
        self.assertAlmostEqual(rectArea(5,2), 10*math.pi)
        self.assertAlmostEqual(rectArea(7,1), 7*math.pi)
        
    def testTrapArea(self):
        self.assertAlmostEqual(trapArea(12,12,1), 144*math.pi)
        self.assertAlmostEqual(trapArea(3,3,1), 9*math.pi)
        
    def testTriArea(self):
        self.assertAlmostEqual(triArea(6,2), 12*math.pi)
        self.assertAlmostEqual(triArea(8,2), 16*math.pi)