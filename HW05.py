import time
import sys


class Book:
    # list_book = []

    def __init__(self, title, authors, publish_year, pages, language, price, read_page=0):
        self.title = title
        self.authors = authors
        self.publish_year = publish_year
        self.pages = pages
        self.language = language
        self.price = price
        self.read_page = read_page

    # def read(self)
    # print(f"You have read {read} more pages from {self.name}. There are {not_read} pages left)
    # you can not read more than book’s pages.Print a comment about completing the book whenever needed.

    def get_status(self):
        # all_pages = self.pages

        # read_pages = 0
        remind = self.pages - self.read_page
        # status = (
        #     "unread"
        #     if remind == self.pages:
        #     else "reading":
        #     if 0 < remind < self.pages
        #     else "finished":
        #     if remind == 0
        #     else "Error: Remind can not bigger than all pages"
        # )
        # # return status

        if remind == self.pages:
            return "Completed"
        elif remind == 0:
            return "Unread"
        else:
            return "Reading"

    def percentage(self):
        x = (self.read_page / self.pages) * 100
        return x

    def read(self, input_pages):
        if input_pages + self.read_page == self.pages:
            return 'Completed!'
        elif input_pages + self.read_page > self.pages:
            return 'You Entered more than left pages!'
        else:
            #self.read_page = input_pages
            self.read_page += input_pages
            #self.read_page = self.pages - input_pages
            return f'You have read {self.read_page} pages from {self.title}.\n{self.pages - self.read_page} pages are left.'


    def __str__(self):
        return f"Title : {self.title} \n " \
               f"Author(s): {self.authors} \n" \
               f"Publish Year: {self.publish_year} \n" \
               f"Pages: {self.pages} \n" \
               f"Language: {self.language} \n" \
               f"Price: {self.price}$ "


class Magazine(Book):
    def __init__(self, title, authors, publish_year, pages, language, price, issue, read_page=None):
        super().__init__(title, authors, publish_year, pages, language, price, read_page)
        self.issue = issue


#
#     def __str__(self):
#         pass


# class Audiobook(Book):
#     def __init__(self, title, authors, publish_year, price, audio_language, time, speaker, book_language, page, read_page=None):
#         """
#         :type speaker: basestring
#         """
#         super().__init__(title, authors, publish_year, price, page, read_page)
#         self.audio_language = audio_language
#         self.book_language = book_language
#         self.speaker = speaker
#         self.time = time
#
#     def __str__(self):
#         pass


# class Podcast(Audiobook):
#     def __init__(self, title, price, publish_year, language, time, speaker, read_page=None):
#         super().__init__(title, price, publish_year, language, time, speaker, read_page)
#
#     def __str__(self):
#         pass


def get_data(all_media):
    for data in all_media:
        print(data)




def add_book():

    # if title in book_dict:
    #     print("Error: Your book title already exist!!!")
    # elif title == "":
    #     print("Error: You must Enter at least one character")

    inputs_list = [input("Enter Title: "), input("Enter Author(s): "), int(input("Enter publish year: ")),
                int(input("Enter Number of pages: ")), int(input("Enter Price: ")), input("Enter language: ")]

    return Book(*inputs_list)


#  def add_magazine():
# #
# #         if title in magazine_dict:
# #             print("Error: Your book title already exist!!!")
# #         elif title == "":
# #             print("Error: You must Enter at least one character")
# #         else:
#      inputs_list = [input("Enter Title: "), input("Enter Author(s): "), int(input("Enter publish year: ")),
#                 int(input("Enter Number of pages: ")), int(input("Enter Price: ")), input("Enter language: ")]
#
#     return Magazine(*inputs_list)


# def add_audiobook():

#         if title in audiobook_dict:
#             print("Error: Your book title already exist!!!")
#         elif title == "":
#             print("Error: You must Enter at least one character")
#         else:

#       inputs_list = [input("Enter Title: "), input("Enter Author(s): "), int(input("Enter publish year: ")),
#                 int(input("Enter Number of pages: ")), int(input("Enter Price: ")), input("Enter language: ")]
#
#       return Audiobook(*inputs_list)


# def add_podcast():
#
#         if title in podcast_dict:
#             print("Error: Your book title already exist!!!")
#         elif title == "":
#             print("Error: You must Enter at least one character")
#         else:

#          inputs_list = [input("Enter Title: "), input("Enter Author(s): "), int(input("Enter publish year: ")),
# #                 int(input("Enter Number of pages: ")), int(input("Enter Price: ")), input("Enter language: ")]
# #
# #          return Podcast(*inputs_list)

all_media = []


def menu():
    while True:
        print("1- View media list")
        print("2- Check status")
        print("3- Sort your bookshelf")
        print("4- Add new media")
        print("5- Exit")
        choice = input("Please select a number: ")
        if choice == '1':
            get_data(all_media)
        elif choice == '2':
            pass
            #all_media[0].get_status()
        elif choice == '3':
            pass
        elif choice == '4':
            selection = input("Please Type B for Add new Book, \n"
                              "Type M for Add new Magazine \n"
                              "Type A for Add new Audiobook \n"
                              "Type P for Add new Podcast")
            if selection == "B" or selection == "b":
                all_media.append(add_book())
            elif selection == "M" or selection == "m":
                pass
                #add_magazine()
            elif selection == "A" or selection == "a":
                pass
                #add_audiobook()
            elif selection == "P" or selection == "p":
                pass
                #add_podcast()
        elif choice == '5':
              break
        #     sys.exit()
        # else:
        #     print("You must only choice number 1 to 5")
        #     print("please try again")
        #     menu()


# print("***************** Welcome ****************")
# name = input("Whant's your name? ")
# print(f"********** Hello {name} ************")
# print(f"***************** Menu ***************** {time.ctime()}")
# print("For Start please add a book in your library")
# """
# ADD BOOK
# """
menu()
# # add_book()

# book1 = Book('sa', 'me', 1990, 23, 'e', 4)
# lst = [book1]
# print(lst[0])

# book1 = add_book()
# print(book1)
# book1.read(4)
# #book1.get_status()
# book1.read(2)
# print(book1.get_status())
