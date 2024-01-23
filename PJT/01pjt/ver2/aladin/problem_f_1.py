import json
import os

def best_new_books(books_list):
    # 각 북마다 2023이 pubDate에 포함되면 new_books에 추가
    new_books = []
    for book in books_list:
        if '2023' in book['pubDate']:
            new_books.append(book)
    # new_books 중 평점에 대한 데이터를 rank에 리시트화
    rank = []
    for new_book in new_books:
        rank.append(new_book['customerReviewRank'])
    # 가장 높은 평점을 기록한 new_book의 title을 추출
    best_new_books = new_books[rank.index(max(rank))]['title']
    # best_book의 정보 중 'title'의 value를 반환
    return best_new_books

if __name__ == '__main__':
    # data/books/ 의 모든 파일 이름을 list화
    file_list = os.listdir('data/books/')
    # 파일 하나씩 오픈해서 books_list에 추가
    books_list = []
    for file in file_list:
        books_json = open(f'data/books/{file}', encoding='utf-8')
        books = json.load(books_json)
        books_list.append(books)
    print(best_new_books(books_list))