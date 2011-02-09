from character import Character
from weapon import Weapon
from power import Power, Attack

class Gravis(Character):
   def __init__(self):
      Character.__init__(self)
      self.setAbilities(str=12, con=10, dex=10, int=12, wis=17, cha=16)

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
      self.setLvl(2)

      #at-wills
      self.setPower(priestsShield=PriestsShield(),
                    sacredFlame=SacredFlame(),
                    astralSeal=AstralSeal())

      #encounters
      self.setPower(shieldBearer=ShieldBearer(),
                    channelDivinityTurnUndead=ChannelDivinityTurnUndead(),
                    channelDivinityDivineFortune=ChannelDivinityDivineFortune(),
                    healingWord=HealingWord())

      #dailies
      self.setPower(astralCondemnation=AstralCondemnation(),
                    shieldOfFaith=ShieldOfFaith())

      self.setWeapon(mace=Mace(),
                     symbolOfDaring=SymbolOfDaring())

      self.setEquip(main='mace',
                    implement='symbolOfDaring')

class Mace(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 0
      self.damageDie = 'd8'
      self.numDie = 1
      self.damageType = 'str'
      self.weaponType = 'mace'
      self.keywords = ['mace','weapon']

class SymbolOfDaring(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 1
      self.damageDie = 'd8'
      self.numDie = 0
      self.extraCrit = '1d6'
      self.weaponType = 'implement'
      self.keywords = ['implement',]

#at-will
class PriestsShield(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'
      self.keywords = ['divine','weapon']
      primary = Attack()
      primary.attackType = 'str'
      primary.defenseType = 'AC'
      primary.weaponsOfDamage = 1
      primary.abilityModDamage = ['str']
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
