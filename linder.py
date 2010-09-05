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

      #at-wills
      self.setPower(slyFlourish=SlyFlourish(),
                    acrobaticStrike=AcrobaticStrike(),
                    fleetingGhost=FleetingGhost())

      #encounters
      self.setPower(shadowJaunt=ShadowJaunt(),
                    positioningStrike=PositioningStrike(),
                    fadingStrike=FadingStrike(),
                    jumpingBladeAssault=JumpingBladeAssault(),
                    snapShot=SnapShot(),
                    huntersQuarry=HuntersQuarry(),
                    criticalOpportunity=CriticalOpportunity(),
                    tumblingDodge=TumblingDodge(),
                    combatTumbleset=CombatTumbleset())

      #dailies
      self.setPower(handspringAssault=HandspringAssault(),
                    mockingStrike=MockingStrike(),
                    aerialAssault=AerialAssault())

      self.setWeapon(misericorde=Misericorde(),
                     poisonedCrossbow=PoisonedCrossbow(),
                     cloakedDagger=CloakedDagger())

      self.setEquip(main='misericorde')

class Misericorde(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 3
      self.damageDie = 'd8'
      self.numDie = 1
      self.critDamage = '3d6'
      self.damageType = 'str'
      self.weaponType = 'dagger'
      self.keywords = ['dagger','lightBlade','radiant']

class PoisonedCrossbow(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 1
      self.damageDie = 'd6'
      self.numDie = 1
      self.critDamage = ''
      self.damageType = 'dex'
      self.weaponType = 'handCrossbow'
      self.keywords = ['handCrossbow','ranged']

class CloakedDagger(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 2
      self.damageDie = 'd4'
      self.numDie = 1
      self.critDamage = ''
      self.damageType = 'str'
      self.weaponType = 'dagger'
      self.keywords = ['dagger','lightBlade']

#at-will
class SlyFlourish(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 1
      self.abilityModDamage = ['dex','cha']
      self.frequency = 'at-will'

class AcrobaticStrike(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 1
      self.abilityModDamage = ['dex']
      self.frequency = 'at-will'

class FleetingGhost(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'
      self.action = 'move'

#encounter
class PositioningStrike(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'will'
      self.weaponsOfDamage = 1
      self.abilityModDamage = ['dex']
      self.frequency = 'encounter'

class SnapShot(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 1
      self.abilityModDamage = ['dex']
      self.frequency = 'encounter'
      self.action = 'minor'

class FadingStrike(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 1
      self.abilityModDamage = ['dex']
      self.frequency = 'encounter'

class JumpingBladeAssault(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'AC' #FIXME: or ref
      self.weaponsOfDamage = 2
      self.abilityModDamage = ['dex']
      self.frequency = 'encounter'

class HuntersQuarry(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'minor'

class ShadowJaunt(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'move'

class CriticalOpportunity(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 3
      self.abilityModDamage = ['dex']
      self.frequency = 'encounter'

class TumblingDodge(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'interrupt'

class CombatTumbleset(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'move'

#daily
class HandspringAssault(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 3
      self.abilityModDamage = ['dex']
      self.frequency = 'daily'

class MockingStrike(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'will'
      self.weaponsOfDamage = 2
      self.abilityModDamage = ['dex']
      self.frequency = 'daily'

class AerialAssault(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'dex'
      self.defenseType = 'ref'
      self.weaponsOfDamage = 3
      self.abilityModDamage = ['dex']
      self.frequency = 'daily'


if __name__ == "__main__":
   import sys
   from PyQt4 import QtGui
   import gui

   app = QtGui.QApplication(sys.argv)

   linder = Linder()

   window = gui.MainWindow()
   window.setCharacter(linder)
   sys.exit(app.exec_())
