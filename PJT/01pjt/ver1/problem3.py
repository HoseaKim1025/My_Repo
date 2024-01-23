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
