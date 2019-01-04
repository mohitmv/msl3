import unittest
import msl

class MslTest(unittest.TestCase):
  def test_basic(self):
    self.assertEqual(msl.id_function(11), 11);
    self.assertEqual(
      msl.left_fold(lambda x, y: x+y*10, [1,2,3,2], 10000),
      10000+1*10+2*10+3*10+2*10
    );


