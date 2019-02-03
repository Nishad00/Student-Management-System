from s7 import Student


class Marks(Student):
    
    top1={"name":"","marks":0}
    top2={"name":"","marks":0}
    top3={"name":"","marks":0}

    def __init__(self, rollno, prn, name, dob, email, contact, dicti):
            Student.__init__(self,prn, rollno, name, dob, email, contact)
            #self.__dicti={"OOT":oot,"CNT":cnt}
            self.__dicti = dicti
            self.total = int(self.dicti.get("OOT"))+int(self.dicti.get("CNT"))

    def __str__(self):
                return str(self.rollno)+"\t"+str(self.prn)+"\t"+str(self.name)+"\t"+str(self.dob)+"\t"+str(self.email)+"\t"+str(self.contact)+"\t"+str(self.dicti)

               
    @property 
    def dicti(self):
        return self.__dicti

    
   # def display(self):
       
    #    print("\n----------------------------------MARKS--------------------------------------------- ")
     #    o = int(self.dicti.get("OOT"))
     #   c = int(self.dicti.get("CNT"))
      #  total = o + c
       # print("OOT: "+str(o))
        
        #print("CNT: "+str(c))
       # print("Total: "+str(total))

    
    def display(self):
        Student.display(i)        


        print("\n----------------------------------MARKS---------------------------------------------\n")
        gradeoot = "F"
        gradepcnt = "F" 
        o = int(self.dicti.get("OOT"))
        if o >= 75 and o <= 100:
                gradeoot = "A"
        elif o >= 65 and o <= 74:
                gradeoot = "B"
        elif o >= 55 and o <= 64:
                gradeoot = "C" 
        elif o >= 45 and o <= 54:
                gradeoot = "D"
        elif o < 40:
                gradeoot = "F"  
                

        c = int(self.dicti.get("CNT"))
        if c >= 75 and c <= 100:
                gradecnt = "A"
        elif c >= 65 and c <= 74:
                gradecnt = "B"
        elif c >= 55 and c <= 64:
                gradecnt = "C" 
        elif c >= 45 and c <= 54:
                gradecnt = "D"
        elif c < 40:
                gradecnt= "F"  
        
        total = o + c
        percentage = total / 2

        p = percentage
        gradep = "F"
        if p >= 75 and p <= 100:
                gradep = "A"
        elif p  >= 65 and p <= 74:
                gradep = "B"
        elif p >= 55 and p <= 64:
                gradep = "C" 
        elif p >= 45 and p <= 54:
                gradep = "D"
        elif p < 40:
                gradep = "F"  
        
                
        print("Subject\t\tMarks\t\tGrade\n\n")
        print(" OOT\t\t "+str(o)+"\t\t "+gradeoot)
        print(" CNT\t\t "+str(c)+"\t\t "+gradecnt)
        print("\nTotal: "+str(total)+"\t\t  Percentage: "+str(percentage)+" %"+"\t\t Grade = "+str(gradep))

    @staticmethod 
    def ldisplay():
        f = open('file2.txt','r')
        for i in list1:
                a = f.readline()
                list2.append(a)


        for i in list1:
                print "\n\n\n__________________________________Data Read From File_________________________________________________\n\n"
                print i

        

        



    @staticmethod
    def topper(list1):
       Marks.top1={"name":"","marks":0}
       for obj in list1:
           if (Marks.top1.get("marks") < obj.total):
               updated={"name":obj.name,"marks":obj.total}
               Marks.top1.update(updated)
       print'Topper of the class is :'+str(Marks.top1.get("name"))+' get :'+str(Marks.top1.get("marks"))
           
    @staticmethod
    def topth(list1):
        top_3=[]
        for s in list1:
            t=int(s.dicti.get("CNT")) + int(s.dicti.get("OOT"))
            top_3.append(t)
            print top_3
            l=len(top_3)
            for j in range(0,l-1):
                for i in range(0,l-1):
                    if (top_3[i]>top_3[i+1]):
                        temp=top_3[i]
                        top_3[i]=top_3[i+1]
                        top_3[i+1]=temp
                        print top_3
            l=len(top_3)-1
            print ("The 3 Topper of class is:",top_3[l],top_3[l-1],top_3[l-2])
                
       
                                   


        
    #def __del__():
     #   print("Distructor Called")

     
