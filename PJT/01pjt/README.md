# PJT 01 - 금융 데이터 수집

### 이번 pjt 를 통해 배운 내용

* 데이터를 서버로부터 Python으로 불러오는 과정에서 API 공식 문서를 참고하는 방법을 익혔다.

* Python으로 데이터를 불러올 때 requests 함수를 import하고 .get, .json을 사용하는 방법을 익혔다.

* 방대한 양의 dict 데이터를 원하는 형식의 데이터로 재조합하여 출력하는 방법을 익혔다.

## 기본 세팅

* [금융상품통합비교공시 API](https://finlife.fss.or.kr/finlife/main/contents.do?menuNo=700029)
  * 정기예금 API 활용

## A. 데이터 추출 - Key 값 출력하기

* 요구 사항
  * 데이터를 json으로 가공한 후 key값만 출력한다.

```python
import pprint
import requests

def get_deposit_products():
  api_key = "95a35bb452f7fc370282e80394b730a1"

  url =  'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
     'auth' : api_key,
     'topFinGrpNo' : '020000',
     'pageNo' : 1
  }
  response = requests.get(url,  params=params).json()
  return response['result'].keys()
    
if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)
```
```
dict_keys(['prdt_div', 'total_count', 'max_page_no', 'now_page_no', 'err_cd', 'err_msg', 'baseList', 'optionList'])
```
* 어려웠던 점
  * url로부터 데이터를 받아오는 방식을 API 공식 문서를 통해 익히는 것이 생소해 조금 해맸지만, 예시로 주어진 사진을 참고해 공식 문서를 읽는 방법을 어느정도 익힐 수 있었다.
  * key : value 구조를 파악하려고 방대한 양의 dict 데이터를 봤을 때 조금 당황했지만, 처음부터 하나하나 읽어보니 복잡한 구조와 양도 조금씩 이해가 됐다.

## B. 데이터 추출 - 전체 정기예금 상품 리스트

* 요구 사항
  * 정기예금 상품 리스트 정보만 출력한다.

```python
import pprint
import requests

def get_deposit_products():
  api_key = "95a35bb452f7fc370282e80394b730a1"

  url =  'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
     'auth' : api_key,
     'topFinGrpNo' : '020000',
     'pageNo' : 1
  }
  response = requests.get(url,  params=params).json()
  return response['result']['baseList']
    
if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)
```
```
[{'dcls_end_day': None,
  'dcls_month': '202312',
  'dcls_strt_day': '20240118',
  'etc_note': '- 가입기간: 1~36개월\n'
              '- 최소가입금액: 1만원 이상\n'
              '- 만기일을 일,월 단위로 자유롭게 선택 가능\n'
              '- 만기해지 시 신규일 당시 영업점과 인터넷 홈페이지에 고시된 계약기간별 금리 적용',
  'fin_co_no': '0010001',
  'fin_co_subm_day': '202401180850',
  'fin_prdt_cd': 'WR0001B',
  'fin_prdt_nm': 'WON플러스예금',
  'join_deny': '1',
  'join_member': '실명의 개인',
  'join_way': '인터넷,스마트폰,전화(텔레뱅킹)',
  'kor_co_nm': '우리은행',
  'max_limit': None,
  'mtrt_int': '만기 후\n'
              '- 1개월이내 : 만기시점약정이율×50%\n'
              '- 1개월초과 6개월이내: 만기시점약정이율×30%\n'
              '- 6개월초과 : 만기시점약정이율×20%\n'
              '\n'
              '※ 만기시점 약정이율 : 일반정기예금 금리',
  'spcl_cnd': '해당사항 없음'},

  ...
```

## C. 데이터 가공 - 전체 정기예금 옵션 리스트

* 요구 사항
  * 정기예금 상품들의 옵션 리스트에서 원하는 데이터만 추출해 원하는 형태로 출력한다.

```python
import pprint
import requests

def get_deposit_products():
  api_key = "95a35bb452f7fc370282e80394b730a1"

  url =  'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
  params = {
     'auth' : api_key,
     'topFinGrpNo' : '020000',
     'pageNo' : 1
  }
  response = requests.get(url,  params=params).json()
  result = []
  new_dict = {}
  # 금융상품코드 = fin_prdt_cd
  # 저축 금리 = intr_rate
  # 저축 기간 = save_trm
  # 저축금리유형 = intr_rate_type
  # 저축금리유형명 = intr_rate_type_nm
  # 최고 우대금리 = intr_rate2
  for i in range(len(response['result']['optionList'])):
    new_dict['금융상품코드'] = response['result']['optionList'][i]['fin_prdt_cd']
    new_dict['저축 금리'] = response['result']['optionList'][i]['intr_rate']
    new_dict['저축 기간'] = response['result']['optionList'][i]['save_trm']
    new_dict['저축금리유형'] = response['result']['optionList'][i]['intr_rate_type']
    new_dict['저축금리유형명'] = response['result']['optionList'][i]['intr_rate_type_nm']
    new_dict['최고 우대금리'] = response['result']['optionList'][i]['intr_rate2']
    result.append(new_dict)
  return result
    
if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)
```
```
[{'금융상품코드': '1001202000002',
  '저축 금리': 3.5,
  '저축 기간': '6',
  '저축금리유형': 'S',
  '저축금리유형명': '단리',
  '최고 우대금리': 3.5},

  ...
```
* 어려웠던 점
  * 원하는 key에만 접근해서 value를 가져온 후 key 이름을 원하는 대로 바꿔 다시 리스트를 만드는 과정이 어려웠다. 맞는 방식인지는 모르겠지만 반복문으로 해당 딕셔너리에서 value를 가져온 후 새로운 이름의 key에 할당하여 요구사항을 충족했다. 


## D. 데이터 가공 - 새로운 값을 만들어 반환하기

* 요구사항
  * 상품과 옵션 정보들을 담고 있는 새로운 값을 만들어 딕셔너리 형태로 반환한다.
  * 코드가 일치하는 상품들은 하나로 묶는다.

```python
import pprint
import requests

def get_deposit_products():
    api_key = "95a35bb452f7fc370282e80394b730a1"

    url =  'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }
    response = requests.get(url,  params=params).json()
    
    code_base = []
    code_opt = {}
    opt_dict_list = []
    result = []
    
    for x in range(len(response['result']['optionList'])):
        code_opt[x] = response['result']['optionList'][x]['fin_prdt_cd']
        opt_dict_list.append({
        '저축 금리' : response['result']['optionList'][x]['intr_rate'],
        '저축 기간' : response['result']['optionList'][x]['save_trm'],
        '저축금리유형' : response['result']['optionList'][x]['intr_rate_type'],
        '저축금리유형명' : response['result']['optionList'][x]['intr_rate_type_nm'],
        '최고 우대금리' : response['result']['optionList'][x]['intr_rate2']
        })

    for i in range(len(response['result']['baseList'])):
        code_base.append(response['result']['baseList'][i]['fin_prdt_cd'])
        rate_list = []
        for j in range(len(code_opt)):
            if code_base[i] == code_opt[j]:
                rate_list.append(opt_dict_list[j])
        result.append({
        '금리 정보' : rate_list,
        '금융상품명' : response['result']['baseList'][i]['fin_prdt_nm'],
        '금융회사명' : response['result']['baseList'][i]['kor_co_nm']
        })
    return result

if __name__ == '__main__':
    result = get_deposit_products()
    pprint.pprint(result)
```
```
[{'금리 정보': [{'저축 금리': 3,
             '저축 기간': '1',
             '저축금리유형': 'S',
             '저축금리유형명': '단리',
             '최고 우대금리': 3},
            {'저축 금리': 3.6,
             '저축 기간': '3',
             '저축금리유형': 'S',
             '저축금리유형명': '단리',
             '최고 우대금리': 3.6},
            {'저축 금리': 3.6,
             '저축 기간': '6',
             '저축금리유형': 'S',
             '저축금리유형명': '단리',
             '최고 우대금리': 3.6},
            {'저축 금리': 3.55,
             '저축 기간': '12',
             '저축금리유형': 'S',
             '저축금리유형명': '단리',
             '최고 우대금리': 3.55},
            {'저축 금리': 3,
             '저축 기간': '24',
             '저축금리유형': 'S',
             '저축금리유형명': '단리',
             '최고 우대금리': 3},
            {'저축 금리': 3,
             '저축 기간': '36',
             '저축금리유형': 'S',
             '저축금리유형명': '단리',
             '최고 우대금리': 3}],
  '금융상품명': 'WON플러스예금',
  '금융회사명': '우리은행'},

...
```
* 어려웠던 점
  * 두 데이터를 수집해 하나의 딕셔너리로 만드는 과정을 두 번의 반복문으로 해결했다. 하지만, 코드가 일치하는 상품들을 리스트로 묶는 구조를 만드는 것이 너무 어려웠다. 과정에서 얕은 복사로 인해 리스트가 원하는 대로 append 되지 않는 시행착오도 겪었지만 결국 처음부터 다시 구조를 짜면서 해결되었다.

# 후기

C까지 풀었을 때가 오전이라 금방 하겠구나 싶었지만, D를 풀고나니 5시였다. 

구조를 만드는 아이디어는 충족됐던 것 같은데 문법적으로 구현하는 데 있어서 시행착오가 많이 있었다. 

하지만 데이터를 복잡하게 조합해보는 경험이 앞으로 큰 도움이 될 것 같다.