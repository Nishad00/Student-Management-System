class Student(object):
        """
        \n\t\t\t\t\tThis is a Menu Driven Program of Student Management System.\n\n In Which a Class is Created For Storing The Information Like rollno,prn,name,dob,contact in the List By Using Methods like add,delete,search,update,display.\n It also used Constructor and Defined Getter Setter Method.  
        """
        #static variabless
        menu = ' \n_________________________________________MENU FOR STUDENT MANAGEMENT SYSTEM __________________________________________ \n\n\t\t\t\t\t1.Add Student \n\t\t\t\t\t2.Remove Student \n\t\t\t\t\t3.Search Student \n\t\t\t\t\t4.Update Student Data \n\t\t\t\t\t5.Show All Students\n\t\t\t\t\t6.Topper\n\t\t\t\t\t7.Top 3 Student\n\t\t\t\t\t8.Exit '
        no_of_object = 0
        #constructor or init method
        def __init__(self, rollno, prn, name, dob, email, contact):
            
            self.__rollno = rollno
            self.__prn = prn 
            self.__prn = prn 
            self.name = name 
            self.dob = dob 
            self.__email = email
            self.__contact = contact
            Student.no_of_object += 1

        def __str__(self):
            return str(self.rollno)+str(self.prn)+str(self.name)+str(self.dob)+str(self.email)+str(self.contact)


        #getter method
        @property
        def rollno(self):
             return self.__rollno

        @rollno.setter
        def rollno(self,rollno):
            if rollno == "":
                print(" \n\t\t\t\t_______________________________ENTER YOUR VALID ROLL NO PLEASE_________________________________\n  ") 
                rollno = raw_input("Enter Roll No =>  ") 
                self.__rollno = rollno
            elif rollno.isalpha():
                print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                rollno = raw_input("Enter Roll No =>  ") 
                self.__rollno = rollno
            elif int(rollno) < 0:
                print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                rollno = raw_input("Enter Roll No =>  ") 
                self.__rollno = rollno
            else:
                self.__rollno = rollno

            


        @property
        def prn(self):
             return self.__prn
             
        @prn.setter
        def prn(self,prn):
            if prn == "":
                print(" \n\t\t\t\t_______________________________ENTER YOUR PRN PLEASE_________________________________\n  ")
                prn = raw_input("Enter Your PRN =>  ")
                self.__prn = prn
            elif prn.isalpha():
                print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                prn = raw_input("Enter Your PRN =>  ")
                self.__prn = prn
            elif int(prn) < 0:
                print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                prn = raw_input("Enter Your PRN =>  ")
                self.__prn = prn
            else:
                self.__prn = prn 

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self,name):
            if name == "" :
                print(" \n\t\t\t\t_______________________________ENTER YOUR NAME PLEASE_________________________________\n  ")   
                name = raw_input("Enter Your Name =>  ")
                self.__name = name
            elif name.isdigit():
                print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                name = raw_input("Enter Your Name =>  ")
                self.__name = name
            elif len(name) < 2:
                print ("\n\t\t\t\t___________________________________YUOR NAME IS TOO SHORT____________________________________\n")
                name = raw_input("Enter Your Name =>  ")
                self.__name = name
            elif len(name) > 30:
                print ("\n\t\t\t\t___________________________________YOUR NAME IS TOO LARGE _________________________________________\n")
                name = raw_input("Enter Your Name =>  ")
                self.__name = name
            else:
                self.__name = name           
            

        @property
        def dob(self):
            return self.__dob

        @dob.setter
        def dob(self,dob):
            if dob == "":
                print(" \n\t\t\t\t_______________________________ENTER YOUR DOB PLEASE_________________________________\n  ")  
                dob = raw_input("Enter Your Date Of Birth =>  ")
                self.__dob = dob
            elif dob.isalpha():
                print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                dob = raw_input("Enter Your Date Of Birth =>  ")
                self.__dob = dob
            elif "/" not in dob:
                print("\n\t\t\t\t_________________________________ENTER A VALID DATE_________________________________\n")
                dob = raw_input("Enter Your Date Of Birth =>  ")
                self.__dob = dob
            else:
                self.__dob = dob
                    


        @property
        def email(self):
             return self.__email

        @email.setter
        def email(self,email):
            if email == "" :
                print(" \n\t\t\t\t_______________________________ENTER YOUR EMAIL PLEASE_________________________________\n  ")   
                email = raw_input("Enter Your E-MAIL =>  ")
                self.__email = email 
            elif email.isdigit():
                print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                email = raw_input("Enter Your E-MAIL =>  ")
                self.__email = email 
            elif len(email) <= 6:
                print("\n\t\t\t\t_________________________________YOUR EMAIL ADDRESS IS TOO SHORT_________________________________\n")
                email = raw_input("Enter Your E-MAIL =>  ")
                self.__email = email 
            elif "." not in email:
                print("\n\t\t\t\t_________________________________ENTER A VALID EMAIL ADDRESS_________________________________\n")
                email = raw_input("Enter Your E-MAIL =>  ")
                self.__email = email 
            elif "@" not in email:
                print("\n\t\t\t\t_________________________________ENTER A VALID EMAIL ADDRESS_________________________________\n")
                email = raw_input("Enter Your E-MAIL =>  ")
                self.__email = email 
            else:
                self.__email = email

        @property
        def contact(self):
             return self.__contact

        @contact.setter
        def contact(self,contact):
            if contact == "":
                print(" \n\t\t\t\t_______________________________ENTER YOUR CONTACT NO PLEASE_________________________________\n  ")
                contact = raw_input("Enter Your Contact =>  ")
                self.__contact  = contact   
            elif contact.isalpha():
                print ("\n\t\t\t\t___________________________________ENTER VALID INPUT____________________________________\n")
                contact = raw_input("Enter Your Contact =>  ")
                self.__contact  = contact 
            elif int(contact) < 0:
                print ("\n\t\t\t\t___________________________________ENTER POSITIVE NO____________________________________\n")
                contact = raw_input("Enter Your Contact =>  ")
                self.__contact  = contact 
            elif len(contact) != 10:
                print ("\n\t\t\t\t___________________________________ENTER 10 DIGIT MOBILE NO____________________________________\n") 
                contact = raw_input("Enter Your Contact =>  ")
                self.__contact  = contact       
            else:
                self.__contact = contact
            


        # static method for display
        
        def display(self):
            try:
                print("\n_________________________________________________________________________________________________________\n")
                print '\nPRESENT STUDENT NO => ',Student.no_of_object
                print("\n_________________________________________________________________________________________________________\n")
                #print("PRESENT STUDENT =>  ")
                print "Rollno \t\t PRN \t\t NAME \t\t DOB \t\t E-Mail \t\t Contact \n\n\n ",self.rollno," \t\t",self.prn," \t\t",self.name," \t\t",self.dob," \t\t",self.email," \t\t",self.contact
               # print("Rollno =>  " +self.rollno)
               # print("PRN =>   " +self.prn)
               # print("NAME =>  " +self.name ) 
               # print("DOB =>  " +self.dob)
               # print("E-mail =>  " +self.email )
               # print("Contact => " +self.contact)
            except:
                print("error")

        #static method for display
        @staticmethod
        def remove():
            try:
            
                print"\n1.Remove by Rollno \n2.Remove by Prn"
                rchoice = input("\nEnter your Choice =>  ")
         
                if rchoice == 1:
                    removeprn = raw_input("Enter your PRN => ")



                    for i in self:
                
                        if i.prn == removeprn:
                            self.remove(i)

                if rchoice == 2:
                    removeroll = raw_input("Enter your Roll no => ")

                    for i in self:
                
                        if i.rollno == removeroll:
                            self.remove(i)
            except:
                print"________error_________"
        
        @staticmethod
        def Search():
            try:
                print "\n1.Search by Prn \n2.Search by Name \n3.Search by Contact "
                schoice = input("\n Enter your choice =>  ")                

                if schoice == 1:
                    sprn = raw_input("\nEnter the PRN no =>  ")

                    for i in self :
                    
                        if i.prn == sprn :
                            print("\n----------------------------\n")
                            print("\nrollno " +i.rollno)
                            print("prn " +i.prn)
                            print("name " +i.name )
                            print("dob " +i.dob)
                            print("email  " +i.email )
                            print("contact\n " +i.contact)
                            print("\n----------------------------\n")


                if schoice == 2:
                    sname = raw_input("\nEnter the Name of student =>  ")
                
                    for i in self :
                        if i.name == sname :  
                            print("\n----------------------------\n")
                            print("\nROLLNO =>  " +i.rollno)
                            print("PRN =>  " +i.prn)
                            print("NAME =>  " +i.name )
                            print("DOB => " +i.dob)
                            print("EMAIL =>  " +i.email )
                            print("CONTACT =>  " +i.contact)
                            print("\n----------------------------\n")


    

                if schoice == 3:
                    scontact = raw_input(" Enter the Contact Number  of student =>  ")

                    for i in self:

                        if i.contact == scontact:
                            print("\n----------------------------\n")
                            print("\nROLLNO =>  " +i.rollno)
                            print("PRN => " +i.prn)
                            print("NAME => " +i.name )
                            print("DOB => " +i.dob)
                            print("EMAIl =>  " +i.email )
                            print("CONTACT => " +i.contact)
                            print("\n----------------------------\n")
            except:
                print"_____error____" 

        @staticmethod
        def update(self):
            try:

                ustudent = raw_input(" Enter the PRN of student to update =>  ")
            
                for i in self:
                    if i.prn == ustudent:

                        print("\t1.ROLLNO \n\t2.PRN \n\t3.NAME \n\t4.DOB   \n\t5.EMAIL  \n\t6.CONTACT \n")
                        uchoice = input("\nEnter your choice =>  ")
                        if uchoice == 1:
                            uroll = raw_input("Enter New Roll No =>  ")
                            i.rollno = uroll

                        elif uchoice == 2:
                            uprn = raw_input("Enter New PRN No =>  ")
                            i.prn = uprn

                        elif uchoice == 3:
                            uname = raw_input("Enter New Name =>  ")
                            i.name = uname

                        elif uchoice == 4:
                            udob = raw_input("Enter New DOB =>  ")
                            i.dob = udob

                        elif uchoice == 5:
                            uemail = raw_input("Enter New Email =>  ")
                            i.email = uemail
                
                        elif uchoice == 6:
                            unumber = raw_input("Enter New Contact No =>  ")
                            i.contact = unumber
            except:
                         print"______error_______"



        
               



    

                   
    



