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