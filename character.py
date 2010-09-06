from skill import Skill
from collections import defaultdict

class Character:
   def __init__(self):
      abilities = ['str','con','dex','int','wis','cha']

      skills = [('acrobatics','dex'),
                ('arcana','int'),
                ('athletics','str'),
                ('bluff','cha'),
                ('diplomacy','cha'),
                ('dungeoneering','wis'),
                ('endurance','con'),
                ('heal','wis'),
                ('history','int'),
                ('insight','wis'),
                ('intimidate','cha'),
                ('nature','wis'),
                ('perception','wis'),
                ('religion','int'),
                ('stealth','dex'),
                ('streetwise','cha'),
                ('thievery','dex')]

      self.ability = dict((a,1) for a in abilities)
      self.abilityMod = dict((a,0) for a in abilities)
      self.skill = dict((s,Skill(a)) for s,a in skills)
      self.setLvl(1)
      self.proficiency = defaultdict(int)
      self.equipped = {}
      self.powers = {}
      self.weapons = {}

   def setLvl(self,lvl):
      self.lvl = lvl
      self.updateAbilityMods()
      self.updateSkills()

   def setAbilities(self,**kwargs):
      for abil in self.ability:
         if abil in kwargs: self.ability[abil] = kwargs[abil]

   def setSkills(self,**kwargs):
      for skill in self.skill:
         if skill in kwargs: self.skill[skill].setTrained(kwargs[skill])

   def setProficiency(self,name,value):
      self.proficiency[name] = value

   def updateAbilityMods(self):
      for m in self.abilityMod:
         self.abilityMod[m] = (self.ability[m] - 10)/2 

   def updateSkills(self):
      for s in self.skill:
         self.skill[s].update(self.lvl,self.abilityMod)

   def setEquip(self,**kwargs):
      for hand in kwargs:
         self.equipped[hand] = kwargs[hand]

   def setPower(self,**kwargs):
      for power in kwargs:
         self.powers[power] = kwargs[power]

   def setWeapon(self,**kwargs):
      for weapon in kwargs:
         self.weapons[weapon] = kwargs[weapon]

   def getPowers(self,frequency=['at-will','encounter','daily'],
                      action=['standard','move','minor'],
                      usage=['unused']):
      l = []
      for p in self.powers:
         if not self.powers[p].frequency in frequency: continue
         if not self.powers[p].action in action: continue
         if self.powers[p].used and 'used' not in usage: continue
         if not self.powers[p].used and 'unused' not in usage: continue
         l.append(p)
      return l

   def getPowerStats(self,power,hand="main",output=True):
      if hand in self.equipped and power in self.powers:
         self.powers[power].generateStats(self,self.weapons[self.equipped[hand]])
      if output and self.powers[power].weaponsOfDamage > 0:
         print "attack bonus:", self.powers[power].attackBonus
         print "normal damage:", self.powers[power].totalDamage
         print "max damage:", self.powers[power].maxDamage
         print "max+weap damage:", self.powers[power].maxPlusWeapon
         print "double max damage:", 2*self.powers[power].maxDamage

   def shortRest(self):
      for p in self.powers:
         if self.powers[p].frequency is 'encounter': self.powers[p].setUsed(False)

   def extendedRest(self):
      for p in self.powers: self.powers[p].setUsed(False)

