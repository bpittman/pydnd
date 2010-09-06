import unittest
from character import Character
from weapon import Weapon
from power import Power

class TestCharacter(unittest.TestCase):
   def setUp(self):
      import linder
      self.linder = linder.Linder()

   def test_skill(self):
      self.assertEqual(self.linder.skill['stealth'].value(), 23)
      self.assertEqual(self.linder.skill['athletics'].value(), 13)
      self.assertEqual(self.linder.skill['arcana'].value(), 7)
      self.assertEqual(self.linder.skill['acrobatics'].value(), 19)
      self.assertEqual(self.linder.skill['insight'].value(), 11)

   def test_ability_mod(self):
      self.assertEqual(self.linder.abilityMod['str'], 1)
      self.assertEqual(self.linder.abilityMod['con'], 1)
      self.assertEqual(self.linder.abilityMod['dex'], 7)
      self.assertEqual(self.linder.abilityMod['int'], 0)
      self.assertEqual(self.linder.abilityMod['wis'], 2)
      self.assertEqual(self.linder.abilityMod['cha'], 6)

class TestPowers(unittest.TestCase):
   def setUp(self):
      import linder
      self.linder = linder.Linder()

   def test_power_attack_bonus(self):
      self.linder.getPowerStats('slyFlourish',output=False)
      self.assertEqual(self.linder.powers['slyFlourish'].attackBonus, 21)
      self.assertEqual(self.linder.powers['slyFlourish'].totalDamage, '1d8+17')
      self.assertEqual(self.linder.powers['slyFlourish'].maxDamage, 25)
      self.assertEqual(self.linder.powers['slyFlourish'].maxPlusWeapon, '1d8+25')

   def test_encounter_availability(self):
      self.assertTrue('tornadoStrike' in self.linder.getPowers())
      self.linder.powers['tornadoStrike'].setUsed(True)
      self.assertFalse('tornadoStrike' in self.linder.getPowers())
      self.linder.shortRest()
      self.assertTrue('tornadoStrike' in self.linder.getPowers())

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
