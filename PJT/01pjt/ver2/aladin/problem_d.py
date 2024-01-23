import json
import os

def best_book(books_list):
    # 각 북마다 평점 가져와서 rank 리스트에 추가
    rank = []
    for books in books_list:
        rank.append(books['customerReviewRank'])
    # books_list에서 max(rank)의 인덱스에 해당하는 정보를 best_book에 할당 
    best_book = books_list[rank.index(max(rank))]
    # best_book의 정보 중 'title'의 value를 반환
    return best_book['title']

if __name__ == '__main__':
    # data/books/ 의 모든 파일 이름을 list화
    file_list = os.listdir('data/books/')
    # 파일 하나씩 오픈해서 books_list에 추가
    books_list = []
    for file in file_list:
        books_json = open(f'data/books/{file}', encoding='utf-8')
        books = json.load(books_json)
        books_list.append(books)
    print(best_book(books_list))