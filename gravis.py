from character import Character
from weapon import Weapon
from power import Power, Attack

class Gravis(Character):
   def __init__(self):
      Character.__init__(self)
      self.setAbilities(str=12, con=10, dex=10, int=12, wis=18, cha=17)

      self.setSkills(heal=True, insight=True, arcana=True, history=True,
                     religion=True)

      #background trait
      self.skill['insight'].miscBonus = 2

      #combat medic feat bonus
      self.skill['heal'].miscBonus = 2

      #armor penalties
      self.skill['acrobatics'].miscBonus = -1
      self.skill['athletics'].miscBonus = -1
      self.skill['endurance'].miscBonus = -1
      self.skill['stealth'].miscBonus = -1
      self.skill['thievery'].miscBonus = -1

      #proficiencies (only bothering with relevant ones)
      self.proficiency['staff'] = 2
      self.proficiency['mace'] = 2
      self.proficiency['implement'] = 1 #implement expertise feat
      self.setLvl(5)

      #at-wills
      self.setPower(lanceOfFaith=LanceOfFaith(),
                    sacredFlame=SacredFlame(),
                    astralSeal=AstralSeal())

      #encounters
      self.setPower(shieldBearer=ShieldBearer(),
                    channelDivinityTurnUndead=ChannelDivinityTurnUndead(),
                    channelDivinityDivineFortune=ChannelDivinityDivineFortune(),
                    healingWord=HealingWord(),
                    hymnOfResurgence=HymnOfResurgence(),
                    radiantSmite=RadiantSmite())

      #dailies
      self.setPower(astralCondemnation=AstralCondemnation(),
                    shieldOfFaith=ShieldOfFaith(),
                    spiritualWeapon=SpiritualWeapon())

      self.setWeapon(mace=Mace(),
                     orbOfLight=OrbOfLight())

      self.setEquip(main='mace',
                    implement='orbOfLight')

class Mace(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 0
      self.damageDie = 'd8'
      self.numDie = 1
      self.damageType = 'str'
      self.weaponType = 'mace'
      self.keywords = ['mace','weapon']

class OrbOfLight(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 2
      self.damageDie = 'd8'
      self.numDie = 0
      self.extraCrit = '2d6'
      self.weaponType = 'implement'
      self.keywords = ['implement',]

#at-will
class LanceOfFaith(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'
      self.keywords = ['divine','implement','radiant']
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'ref'
      primary.nonWeaponDamageDie = 'd8'
      primary.nonWeaponNumDie = 1
      primary.abilityModDamage = ['wis']
      self.setAttack(primary=primary)

class SacredFlame(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'
      self.keywords = ['divine','implement','radiant']
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'ref'
      primary.nonWeaponDamageDie = 'd6'
      primary.nonWeaponNumDie = 1
      primary.abilityModDamage = ['wis']
      self.setAttack(primary=primary)

class AstralSeal(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'
      self.keywords = ['divine','healing','implement']
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'ref'
      primary.weaponsOfDamage = 0
      primary.extraAttack = 2
      self.setAttack(primary=primary)

#encounter
class HymnOfResurgence(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.keywords = ['divine','implement']
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'for'
      primary.weaponsOfDamage = 0
      self.setAttack(primary=primary)

class ShieldBearer(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.keywords = ['conjuration','divine','implement','radiant']
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'ref'
      primary.nonWeaponDamageDie = 'd8'
      primary.nonWeaponNumDie = 2
      primary.abilityModDamage = ['wis']
      self.setAttack(primary=primary)

class ChannelDivinityTurnUndead(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.keywords = ['divine','implement','radiant']
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'wil'
      primary.nonWeaponDamageDie = 'd10'
      primary.nonWeaponNumDie = 1
      primary.abilityModDamage = ['wis']
      self.setAttack(primary=primary)

class ChannelDivinityDivineFortune(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.keywords = ['divine']
      #self.action = 'free' #FIXME

class HealingWord(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'minor'
      self.maxUses = 2
      self.usesRemaining = 2
      self.keywords = ['divine','healing']

class RadiantSmite(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.keywords = ['divine','radiant','weapon']
      primary = Attack()
      primary.attackType = 'str'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 2
      primary.abilityModDamage = ['str','wis']
      self.setAttack(primary=primary)

#daily
class AstralCondemnation(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'daily'
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'ref'
      primary.nonWeaponDamageDie = 'd6'
      primary.nonWeaponNumDie = 3
      primary.abilityModDamage = ['wis']
      self.setAttack(primary=primary)
      self.keywords = ['divine','implement','radiant']

class SpiritualWeapon(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'daily'
      primary = Attack()
      primary.attackType = 'wis'
      primary.defenseType = 'AC'
      primary.nonWeaponDamageDie = 'd10'
      primary.nonWeaponNumDie = 1
      primary.abilityModDamage = ['wis']
      self.setAttack(primary=primary)
      self.keywords = ['divine','implement','conjuration']

class ShieldOfFaith(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'daily'
      self.keywords = ['divine']

if __name__ == "__main__":
   import sys
   from PyQt4 import QtGui
   import gui

   app = QtGui.QApplication(sys.argv)

   gravis = Gravis()

   window = gui.MainWindow()
   window.setCharacter(gravis)
   sys.exit(app.exec_())
