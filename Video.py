from Media import Media

class Video(Media):
   def __init__(self, calln,title_book,subj,descp,distri,notess,seriess,label):
       Media.__init__(self,calln,title_book,subj,notess)
       self.descp = descp
       self.distri = distri
       self.seriess = seriess
       self.label = label
       

   def display(self):
       print("Media Type  : Video");
       print("----------------------");
       print("Call number  :"+ self.callno );
       print("Title        :"+ self.title );
       print("Subject      :"+ self.subjects );
       print("Description  :"+self.descp);
       print("Distributor  :"+self.distri);
       print("Notes        :"+self.notes);
       print("Label        :"+self.label);
       print("Series       :"+self.seriess);


   def compare_other(self,s):
       if self.descp.find(s)!= -1:
            return True
       elif self.distri.find(s) != -1:
            return True
       elif self.notes.find(s) != -1:
            return True
       else:
            return False
