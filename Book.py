from Media import Media

class Book(Media):
   def __init__(self,calln,title_book,subjs,author,descp,publisher,citybook,year,series,notes):
      Media.__init__(self, calln, title_book, subjs, notes)
      self.author = author
      self.descp = descp
      self.publisher = publisher
      self.citybook = citybook
      self.year = year
      self.series = series
      
      
   def display(self):
        print("Media Type : Book")
        print("----------------------")
        print("Call number  :"+ self.callno);
        print("Title        :"+ self.title)
        print("Subject      :"+ self.subjects)
        print("Author       :"+self.author)
        print("Description  :"+self.descp)
        print("Publisher    :"+self.publisher)
        print("City         :"+self.citybook)
        print("Year         :"+self.year)
        print("Series       :"+self.series)
        print("Notes        :"+self.notes)
      
   def compare_other(self,name):
      if self.descp.find(name)!= -1:
         return True;
      elif self.year.find(name)!= -1:
         return True;
      elif self.notes.find(name)!= -1:
         return True;
      else:
         return False;
    
