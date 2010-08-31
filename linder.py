from character import Character
from weapon import Weapon
from power import Power

class Linder(Character):
   def __init__(self):
      Character.__init__(self)
      self.setAbilities(str=13, con=12, dex=20, int=11, wis=14, cha=21)

      self.setSkills(acrobatics=True, athletics=True, bluff=True,
                       perception=True, stealth=True, streetwise=True,
                       thievery=True)

      #racial bonuses
      self.skill['diplomacy'].miscBonus = 2
      self.skill['insight'].miscBonus = 2

      self.proficiency['dagger'] = 3+1 #proficient + rogue class bonus
      self.proficiency['handCrossbow'] = 2
      self.setLvl(11)

      self.setPower(slyFlourish=SlyFlourish())
      self.setEquip(main=Misericorde())

class Misericorde(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 3
      self.damageDie = '1d8'
      self.critDamage = '3d6'
      self.damageType = 'str'
      self.keywords = ['dagger','lightBlade','radiant']

class SlyFlourish(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.abilityModDamage = ['dex','cha']

