import requests
from user_agent import generate_user_agent
r=requests.session()




def CPT2():
  global ID
  url = 'https://www.tiktok.com/captcha/verify?lang=en&app_name=Tik_Tok_Login&h5_sdk_version=2.16.47&sdk_version=&iid=0&did=6968310577286661637&device_id=6968310577286661637&ch=web_text&aid=1459&os_type=2&tmp=1623878031197&platform=pc&webdriver=false&fp=verify_1ca8bcd3dbf75db5d781c51f812298ce&type=verify&detail=*WMHWI3-0aZ2wxJzbRW7oyoJO9TdOuv47Krv9UeEZ-OcwN-rCM58Ith8RIihy4d70S-eFWxbNrD61b6703bVX2ZJphx6yE*CLO6SK-*Q-U9mbKl1T358egKTDPrZEfmX2nqjinLS0L7Egv*KgPJt6KHvfhyeZ-hJkcBEUGN53aBMkoeO5PS5AKq5oHwg90J5sbd098WDvUStelxTYOEl1nWv9omqrW3K590EqdFpyfn510X*WuCf6kkHd*4XkMbLfJO3RBY68-yTcFzvtKr2HLGNMHKJBylEs33IM0BcPt4cYhyiMOnaeHF-RoENlYbOLWdO3Sta1tbRKGw82kw7cS5ZW8GSs9UKbBKHaGGhyHKgy0xTd-U8mCCfJydDv1Ib3dRPQxZdP5TDp3n-ZNImJKRdjTT18EarKgu-DOTRWPpgMmvSg1k.&subtype=slide&challenge_code=99999&os_name=windows'
  
  
  headers = {
  'Host': 'www.tiktok.com',
  'Cookie': 'tt_webid_v2=6968310577286661637; tt_webid=6968310577286661637; ttwid=1%7CZzvaIhaLGoGxA3j52jOXiFC8BH-0Jhw_1kGxJs2v8yA%7C1623873248%7Cc529d7ef66ec9dcbc99fa8e46a09a6aa1cae24d5ed31714aecdd9c088f7080a3; MONITOR_WEB_ID=verify_1ca8bcd3dbf75db5d781c51f812298ce; passport_csrf_token=4ede4960536ddce60e3edefdcb9db996; passport_csrf_token_default=4ede4960536ddce60e3edefdcb9db996; tt_csrf_token=tCkiiCkUHTUy9Xu3jHnWZmj7; csrf_session_id=1e3e7af6547d4105a370cfc06a7fc3aa; R6kq3TV7=AA5FOBZ6AQAASXqHR-BUtj4hdjyQZr6-Rw1x7wn8dmToaHMNSacHJ883kB9Q|1|0|8c2f3d024a2cf2321a5910272460626dcd07c0ec; s_v_web_id=verify_1ca8bcd3dbf75db5d781c51f812298ce',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
  'Accept': 'application/json, text/plain, */*',
  'Accept-Language': 'en-US,en;q=0.5',
  'Accept-Encoding': 'gzip, deflate',
  'Content-Type': 'application/json;charset=utf-8',
  'Content-Length': '14893',
  'Origin': 'https://www.tiktok.com',
  'Referer': 'https://www.tiktok.com/login/phone-or-email/email',
  'Te': 'trailers',
  'Connection': 'close'}
  
  
  data = {
  "modified_img_width":'340',
  "id":ID,
  "mode":"slide",
  "reply": # the information,}
  
  go =r.post(url,headers=headers,data=data).text
  print(go)

def CPT1():
  global ID
  url = 'https://www.tiktok.com/captcha/get?lang=en&app_name=Tik_Tok_Login&h5_sdk_version=2.16.44&sdk_version=&iid=0&did=6968316455419430405&device_id=6968316455419430405&ch=web_text&aid=1459&os_type=2&tmp=1623085228541&platform=pc&webdriver=false&fp=verify_5edf3ce125d9831f066e1b48d03591b9&type=verify&detail=H6FaCLwQpWFT1rcXlVL7qCdcks9cZQiJbXIu9JyxXaPTv9A6E3ASXVWxc3PQoADd-t7oqXy*t7JRo2lyqQeVUIuJ1UYFPwFx1I73c*pxLAUr*ZnCF8dmfFa9nMhOkXAD9dd2jRUIB2iU5vzrI4XLYXYlX69DAHz8pO6H5OGdz0m5aRN6ZvP9PMNfp6KRPMMlDjjpcgwYRoTM3AdsAXL3vdIres8fJHhA-ZUCH*2oIDrQ0M0M*phufgl7ydD23oDk5pMKNFew70ljZyx*DmiHKxJhmdFrh-jD77pLW0FuuEVXz*pjdhXbmq5IEfODv05SkosVfDLFNkekIyNASk9buNuPX0DPms*E7zhPkXhrewIXWR77rPDNtmFfp1OiN*zZcuTJw-tw2USE1jwawrXxS*iP9p-u3iwynNhUdqibhiAqEFIZNqY.&subtype=slide&challenge_code=5&os_name=windows'
  
  headers = {
  'accept': 'application/json, text/plain, */*',
  'accept-language': 'en-US,en;q=0.9',
  'cookie': 'tt_webid_v2=6968316455419430405; tt_webid=6968316455419430405; passport_csrf_token=349596cbe84fd0ffe5dbd9340394dca6; passport_csrf_token_default=349596cbe84fd0ffe5dbd9340394dca6; tt_csrf_token=bi9kcuHLorLdotbc50QztjLU; csrf_session_id=618c24fd980d417e89ffcb3a163564da; ttwid=1%7ChE9PNUw9TRoYHFHf1SUq025zx476Rovxl5rjGRoVIM4%7C1623084256%7C775a1c8497980109c5a2feb50db5f70d669b48c3b9e96c397f8be43c65b4d980; R6kq3TV7=AL5NXOd5AQAALCBhcYQu-KGpnWFsfAMQRFH0uXmuRQNliBisqYAeKamJ73y1|1|0|ff08b0564400d83cb3a77f12aa0d9f783e4ff3fb; s_v_web_id=verify_5edf3ce125d9831f066e1b48d03591b9; MONITOR_WEB_ID=verify_5edf3ce125d9831f066e1b48d03591b9',
  'referer': 'https://www.tiktok.com/login/phone-or-email/email',
  'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
  'sec-ch-ua-mobile': '?0',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
  
  
  ok = r.get(url,headers=headers)
  print(ok.text)
  All = ok.json()['data']
  ID = ok.json()['data']['id']
  print(ID)
  CPT2()
  
CPT1()
