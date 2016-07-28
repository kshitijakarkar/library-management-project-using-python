from Media import Media

class Film(Media):
    """docstring for """
    def __init__(self,calln,title_book,subj,director,notess,year):
        Media.__init__(self,calln,title_book,subj,notess)
        self.director = director
        self.year = year


    def display(self):
         #print();
         print( "Media Type :Film");
         print("----------------------");
         print("Call number  :"+self.callno);
         print("Title        :"+self.title);
         print("Subject      :"+self.subjects);
         print("Director     :"+self.director);
         print("Notes        :"+self.notes);
         print("Year         :"+self.year);


def compare_other(self,name):
    if director.find(name)!= -1:
        return True;
    elif year.find(name)!= -1:
        return True;
    elif notes.find(name)!= -1:
       return True;
    else:
       return False;
