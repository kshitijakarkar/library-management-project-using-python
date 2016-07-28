class Media:
   def __init__(self,callno,title,subjects,notes):
      self.callno = callno
      self.title = title
      self.subjects = subjects
      self.notes = notes
      
   def compare_title(self,value):
      return value in self.title
      
   def compare_call_number(self,value):
      return value in self.callno
      
   def compare_subject(self,value):
      return value in self.subjects
      
   def compare_other(self,value):
      return False
   
   def display(self):
      pass
