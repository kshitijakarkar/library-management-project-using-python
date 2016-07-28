from Media import Media

class Periodic(Media):
    """docstring for """
    def __init__(self, calln,title_book,subj,author,descp,publisher,history,seriess,notess,relat_title,othr,gvt):
        Media.__init__(self,calln,title_book,subj,notess)
        self.author = author
        self.descp = descp
        self.publisher =publisher
        self.history = history
        self.seriess = seriess
        self.relat_title = relat_title
        self.othr = othr
        self.gvt =gvt


    def display(self):
         print( "Media Type         :Periodic");
         print("--------------------------------");
         print("Call number          :"+ self.callno );
         print("Title                :"+ self.title );
         print("Subject              :"+ self.subjects );
         print("Author               :"+ self.author);
         print("Description          :"+ self.descp);
         print("Publisher            :"+ self.publisher);
         print("Publisher history    :"+ self.history);
         print("Series               :"+ self.seriess);
         print("Notes                :"+ self.notes);
         print("Related titles       :"+ self.relat_title);
         print("Other forms of title :"+ self.othr);
         print("Govt doc number      :"+ self.gvt);


    def compare_other(self,name):
         if self.descp.find(name)!= -1:
            return True;
         elif self.seriess.find(name)!= -1:
            return True;
         elif self.relat_title.find(name)!= -1:
            return True;
         elif self.notes.find(name)!= -1:
            return True;
         else:
            return False;
