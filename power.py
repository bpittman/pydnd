class Power:
   def __init__(self):
      self.action = 'standard'
      self.frequency = 'at-will'
      self.keywords = ''
      self.attackType = ''
      self.defenseType = ''
      self.weaponsOfDamage = 0
      self.abilityModDamage = []
      self.used = False

   def generateStats(self,char, weapon):
      if self.attackType:
         self.attackBonus = char.lvl/2 + char.abilityMod[self.attackType]
         self.attackBonus += char.proficiency[weapon.weaponType] + weapon.enhancement

         weaponTypeBonus = char.abilityMod[weapon.damageType]
         perWeaponDamageBonus = weapon.enhancement
         weaponDamageBonus = self.weaponsOfDamage*(perWeaponDamageBonus)
         abilityWeaponBonus = sum([char.abilityMod[mod] for mod in self.abilityModDamage])

         weaponString = str(self.weaponsOfDamage*weapon.numDie) + weapon.damageDie

         self.totalDamage =  weaponString + '+' + str(weaponDamageBonus+abilityWeaponBonus + weaponTypeBonus)

         #house rules crit system
         self.maxDamage = self.weaponsOfDamage*(perWeaponDamageBonus + int(weapon.damageDie[1:])*weapon.numDie)
         self.maxDamage += abilityWeaponBonus + char.abilityMod[weapon.damageType]
         self.maxPlusWeapon = '1'+weapon.damageDie + '+' + str(self.maxDamage+perWeaponDamageBonus)

   def text(self):
      if not self.attackType: return ''
      text = "attack bonus:" + str(self.attackBonus) + '\n'
      text += "normal damage:" +  str(self.totalDamage) + '\n'
      text += "max damage:" +  str(self.maxDamage) + '\n'
      text += "max+weap damage:" +  str(self.maxPlusWeapon) + '\n'
      text += "double max damage:" +  str(2*self.maxDamage) + '\n'
      return text

   def setUsed(self, used):
      self.used = used if not self.frequency == 'at-will' else False
