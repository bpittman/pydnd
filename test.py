import unittest
from character import Character
from weapon import Weapon
from power import Power

class TestCharacter(unittest.TestCase):
   def setUp(self):
      import linder
      self.linder = linder.Linder()

   def test_skill(self):
      self.assertEqual(self.linder.skill['stealth'].value(), 15)
      self.assertEqual(self.linder.skill['athletics'].value(), 11)
      self.assertEqual(self.linder.skill['arcana'].value(), 5)
      self.assertEqual(self.linder.skill['athletics'].value(), 11)
      self.assertEqual(self.linder.skill['insight'].value(), 9)

   def test_ability_mod(self):
      self.assertEqual(self.linder.abilityMod['str'], 1)
      self.assertEqual(self.linder.abilityMod['con'], 1)
      self.assertEqual(self.linder.abilityMod['dex'], 5)
      self.assertEqual(self.linder.abilityMod['int'], 0)
      self.assertEqual(self.linder.abilityMod['wis'], 2)
      self.assertEqual(self.linder.abilityMod['cha'], 5)

class TestPowers(unittest.TestCase):
   def setUp(self):
      import linder
      self.linder = linder.Linder()

   def test_power_attack_bonus(self):
      self.linder.getPowerStats('slyFlourish',output=False)
      self.assertEqual(self.linder.powers['slyFlourish'].attackBonus, 17)
      self.assertEqual(self.linder.powers['slyFlourish'].totalDamage, '1d8+14')
      self.assertEqual(self.linder.powers['slyFlourish'].maxDamage, 22)
      self.assertEqual(self.linder.powers['slyFlourish'].maxPlusWeapon, '1d8+22')

   def test_encounter_availability(self):
      self.assertTrue('positioningStrike' in self.linder.getPowers())
      self.linder.powers['positioningStrike'].setUsed(True)
      self.assertFalse('positioningStrike' in self.linder.getPowers())
      self.linder.shortRest()
      self.assertTrue('positioningStrike' in self.linder.getPowers())

   def test_daily_availability(self):
      self.assertTrue('aerialAssault' in self.linder.getPowers())
      self.linder.powers['aerialAssault'].setUsed(True)
      self.assertFalse('aerialAssault' in self.linder.getPowers())
      self.linder.shortRest()
      self.assertFalse('aerialAssault' in self.linder.getPowers())
      self.linder.extendedRest()
      self.assertTrue('aerialAssault' in self.linder.getPowers())

if __name__ == '__main__':
    unittest.main()
