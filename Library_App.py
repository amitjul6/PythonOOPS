
class Library:
    def __init__(self,listofbooks):
        self.listbooks=listofbooks
        self.originallist = listofbooks.copy()
            
    def listallbooks(self):
        print("below is the list of books we have in the library: ")
        for book in self.listbooks:
            print(book)
    
    def lendbook(self,thisbook):
        if thisbook in self.listbooks:
            print ("book borrowed: ")
            self.listbooks.remove(thisbook)
        else:
            print ("book not in Library ")
    
    def addbook (self, retbook):
        if (retbook in self.originallist):
            if (retbook not in self.listbooks):
                self.listbooks.append(retbook)
            else:
                print("Book is Already Returned")
            
        else:
            print("invalid book name")
            
class Student:
    def lendbook(self):
        print("Which book you wanna have: ")
        self.thisbook = input()
        return self.thisbook
        
    def returnbook(self):
        print ("which book you wanna return? ")
        self.retbook = input()
        return self.retbook

def main():
    library = Library(["Art of not giving a fuck","Unbroken", "Pepa Pig"])
    student = Student()
    done = False
    while done == False:
        print (" welcome to the Library 2021 ")

        print ("What do you wanna do : \n 1. See all Avaliable books \n 2. Lend a book \n 3. Retuen a book \n 4. Exit")

        userChoice = int(input())

        if userChoice == 1:
            library.listallbooks()

        elif userChoice == 2:
            library.lendbook(student.lendbook())

        elif userChoice == 3:
            library.addbook(student.returnbook())

        elif userChoice == 4:
            break;
    
main()