def add():
        tst = input("\n Enter no of Students you want to add =>  ")
         

        for i in range(tst):
           choice2 = 1
           while choice2 == 1:
                   rollno =raw_input("     Enter Your Roll Number =>   ")
                   if rollno == "":
                        print(" \n\t\t\t\t_______________________________ENTER YOUR ROLL NO PLEASE_________________________________\n  ")  
                   elif rollno.isalpha():
                        print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                   elif int(rollno) < 0:
                        print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                   else:
                        choice2 = 0

          

           choice2 = 1
           while choice2 == 1:
                prn = raw_input("     Enter your PRN no =>  ")
                if prn == "":
                        print(" \n\t\t\t\t_______________________________ENTER YOUR PRN PLEASE_________________________________\n  ")  
                elif prn.isalpha():
                        print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                elif int(prn) < 0:
                        print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                else:
                        choice2 = 0



           choice2 = 1
           while choice2 == 1:
                name = raw_input("     Enter your Name =>  ")
                if name == "" :
                        print(" \n\t\t\t\t_______________________________ENTER YOUR NAME PLEASE_________________________________\n  ")    
                elif name.isdigit():
                        print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                elif len(name) < 2:
                        print ("\n\t\t\t\t___________________________________YUOR NAME IS TOO SHORT____________________________________\n")
                elif len(name) > 30:
                        print ("\n\t\t\t\t___________________________________YOUR NAME IS TOO LARGE _________________________________________\n")
                else:
                        choice2 = 0


           choice2 = 1
           while choice2 == 1:
                dob =   raw_input("     Enter your Date of birth DD/MM/YY   =>  ")
                if dob == "":
                        print(" \n\t\t\t\t_______________________________ENTER YOUR DOB PLEASE_________________________________\n  ")  
                elif dob.isalpha():
                        print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                #elif int(dob) < 0:
                 #       print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                elif "/" not in dob:
                     print("\n\t\t\t\t_________________________________ENTER A VALID DATE_________________________________\n")
                
                else:
                        choice2 = 0


           choice2 = 1
           while choice2 == 1:
                email = raw_input("     Enter your E-mail Address =>  ")
                if email == "" :
                        print(" \n\t\t\t\t_______________________________ENTER YOUR EMAIL PLEASE_________________________________\n  ")    
                elif email.isdigit():
                        print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                elif len(email) <= 6:
                    print("\n\t\t\t\t_________________________________YOUR EMAIL ADDRESS IS TOO SHORT_________________________________\n")
                elif "." not in email:
                     print("\n\t\t\t\t_________________________________ENTER A VALID EMAIL ADDRESS_________________________________\n")
                elif "@" not in email:
                     print("\n\t\t\t\t_________________________________ENTER A VALID EMAIL ADDRESS_________________________________\n")
                else:
                        choice2 = 0



           choice2 = 1
           while choice2 == 1:
                contact = raw_input("     Enter your Contact Number : ")
                if contact == "":
                    print(" \n\t\t\t\t_______________________________ENTER YOUR CONTACT NO PLEASE_________________________________\n  ")  
                elif contact.isalpha():
                    print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                elif int(contact) < 0:
                    print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                elif len(contact) != 10:
                    print ("\n\t\t\t\t___________________________________ENTER 10 DIGIT MOBILE NO____________________________________\n")       
                else:
                    choice2 = 0

           choice2 = 1
           while choice2 == 1:
                oot = raw_input("     Enter your OOT MARKS no =>  ")
                if oot == "":
                        print(" \n\t\t\t\t_______________________________ENTER YOUR OOT MARKS PLEASE_________________________________\n  ")  
                elif oot.isalpha():
                        print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                elif int(oot) < 0:
                        print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                elif int(oot) > 100:
                    print ("\n\t\t\t\t___________________________________ENTER A VALID MARKS____________________________________\n")
                    
                else:
                        choice2 = 0

           choice2 = 1
           while choice2 == 1:
                cnt = raw_input("     Enter your CNT MARKS no =>  ")
                if cnt == "":
                        print(" \n\t\t\t\t_______________________________ENTER YOUR CNT MARKS PLEASE_________________________________\n  ")  
                elif cnt.isalpha():
                        print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                elif int(cnt) < 0:
                        print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                elif int(cnt) > 100:
                        print ("\n\t\t\t\t___________________________________ENTER A VALID MARKS____________________________________\n")
                else:
                        choice2 = 0
                        



           print "\n"
           dicti={"OOT":int(oot),"CNT":int(cnt)}
 
           list1.append(Marks(rollno,prn,name,dob,email,contact,dicti))
           f = open('file2.txt','a')
           for i in list1:
                 f.write(str(i))
                 f.write("\n")

           
                 
           


list1 = []
list2 = []
choice = 0
d = Marks
print(Student.__doc__)
ddii = {"Top1":0, "Top2":0, "TOP3":0 }

while choice != 8:
    
    print "\n\n\n=========================================================================================================================================="
    print d.menu
    print "=========================================================================================================================================="
    
    choice3 = 1
    while choice3 == 1:      
        choice2 = raw_input("Enter your choice =>  ")      
        if choice2== "":
             print(" \n\t\t\t\t_______________________________ENTER YOUR CHOICE PLEASE_________________________________\n  ")
           
        elif choice2.isalpha():
             print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n") 
           
        elif int(choice2) < 0 :
            print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")

        elif int(choice2) > 8:
            print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")          

        else:   
            choice = int(choice2)  
            choice3 = 0    
       
            
                  
    if(choice == 1):
        add()
        
         

    elif(choice == 5):
        for i in list1:
            i.display()            
            #Marks.marksdisplay(i)

        Marks.ldisplay()

    elif(choice == 6):
            Marks.topper(list1)

    elif(choice == 7):
        for i in list1:
            Marks.topth(i)

   
    elif(choice == 2):
         d.remove(list1)


    elif(choice == 3):
        d.Search(list1)

        
    elif(choice == 4):
        d.update(list1)
        print "__________________________________________File Sucessfully Updated_________________________________________"
       
       # for i in list1:
        #         f.write(str(i))