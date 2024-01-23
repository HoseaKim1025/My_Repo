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