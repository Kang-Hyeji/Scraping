import requests
from bs4 import BeautifulSoup

#현재상영작 코드,제목
movie_code_response = requests.get('https://movie.naver.com/movie/running/current.nhn')

movie_code_soup = BeautifulSoup(movie_code_response.text,'html.parser')

movie_list = movie_code_soup.select(
    '#content > .article > .obj_section > .lst_wrap > ul > li'
)
final_movie_data=[]
for movie in movie_list:
    a_tag = movie.select_one('dl>dt>a')
    movie_title=a_tag.contents[0]
    movie_code=a_tag['href']
    movie_code= movie_code.split('?code=')[1]
    
    movie_data ={
        'title': movie_title,
        'code': movie_code
    }
    final_movie_data.append(movie_data)
    print(final_movie_data)


headers = {
    'authority': 'movie.naver.com',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'iframe',
    'referer': 'https://movie.naver.com/movie/bi/mi/point.nhn?code=189069',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=H2MTKRNSTABF6; NRTK=ag#all_gr#0_ma#-2_si#-2_en#-2_sp#-2; ASID=2772192f000001734a96bb1000000062; _fbp=fb.1.1595161176340.904627745; _ga=GA1.1.1658926459.1595161176; _ga_4BKHBFKFK0=GS1.1.1595161175.1.1.1595161235.60; NM_THUMB_PROMOTION_BLOCK=Y; nx_ssl=2; page_uid=UyWb/wp0YihsslQBVydssssstOG-049102; csrf_token=272e8224-30b0-4980-8164-4667dcdaafc6',
}



#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=189069&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false', headers=headers)

#리뷰와 평점가져오기
for movie in final_movie_data:
    movie_code = movie['code']

    params = (
    ('code', movie_code),
    ('type', 'after'),
    ('isActualPointWriteExecute', 'false'),
    ('isMileageSubscriptionAlready', 'false'),
    ('isMileageSubscriptionReject', 'false'),
)

    review_response = requests.get('https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn', headers=headers, params=params)
# print(review_response.text)
   
   
    # REVIEW_URL = f'https://movie.naver.com/movie/bi/mi/basic.nhn?code={movie_code}#tab'
    # review_response = requests.get(REVIEW_URL)
    review_soup = BeautifulSoup(review_response.text,'html.parser')

    review_list = review_soup.select(
        'body > div > div > div.score_result > ul > li'
    )
    print(review_list)