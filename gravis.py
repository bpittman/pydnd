from character import Character
from weapon import Weapon
from power import Power

class Doctor(Character):
   def __init__(self):
      Character.__init__(self)
      self.setAbilities(str=12, con=10, dex=10, int=12, wis=17, cha=16)

      self.setSkills(heal=True, insight=True, arcana=True, history=True,
                     religion=True)

      #background trait
      self.skill['insight'].miscBonus = 2

      #proficiencies (only bothering with relevant ones)
      self.proficiency['staff'] = 2
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

      self.setWeapon(quarterstaff=Quarterstaff())

      self.setEquip(main='quarterstaff')

class Quarterstaff(Weapon):
   def __init__(self):
      Weapon.__init__(self)
      self.enhancement = 0
      self.damageDie = 'd8'
      self.numDie = 1
      self.damageType = 'str'
      self.weaponType = 'staff'
      self.keywords = ['staff',]

#at-will
class PriestsShield(Power):
   def __init__(self):
      Power.__init__(self)
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

   doctor = Doctor()

   window = gui.MainWindow()
   window.setCharacter(doctor)
   sys.exit(app.exec_())
