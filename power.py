class Power:
   def __init__(self):
      self.action = 'standard'
      self.frequency = 'at-will'
      self.keywords = []
      self.usesRemaining = 1
      self.maxUses = 1
      self.attacks = {}

   def available(self):
      return self.usesRemaining > 0

   def setUsed(self, used):
      if self.frequency == 'at-will': return
      if used:
         self.usesRemaining = max(self.usesRemaining-1,0)
      else:
         self.usesRemaining = self.maxUses

   def setAttack(self,**kwargs):
      for attack in kwargs:
         self.attacks[attack] = kwargs[attack]

   def text(self):
      text = ''
      for key in sorted(self.attacks.keys()):
         if not self.attacks[key].attackType: return ''
         text += key + ': \n'
         attack = self.attacks[key]
         if hasattr(attack,'attackBonus'): text += "attack bonus:" + str(attack.attackBonus) + '\n'
         if hasattr(attack,'totalDamage'): text += "normal damage:" + str(attack.totalDamage) + '\n'
         if hasattr(attack,'maxDamage'): text += "max damage:" + str(attack.maxDamage) + '\n'
         text += '\n'
      return text

   def generateStats(self,char,weapon):
      for key in self.attacks.keys():
         self.attacks[key].generateStats(char,weapon)

class Attack:
   def __init__(self):
      self.attackType = ''
      self.defenseType = ''
      self.nonWeaponDamageDie = 'd4'
      self.nonWeaponNumDie = 0
      self.weaponsOfDamage = 0
      self.extraAttack = 0
      self.abilityModDamage = []

   def generateStats(self, char,weapon):
      if self.attackType:
         self.attackBonus = char.lvl/2 + char.abilityMod[self.attackType]
         self.attackBonus += char.proficiency[weapon.weaponType] + weapon.enhancement
         self.attackBonus += self.extraAttack

         weaponDamageBonus = weapon.enhancement
         abilityWeaponBonus = sum([char.abilityMod[mod] for mod in self.abilityModDamage])
         self.extraCrit = ''
         if char.extraCrit: self.extraCrit+= char.extraCrit + '+'
         if weapon.extraCrit: self.extraCrit+= weapon.extraCrit + '+'

         weaponString = ''
         if self.weaponsOfDamage:
            weaponString = str(self.weaponsOfDamage*weapon.numDie) + weapon.damageDie + '+'
         nonWeaponString = ''
         if self.nonWeaponNumDie:
            nonWeaponString = str(self.nonWeaponNumDie) + self.nonWeaponDamageDie + '+'

         self.numericBonus = weaponDamageBonus + abilityWeaponBonus
         self.totalDamage =  weaponString + nonWeaponString + str(self.numericBonus)

         maxDamageValue = self.weaponsOfDamage*(int(weapon.damageDie[1:])*weapon.numDie) \
                          + self.nonWeaponNumDie*int(self.nonWeaponDamageDie[1:]) \
                          + self.numericBonus
         self.maxDamage = self.extraCrit + str(maxDamageValue)

   def text(self):
      if not self.attackType: return ''
      text = "attack bonus:" + str(self.attackBonus) + '\n'
      text += "normal damage:" +  str(self.totalDamage) + '\n'
      text += "max damage:" + str(self.maxDamage) + '\n'
      return text
