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

   def testLevel(self):
      self.assertEqual(self.gravis.lvl, 5)

   def test_skill(self):
      self.assertEqual(self.gravis.skill['stealth'].value(), 1)
      self.assertEqual(self.gravis.skill['athletics'].value(), 2)
      self.assertEqual(self.gravis.skill['arcana'].value(), 8)
      self.assertEqual(self.gravis.skill['heal'].value(), 13)
      self.assertEqual(self.gravis.skill['insight'].value(), 13)

   def test_ability_mod(self):
      self.assertEqual(self.gravis.abilityMod['str'], 1)
      self.assertEqual(self.gravis.abilityMod['con'], 0)
      self.assertEqual(self.gravis.abilityMod['dex'], 0)
      self.assertEqual(self.gravis.abilityMod['int'], 1)
      self.assertEqual(self.gravis.abilityMod['wis'], 4)
      self.assertEqual(self.gravis.abilityMod['cha'], 3)

class TestLinderPowers(unittest.TestCase):
   def setUp(self):
      import linder
      self.linder = linder.Linder()

   def test_power_attack_bonus(self):
      self.linder.getPowerStats('slyFlourish',output=False)
      self.assertEqual(self.linder.powers['slyFlourish'].attacks['primary'].attackBonus, 22)
      self.assertEqual(self.linder.powers['slyFlourish'].attacks['primary'].totalDamage, '1d8+16')
      self.assertEqual(self.linder.powers['slyFlourish'].attacks['primary'].maxDamage, '1d10+3d6+24')

   def test_multiweapon_power_bonus(self):
      self.linder.getPowerStats('slayingStrike',output=False)
      bloodied = self.linder.powers['slayingStrike'].attacks['targetBloodied']
      unbloodied = self.linder.powers['slayingStrike'].attacks['targetUnbloodied']
      self.assertEqual(bloodied.attackBonus, 22)
      self.assertEqual(bloodied.totalDamage, '5d8+11')
      self.assertEqual(bloodied.maxDamage, '1d10+3d6+51')
      self.assertEqual(unbloodied.attackBonus, 22)
      self.assertEqual(unbloodied.totalDamage, '3d8+10')
      self.assertEqual(unbloodied.maxDamage, '1d10+3d6+34')

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

class TestGravisPowers(unittest.TestCase):
   def setUp(self):
      import gravis
      self.gravis = gravis.Gravis()

   def test_implement_attack(self):
      self.gravis.getPowerStats('sacredFlame',hand='implement',output=False)
      self.assertEqual(self.gravis.powers['sacredFlame'].attacks['primary'].attackBonus, 9)
      self.assertEqual(self.gravis.powers['sacredFlame'].attacks['primary'].totalDamage, '1d6+6')
      self.assertEqual(self.gravis.powers['sacredFlame'].attacks['primary'].maxDamage, '2d6+12')

   def test_mace_attack(self):
      self.gravis.getPowerStats('radiantSmite',hand='main',output=False)
      self.assertEqual(self.gravis.powers['radiantSmite'].attacks['primary'].attackBonus, 5)
      self.assertEqual(self.gravis.powers['radiantSmite'].attacks['primary'].totalDamage, '2d8+5')
      self.assertEqual(self.gravis.powers['radiantSmite'].attacks['primary'].maxDamage, '21')

   def test_multiuse_availability(self):
      self.assertTrue('healingWord' in self.gravis.getPowers())
      self.gravis.powers['healingWord'].setUsed(True)
      self.assertTrue('healingWord' in self.gravis.getPowers())
      self.gravis.powers['healingWord'].setUsed(True)
      self.assertFalse('healingWord' in self.gravis.getPowers())
      self.gravis.shortRest()
      self.assertTrue('healingWord' in self.gravis.getPowers())

   def test_power_attack_bonus(self):
      self.gravis.getPowerStats('astralSeal',hand='implement',output=False)
      self.assertEqual(self.gravis.powers['astralSeal'].attacks['primary'].attackBonus, 11)

if __name__ == '__main__':
    unittest.main()
