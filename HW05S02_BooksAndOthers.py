import time


class Book:
    list_book = []
    def __init__(self, title, authors, publish_year, pages, language, price):
        self.title = title
        self.authors = authors
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price

    def add_book(self):
        book_dict = {"title": [], "authors": [], "publish_year": [], "pages": [], "language": [], "price": []}
        while True:
            self.title = input("Enter Title: ")
            self.authors = input("Enter Author(s): ")
            self.publish_year = input("Enter publish year: ")
            self.pages = input("Enter Number of pages: ")
            self.price = input("Enter Price: ")
            if self.title in book_dict:
                print("Error: Your book title already exist!!!")
            elif self.title == "":
                print("Error: You must Enter at least one character")
            else:
                book_dict["title"].append(self.title)
                book_dict["authors"].append(self.authors)
                book_dict["publish_year"].append(self.publish_year)
                book_dict["pages"].append(self.pages)
                book_dict["price"].append(self.price)
                break
        print(book_dict)





    # def read(self)
    # print(f"You have read {read} more pages from {self.name}. There are {not_read} pages left)
    ##you can not read more than book’s pages.Print a comment about completing the book whenever needed.


    def get_status(self):
        all_pages = self.pages
        read_pages = 0
        remind = all_pages - read_pages
        self.status = (
            "unread"
            if remind == all_pages
            else "reading"
            if remind > 0 and remind != all_pages
            else "finished"
            if remind == 0
            else breakpoint()
        )
        return self.status

    def __str__(self):
        return f" Title : {self.title} \n " \
               f" Author(s): {self.authors} \n" \
               f"Publish Year: {self.publish_year} \n" \
               f"Pages: {self.pages} \n" \
               f"Language: {self.language} \n" \
               f"Price: {self.price}$ "


class Magazine(Book):
    def __init__(self, title, authors, publish_year, pages, language, price, issue):
        super().__init__(title, authors, publish_year, pages, language, price)
        self.issue = issue


class Audiobook(Book):
    def __init__(self, title, authors, publish_year, price, audio_language, time, speaker, book_language):
        """
        :type speaker: basestring
        """
        super().__init__(title, authors, publish_year, price)
        self.audio_language = audio_language
        self.book_language = book_language
        self.speaker = speaker
        self.time = time


class Podcast(Audiobook, Book):
    def __init__(self, title, price, publish_year, language, time, speaker):
        super().__init__(title, price, publish_year, language, time, speaker)








print("***************** Welcome ****************")
name = input("Whant's your name? ")
print(f"********** Hello {name} ************")
print(f"***************** Menu ***************** {time.ctime()}")
print("For Start please add a book in your library")
""" 
    ADD BOOK
"""
add_book = Book()
add_book.add_book()
print("1- View media list: ")
print("2- Check status")
print("3- Sort your bookshelf")
print("4- Add new media")
print("Please select a number: ")




