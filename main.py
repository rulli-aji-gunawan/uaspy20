from core.baseapp import BaseApp
from core.search_helper import *
from view.view_book import *
from view.input_book import *

class MainApp():

    def __init__(self):
        self.books = []

    def run(self):
        MainApp.books = BaseApp()
        return MainApp.books.run()

    def list_book(self):
        # MainApp.books = ViewBook()
        # return MainApp.books.list()
        lBook = ViewBook(self.books)
        return lBook.list()


    def add_book(self):
        aBook = InputBook()
        aBook.input()
        return self.books

    def search_book(self):
        iBook = InputBook()
        iBook.search()
        SH = SearchHelper()
        SH.search_title(self.books)
        VB = ViewBook(self.books)
        VB.list()

    # def run(self):
    #     MainApp.books = BaseApp()
    #     return MainApp.books.run()

if __name__ == "__main__":
    app = MainApp()
    app.run()

