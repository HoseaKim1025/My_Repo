import json
import os

def new_books(books_list):
    # 각 북마다 2023이 pubDate에 포함되면 new_books에 추가
    new_books = []
    for book in books_list:
        if '2023' in book['pubDate']:
            new_books.append(book['title'])
    return new_books

if __name__ == '__main__':
    # data/books/ 의 모든 파일 이름을 list화
    file_list = os.listdir('data/books/')
    # 파일 하나씩 오픈해서 books_list에 추가
    books_list = []
    for file in file_list:
        books_json = open(f'data/books/{file}', encoding='utf-8')
        books = json.load(books_json)
        books_list.append(books)
    print(new_books(books_list))