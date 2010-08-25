import unittest
from character import Character

class TestCharacter(unittest.TestCase):
   def setUp(self):
      self.linder = Character()
      self.linder.setAbilities(str=13, con=12, dex=20, int=11, wis=14, cha=21)
      self.linder.setSkills(acrobatics=True, athletics=True, bluff=True, 
                       perception=True, stealth=True, streetwise=True,
                       thievery=True)
      self.linder.skill['diplomacy'].miscBonus = 2
      self.linder.skill['insight'].miscBonus = 2
      self.linder.setLvl(11)

   def test_skill(self):
      self.assertEqual(self.linder.skill['stealth'].value(), 15)
      self.assertEqual(self.linder.skill['athletics'].value(), 11)
      self.assertEqual(self.linder.skill['arcana'].value(), 5)
      self.assertEqual(self.linder.skill['athletics'].value(), 11)
      self.assertEqual(self.linder.skill['insight'].value(), 9)

if __name__ == '__main__':
    unittest.main()
