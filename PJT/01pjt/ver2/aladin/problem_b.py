import json
from pprint import pprint


def book_info(book, categories):

    # book의 카테고리id와 categories의 id가 같으면,
    # book의 카테고리id를 categories의 name으로 변경
    categoryId = book.get('categoryId')
    for i in range(len(categoryId)):
        for j in range(len(categories)):
            if categoryId[i] == categories[j]['id']:
                categoryId[i] = categories[j]['name']

    # book.json 파일에서 원하는 데이터 가져오기
    book_info = {
        'id' : book.get('id'),
        'title' : book.get('title'),
        'author': book.get('author'),
        'priceSales' : book.get('priceSales'),
        'description' : book.get('description'),
        'cover': book.get('cover'),
        'categoryName': categoryId
    }
    return book_info

if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(book_info(book, categories_list))
