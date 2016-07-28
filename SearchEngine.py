from Book import Book
from Film import Film
from Periodic import Periodic
from Video import Video

class SearchEngine:
   def __init__(self):
      self.cardcatalog = [] 
      b = open('book.txt','r')
      for line in b:
         cn = line.split('|')
         calln = cn[0]
         title = cn[1]
         sub = cn[2]
         auth = cn[3]
         desc = cn[4]
         publ = cn[5]
         city = cn[6]
         year = cn[7]
         series = cn[8]
         notes = cn[9]   
         book = Book(calln,title,sub,auth,desc,publ,city,year,series,notes)
         self.cardcatalog.append(book)
      b.close()   
   
      fi = open('film.txt','r')
      for line in fi:
         cn1 = line.split('|')
         calln = cn1[0]
         title = cn1[1]
         sub = cn1[2]
         director = cn1[3]
         notes = cn1[4]
         year = cn1[5]
         film = Film(calln,title,sub,director,notes,year)
         self.cardcatalog.append(film)
      fi.close()
      
      v = open('video.txt','r')
      for line in v:
         cn2 = line.split('|')
         calln = cn2[0]
         title = cn2[1]
         sub = cn2[2]
         desc = cn2[3]
         distributor = cn2[4]
         notes = cn2[5]
         series = cn2[6]
         label = cn2[7]
         video = Video(calln,title,sub,desc,distributor,notes,series,label)
         self.cardcatalog.append(video)
      v.close() 
      
      p = open('periodic.txt','r')
      for line in p:
         cn3 = line.split('|')
         calln = cn3[0]
         title = cn3[1]
         sub = cn3[2]
         auth = cn3[3]
         desc = cn3[4]
         publ = cn3[5]
         phistory = cn3[6]
         series = cn3[7]
         notes = cn3[8]
         related_title = cn3[9]
         othr_form = cn3[10]
         govt_doc = cn3[11]   
         periodic = Periodic(calln,title,sub,auth,desc,publ,phistory,series,notes,related_title,othr_form,govt_doc)
         self.cardcatalog.append(periodic)
      p.close()   
   
    
      

   def search_by_title(self, title):
      result = []
      for i in range(len(self.cardcatalog)):
         answer= self.cardcatalog[i].compare_title(title);
         if answer== True:
            result.append(self.cardcatalog[i]);
      return result
     
   
   def search_by_call_number(self, calln):
      result = []
      for i in range(len(self.cardcatalog)):
         answer= self.cardcatalog[i].compare_call_number(calln);
         if answer== True:
            result.append(self.cardcatalog[i]);
      return result
      
   
   def search_by_subject(self, subject):
      result = []
      for i in range(len(self.cardcatalog)):
         answer= self.cardcatalog[i].compare_subject(subject);
         if answer== True:
            result.append(self.cardcatalog[i]);
      return result
      
   def search_by_other(self, other):
      result = []
      for i in range(len(self.cardcatalog)):
         answer= self.cardcatalog[i].compare_other(other);
         if answer== True:
            result.append(self.cardcatalog[i]);
      return result
   
   
   
