from converters.book_converter import BookConverters
from models.books_model import *


class BookAPIService:
    def __init__(self):
        
        self.book_conversion_obj = BookConverters()

    def get_book_record(self):
        try:
            final_data = Book.query.all()
            final_response = self.book_conversion_obj.convert_to_get_book(final_response=final_data)
            return final_response
        except Exception as ex:
          
            return ex

    def add_book_record(self,input_data):
        try:
            id = input_data.get('id')
            title=input_data.get('title')
            author=input_data.get('author')
            date_joined = input_data.get('date_joined')
            new_book = Book(id=id,title=title, author=author,
                            date_joined=date_joined)
           
            final_response = self.book_conversion_obj.convert_to_post_book(final_response=new_book)
            return final_response
        except Exception as ex:
           
            return ex
