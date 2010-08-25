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

   def updateAbilityMods(self):
      for m in self.abilityMod:
         self.abilityMod[m] = (self.ability[m] - 10)/2 

   def updateSkills(self):
      for s in self.skill:
         self.skill[s].update(self.lvl,self.abilityMod)

