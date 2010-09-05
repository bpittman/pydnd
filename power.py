class Power:
   def __init__(self):
      self.action = 'standard'
      self.frequency = 'at-will'
      self.keywords = ''
      self.attackType = ''
      self.defenseType = ''
      self.weaponsOfDamage = 0
      self.abilityModDamage = []

   def use(self,char, weapon):
      if self.attackType:
         self.attackBonus = char.lvl/2 + char.abilityMod[self.attackType]
         self.attackBonus += char.proficiency[weapon.weaponType] + weapon.enhancement

         perWeaponDamageBonus = char.abilityMod[weapon.damageType] + weapon.enhancement
         weaponDamageBonus = self.weaponsOfDamage*(perWeaponDamageBonus)
         abilityWeaponBonus = sum([char.abilityMod[mod] for mod in self.abilityModDamage])

         weaponString = str(self.weaponsOfDamage*weapon.numDie) + weapon.damageDie

         self.totalDamage =  weaponString + '+' + str(weaponDamageBonus+abilityWeaponBonus)

         #house rules crit system
         self.maxDamage = self.weaponsOfDamage*(perWeaponDamageBonus + int(weapon.damageDie[1:])*weapon.numDie)
         self.maxDamage += abilityWeaponBonus
         self.maxPlusWeapon = weaponString + '+' + str(self.maxDamage)

   def text(self):
      if not self.attackType: return 'no attack'
      text = "attack bonus:" + str(self.attackBonus) + '\n'
      text += "normal damage:" +  str(self.totalDamage) + '\n'
      text += "max damage:" +  str(self.maxDamage) + '\n'
      text += "max+weap damage:" +  str(self.maxPlusWeapon) + '\n'
      text += "double max damage:" +  str(2*self.maxDamage) + '\n'
      return text
