books=[]
while True:
    print("LIBRARY MANAGEMENT SYSTEM")
    print("1=add books")
    print("2=search books")
    print("3=remove books")
    print("4=display avilable books")
    print("5=exit")
    choice=int(input("enter your choice 1-5:"))
    if(choice==1):
        book=input("enter book name:")
        books.append(book)
        print("book added succesfully")
    elif(choice==2):
        book=input("enter the book to be searched:")
        if(book in books):
            print("book found!")
        else:
            print("not found")
    elif(choice==3):
        book=input("enter book to be remmoved:")
        if (books in book):
            books.remove(book)
            print("book removed")
        else:
            print("book not removed")
    elif(choice==4):
        if len(books)==0:
            print("no book avilable")
        else:
            print("books are avilable")
            for b in books:
                print("-",b)
    elif(choice==5):
        print("exiting program")
        break
    else:
        print("invalid choice")
        