from character import Character
from weapon import Weapon
from power import Power

class Gravis(Character):
   def __init__(self):
      Character.__init__(self)
      self.setAbilities(str=12, con=10, dex=10, int=12, wis=17, cha=16)

      self.setSkills(heal=True, insight=True, arcana=True, history=True,
                     religion=True)

      #background trait
      self.skill['insight'].miscBonus = 2

      #armor penalties
      self.skill['acrobatics'].miscBonus = -1
      self.skill['athletics'].miscBonus = -1
      self.skill['endurance'].miscBonus = -1
      self.skill['stealth'].miscBonus = -1
      self.skill['thievery'].miscBonus = -1

      #proficiencies (only bothering with relevant ones)
      self.proficiency['staff'] = 2
      self.proficiency['implement'] = 1 #implement expertise feat
      self.setLvl(1)

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
      self.setPower(astralCondemnation=AstralCondemnation())

      self.setWeapon(quarterstaff=Quarterstaff(),
                     holySymbol=HolySymbol())

      self.setEquip(main='quarterstaff',
                    implement='holySymbol')

class Quarterstaff(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 0
      self.damageDie = 'd8'
      self.numDie = 1
      self.damageType = 'str'
      self.weaponType = 'staff'
      self.keywords = ['staff',]

class HolySymbol(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 0
      self.damageDie = 'd8'
      self.numDie = 0
      self.damageType = 'str'
      self.weaponType = 'staff'
      self.keywords = ['implement',]

#at-will
class PriestsShield(Power):
   def __init__(self):
      Power.__init__(self)
      self.attackType = 'str'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 1
      self.abilityModDamage = ['str']
      self.frequency = 'at-will'

class SacredFlame(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'

class AstralSeal(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'at-will'

#encounter
class ShieldBearer(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'

class ChannelDivinityTurnUndead(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'

class ChannelDivinityDivineFortune(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      #self.action = 'free' #FIXME

class HealingWord(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'encounter'
      self.action = 'minor'
      self.maxUses = 2
      self.usesRemaining = 2

#daily
class AstralCondemnation(Power):
   def __init__(self):
      Power.__init__(self)
      self.frequency = 'daily'

if __name__ == "__main__":
   import sys
   from PyQt4 import QtGui
   import gui

   app = QtGui.QApplication(sys.argv)

   gravis = Gravis()

   window = gui.MainWindow()
   window.setCharacter(gravis)
   sys.exit(app.exec_())
