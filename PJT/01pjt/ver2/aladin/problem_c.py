import json
from pprint import pprint

def books_info(books, categories):
    # books의 x번째 정보를 가져와 재조합해 books_info에 하나씩 추가
    books_info = []
    for x in range(len(books)):
        # books의 x번째 카테고리id와 categories의 id가 같으면,
        # books의 x번째 카테고리id를 categories의 name으로 변경
        categoryId = books[x]['categoryId']
        for i in range(len(categoryId)):
            for j in range(len(categories)):
                if categoryId[i] == categories[j]['id']:
                    categoryId[i] = categories[j]['name']

        # books.json 파일에서 원하는 데이터 가져오기
        book_info = {
            'id' : books[x]['id'],
            'title' : books[x]['title'],
            'author': books[x]['author'],
            'priceSales' : books[x]['priceSales'],
            'description' : books[x]['description'],
            'cover': books[x]['cover'],
            'categoryName': categoryId
        }
        books_info.append(book_info)
    
    return books_info

if __name__ == '__main__':
    books_json = open('data/books.json', encoding='utf-8')
    books = json.load(books_json)

    categories_json = open('data/categories.json', encoding='utf-8')
    categories_list = json.load(categories_json)

    pprint(books_info(books, categories_list))
