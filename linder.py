from character import Character
from weapon import Weapon
from power import Power, Attack

class Linder(Character):
   def __init__(self):
      Character.__init__(self)
      self.setAbilities(str=13, con=12, dex=24, int=11, wis=15, cha=22)

      self.setSkills(acrobatics=True, athletics=True, bluff=True,
                       perception=True, stealth=True, streetwise=True,
                       thievery=True)

      #racial bonuses
      self.skill['diplomacy'].miscBonus = 2
      self.skill['insight'].miscBonus = 2

      #Devastating Critical feat
      self.extraCrit = '1d10'

      #jet black stone bonus
      self.skill['stealth'].miscBonus = 4

      self.proficiency['dagger'] = 3+1 #proficient + rogue class bonus
      self.proficiency['handCrossbow'] = 2
      self.setLvl(17)

      #at-wills
      self.setPower(slyFlourish=SlyFlourish(),
                    acrobaticStrike=AcrobaticStrike())

      #encounters
      self.setPower(shadowJaunt=ShadowJaunt(),
                    fadingStrike=FadingStrike(),
                    jumpingBladeAssault=JumpingBladeAssault(),
                    escapeArtistsGambit=EscapeArtistsGambit(),
                    cleverMove=CleverMove(),
                    sneakInTheAttack=SneakInTheAttack(),
                    rockyIVPunch=RockyIVPunch(),
                    criticalOpportunity=CriticalOpportunity(),
                    tumblingDodge=TumblingDodge(),
                    combatTumbleset=CombatTumbleset(),
                    tornadoStrike=TornadoStrike(),
                    oathOfEnmity=OathOfEnmity())

      #dailies
      self.setPower(slayingStrike=SlayingStrike(),
                    aerialAssault=AerialAssault(),
                    trickStrike=TrickStrike(),
                    badIdeaFriend=BadIdeaFriend())

      self.setWeapon(misericorde=Misericorde(),
                     poisonedCrossbow=PoisonedCrossbow(),
                     cloakedDagger=CloakedDagger(),
                     unarmed=Unarmed())

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
      self.extraCrit = '3d6'

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
      self.extraCrit = '1d6'

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
      self.extraCrit = '2d6'

class Unarmed(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 0
      self.damageDie = 'd4'
      self.numDie = 1
      self.critDamage = ''
      self.damageType = 'str'
      self.weaponType = 'fist'
      self.keywords = ['unarmed']
      self.extraCrit = ''

#at-will
class SlyFlourish(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 1
      primary.abilityModDamage = ['dex','cha']
      self.setAttack(primary=primary)

class AcrobaticStrike(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 1
      primary.abilityModDamage = ['dex']
      self.frequency = 'at-will'
      self.setAttack(primary=primary)

#encounter
class FadingStrike(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 1
      primary.abilityModDamage = ['dex']
      self.frequency = 'encounter'
      self.setAttack(primary=primary)

class JumpingBladeAssault(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC' #FIXME: or ref
      primary.weaponsOfDamage = 2
      primary.abilityModDamage = ['dex']
      self.frequency = 'encounter'
      self.setAttack(primary=primary)

class OathOfEnmity(Power):
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
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 3
      primary.abilityModDamage = ['dex']
      self.frequency = 'encounter'
      self.setAttack(primary=primary)

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

class TornadoStrike(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 2
      primary.abilityModDamage = ['dex']
      self.frequency = 'encounter'
      self.setAttack(primary=primary)

class CleverMove(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'interrupt'

class EscapeArtistsGambit(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 2
      primary.abilityModDamage = ['dex']
      self.frequency = 'encounter'
      self.setAttack(primary=primary)

class SneakInTheAttack(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'minor'

class RockyIVPunch(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'ref'
      primary.weaponsOfDamage = 0
      self.frequency = 'encounter'
      self.action = 'minor'
      self.setAttack(primary=primary)

#daily
class SlayingStrike(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'daily'
      targetBloodied = Attack()
      targetBloodied.attackType = 'dex'
      targetBloodied.defenseType = 'AC'
      targetBloodied.weaponsOfDamage = 5
      targetBloodied.abilityModDamage = ['dex','str']
      targetUnbloodied = Attack()
      targetUnbloodied.attackType = 'dex'
      targetUnbloodied.defenseType = 'AC'
      targetUnbloodied.weaponsOfDamage = 3
      targetUnbloodied.abilityModDamage = ['dex',]
      self.setAttack(targetBloodied=targetBloodied,targetUnbloodied=targetUnbloodied)

class AerialAssault(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'ref'
      primary.weaponsOfDamage = 3
      primary.abilityModDamage = ['dex']
      self.frequency = 'daily'
      self.setAttack(primary=primary)

class TrickStrike(Power):
   def __init__(self):
      Power.__init__(self)
      primary = Attack()
      primary.attackType = 'dex'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 3
      primary.abilityModDamage = ['dex']
      self.frequency = 'daily'
      self.setAttack(primary=primary)

class BadIdeaFriend(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'daily'
      self.action = 'interrupt'

if __name__ == "__main__":
   import sys
   from PyQt4 import QtGui
   import gui

   app = QtGui.QApplication(sys.argv)

   linder = Linder()

   window = gui.MainWindow()
   window.setCharacter(linder)
   sys.exit(app.exec_())
