import unittest
from character import Character
from weapon import Weapon
from power import Power

class TestLinder(unittest.TestCase):
   def setUp(self):
      import linder
      self.linder = linder.Linder()

   def test_skill(self):
      self.assertEqual(self.linder.skill['stealth'].value(), 24)
      self.assertEqual(self.linder.skill['athletics'].value(), 14)
      self.assertEqual(self.linder.skill['arcana'].value(), 8)
      self.assertEqual(self.linder.skill['acrobatics'].value(), 20)
      self.assertEqual(self.linder.skill['insight'].value(), 12)

   def test_ability_mod(self):
      self.assertEqual(self.linder.abilityMod['str'], 1)
      self.assertEqual(self.linder.abilityMod['con'], 1)
      self.assertEqual(self.linder.abilityMod['dex'], 7)
      self.assertEqual(self.linder.abilityMod['int'], 0)
      self.assertEqual(self.linder.abilityMod['wis'], 2)
      self.assertEqual(self.linder.abilityMod['cha'], 6)

class TestGravis(unittest.TestCase):
   def setUp(self):
      import gravis
      self.gravis = gravis.Gravis()

   def test_skill(self):
      self.assertEqual(self.gravis.skill['stealth'].value(), -1)
      self.assertEqual(self.gravis.skill['athletics'].value(), 0)
      self.assertEqual(self.gravis.skill['arcana'].value(), 6)
      self.assertEqual(self.gravis.skill['heal'].value(), 8)
      self.assertEqual(self.gravis.skill['insight'].value(), 10)

   def test_ability_mod(self):
      self.assertEqual(self.gravis.abilityMod['str'], 1)
      self.assertEqual(self.gravis.abilityMod['con'], 0)
      self.assertEqual(self.gravis.abilityMod['dex'], 0)
      self.assertEqual(self.gravis.abilityMod['int'], 1)
      self.assertEqual(self.gravis.abilityMod['wis'], 3)
      self.assertEqual(self.gravis.abilityMod['cha'], 3)

class TestPowers(unittest.TestCase):
   def setUp(self):
      import linder
      self.linder = linder.Linder()

   def test_power_attack_bonus(self):
      self.linder.getPowerStats('slyFlourish',output=False)
      self.assertEqual(self.linder.powers['slyFlourish'].attackBonus, 22)
      self.assertEqual(self.linder.powers['slyFlourish'].totalDamage, '1d8+16')
      self.assertEqual(self.linder.powers['slyFlourish'].maxDamage, '1d10+3d6+24')

   def test_multiweapon_power_bonus(self):
      self.linder.getPowerStats('slayingStrike',output=False)
      self.assertEqual(self.linder.powers['slayingStrike'].attackBonus, 22)
      self.assertEqual(self.linder.powers['slayingStrike'].totalDamage, '5d8+11')
      self.assertEqual(self.linder.powers['slayingStrike'].maxDamage, '1d10+3d6+51')

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
