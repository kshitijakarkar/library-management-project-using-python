from SearchEngine import SearchEngine

def main():
   se = SearchEngine()
   results = []
               
   ch = "y"
   
   while(ch=="y"):
      print("Menu\n1.Search by call number\n2.Search by Title\n3.Search by subject\n4.Search by other\n5.exit\n")
      print("Enter search number :")
      choice = input()
      if choice=="1":
         #print("first choice")
         string = input("Enter String :")
         results = se.search_by_call_number(string)
         for count in range(len(results)):
            results[count].display()
         #print(len(results))
         del results[:]       
      elif choice=="2":
         string = input("Enter String :")
         results = se.search_by_title(string)
         for count in range(len(results)):
            results[count].display()
         #print(len(results))
         del results[:]       
      elif choice=="3":
         string = input("Enter String :")
         results = se.search_by_subject(string)
         for count in range(len(results)):
            results[count].display()
         #print(len(results))
         del results[:]       
      elif choice=="4":
         string = input("Enter String :")
         results = se.search_by_other(string)
         for count in range(len(results)):
            results[count].display()
         #print(len(results))
         del results[:]       
      elif choice=="5":
         print("Exited")
         break
      else:
         print("Invalid choice ")
      ch = input("Do you want to continue ?(y/n)")
if __name__ == "__main__":
    main()
    
   
