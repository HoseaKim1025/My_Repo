import json
import os

def sorted_cs_books_by_price(books_list, categories_list):
    
    # category id가 컴퓨터 공학 (2721)인 책들 리스트화
    new_books = []
    for book in books_list:
        if str(type(book['categoryId'])) == "<class 'list'>":
            if categories_list[-1]['id'] in book['categoryId']:
                new_books.append(book)
        elif str(type(book['categoryId'])) == "<class 'int'>":
            if book['categoryId'] == categories_list[-1]['id']:
                new_books.append(book)

    # new_books를 priceSales : title 형태로 리스트화하여 priceSales 순으로 정렬
    new_dict = {}
    for new_book in new_books:
        new_dict[f'{new_book["priceSales"]}'] = new_book['title']
    return list(new_dict.values())

if __name__ == '__main__':
    # data/books/ 의 모든 파일 이름을 list화
    file_list = os.listdir('data/books/')
    # 파일 하나씩 오픈해서 books_list에 추가
    books_list = []
    for file in file_list:
        books_json = open(f'data/books/{file}', encoding='utf-8')
        books = json.load(books_json)
        books_list.append(books)
    # 카테고리 파일
    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    print(sorted_cs_books_by_price(books_list, categories_list))