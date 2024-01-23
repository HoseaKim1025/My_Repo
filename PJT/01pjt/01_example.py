# 데이터를 가져오는 파이썬 라이브러리(패키지) : requests
# 파이썬 패키지 관리 : pip
    # 설치 : pip install <패키지이름>
    # 목록 확인 : pip list
# 내 코드에 다른 패키지 추가 : import <이름>

import requests
import pprint

# url = 'https://fakestoreapi.com/carts'
# .get() : 서버에 데이터 요청, 
# .json() 데이터를 딕셔너리로 변환 (js object notation, 자바스크립트 객체 표기법) (면접 시 주의 : 통신방법이나 프로그래밍 문법이 아니라 단순히 데이터를 표현하는 방법 중 하나임)
# print(data)


# 오픈 api는 공식 문서의 일일 및 월간 사용량 제한을 반드시 확인!
# weather api key : 7df3344c668299d1c0b61225ff5f058b

api_key = '87246d75e1ce26e1392a087b3d1d88c5' # 강사님 api key
# api_key = '7df3344c668299d1c0b61225ff5f058b'
# 서울의 위도와 경도
lat = 37.56
lon = 126.97

url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'
data = requests.get(url).json() 
# pprint.pprint(data)

# 날씨 요약 정보 : 서울 기준 'clear sky'가 출력되도록 해보자!
pprint.pprint(data['weather'][0]['description'])

# 추가 공부 과제 (도전 과제에서 이 부분 고민해서 진행해볼 것)
# data['weather'] 와 data.get('weather') 의 차이는 무엇일까?