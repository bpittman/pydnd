class Power:
   def __init__(self):
      self.action = 'standard'
      self.frequency = 'at-will'
      self.keywords = ''
      self.attackType = 'str'
      self.defenseType = 'AC'
      self.weaponsOfDamage = 1
      self.abilityModDamage = ['str',]

   def use(self,char, weapon):
      self.attackBonus = char.lvl/2 + char.abilityMod[self.attackType]
      self.attackBonus += char.proficiency[weapon.weaponType] + weapon.enhancement

      self.damageBonus = self.weaponsOfDamage*(char.abilityMod[weapon.damageType] + weapon.enhancement)
      self.damageBonus += sum([char.abilityMod[mod] for mod in self.abilityModDamage])
      self.totalDamage = weapon.damageDie + '+' + str(self.damageBonus)
