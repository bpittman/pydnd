class Skill:
   def __init__(self,ability):
      self.trained = False
      self.totalBonus = 0
      self.miscBonus = 0
      self.ability = ability

   def update(self,lvl,mod):
      self.totalBonus = (5 if self.trained else 0) + lvl/2 + mod[self.ability] + self.miscBonus

   def setTrained(self, value):
      self.trained = value

   def value(self):
      return self.totalBonus
