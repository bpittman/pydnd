class Power:
   def __init__(self):
      self.action = 'standard'
      self.frequency = 'at-will'
      self.keywords = ''
      self.attackType = ''
      self.defenseType = ''
      self.weaponsOfDamage = 0
      self.abilityModDamage = []
      self.usesRemaining = 1
      self.maxUses = 1

   def generateStats(self,char, weapon):
      if self.attackType:
         self.attackBonus = char.lvl/2 + char.abilityMod[self.attackType]
         self.attackBonus += char.proficiency[weapon.weaponType] + weapon.enhancement

         weaponDamageBonus = weapon.enhancement
         abilityWeaponBonus = sum([char.abilityMod[mod] for mod in self.abilityModDamage])
         self.extraCrit = ''
         if char.extraCrit: self.extraCrit+= char.extraCrit + '+'
         if weapon.extraCrit: self.extraCrit+= weapon.extraCrit + '+'

         weaponString = str(self.weaponsOfDamage*weapon.numDie) + weapon.damageDie
         self.numericBonus = weaponDamageBonus + abilityWeaponBonus
         self.totalDamage =  weaponString + '+' + str(self.numericBonus)

         #house rules crit system
         maxDamageValue = self.weaponsOfDamage*(int(weapon.damageDie[1:])*weapon.numDie) + self.numericBonus
         self.maxDamage = self.extraCrit + str(maxDamageValue)

   def available(self):
      return self.usesRemaining > 0

   def text(self):
      if not self.attackType: return ''
      text = "attack bonus:" + str(self.attackBonus) + '\n'
      text += "normal damage:" +  str(self.totalDamage) + '\n'
      text += "max damage:" + str(self.maxDamage) + '\n'
      return text

   def setUsed(self, used):
      if self.frequency == 'at-will': return
      if used:
         self.usesRemaining = max(self.usesRemaining-1,0)
      else:
         self.usesRemaining = self.maxUses
