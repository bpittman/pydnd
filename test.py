import unittest
from character import Character
from weapon import Weapon
from power import Power

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

   def test_ability_mod(self):
      self.assertEqual(self.linder.abilityMod['str'], 1)
      self.assertEqual(self.linder.abilityMod['con'], 1)
      self.assertEqual(self.linder.abilityMod['dex'], 5)
      self.assertEqual(self.linder.abilityMod['int'], 0)
      self.assertEqual(self.linder.abilityMod['wis'], 2)
      self.assertEqual(self.linder.abilityMod['cha'], 5)

class TestWeapon(unittest.TestCase):
   def setUp(self):
      self.linder = Character()
      self.linder.setAbilities(str=13, con=12, dex=20, int=11, wis=14, cha=21)
      self.linder.setSkills(acrobatics=True, athletics=True, bluff=True,
                       perception=True, stealth=True, streetwise=True,
                       thievery=True)
      self.linder.skill['diplomacy'].miscBonus = 2
      self.linder.skill['insight'].miscBonus = 2
      self.linder.setLvl(11)
      self.linder.proficiency['dagger'] = 4 #3 prof + 1 rogue class

      self.misericorde = Weapon()
      self.misericorde.enhancement = 3
      self.misericorde.damageDie = 'd8'
      self.misericorde.numDie = 1
      self.misericorde.critDamage = '3d6'
      self.misericorde.damageType = 'str'
      self.misericorde.keywords = ['dagger','lightBlade','radiant']

      self.slyFlourish = Power()
      self.slyFlourish.attackType = 'dex'
      self.slyFlourish.defenseType = 'AC'
      self.slyFlourish.weaponsOfDamage = 1
      self.slyFlourish.abilityModDamage = ['dex','cha']

      self.linder.setWeapon(misericorde=self.misericorde)
      self.linder.setEquip(main='misericorde')
      self.linder.setPower(slyFlourish=self.slyFlourish)
      self.linder.getPowerStats("slyFlourish",output=False)

   def test_power_attack_bonus(self):
      self.assertEqual(self.slyFlourish.attackBonus, 17)
      self.assertEqual(self.slyFlourish.totalDamage, '1d8+14')
      self.assertEqual(self.slyFlourish.maxDamage, 22)
      self.assertEqual(self.slyFlourish.maxPlusWeapon, '1d8+22')

if __name__ == '__main__':
    unittest.main()
