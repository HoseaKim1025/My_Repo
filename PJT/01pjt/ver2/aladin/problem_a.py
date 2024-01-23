import json
from pprint import pprint

def book_info(book):
    
    # book.json 파일에서 원하는 데이터 가져오기
    book_info = {
        'id' : book.get('id'),
        'title' : book.get('title'),
        'author': book.get('author'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover': book.get('cover'),
        'categoryId': book.get('categoryId')
    }
    return book_info

if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))