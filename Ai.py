import requests,time,sys
def Code(pro)->str:
    headers = {'authority': 'api.aichatos.cloud','accept': 'application/json, text/plain, */*','accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6','content-type': 'application/json','origin': 'https://chat.yqcloud.top','referer': 'https://chat.yqcloud.top/','sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'cross-site','user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'}
    json_data = {'prompt': pro,'userId': '#/chat/1714538755256','network': True,'system': '','withoutContext': False,'stream': False}
    response = requests.post('https://api.aichatos.cloud/api/generateStream', headers=headers, json=json_data).text
    return response
def sprint(text,sleep):
	import sys as n
	for c in text + '':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.3/ 120)
def GPT(dream) -> str:
		cookies = {'cf_clearance': '9._wgKUAhK7e76OvWrsatn_LEgwYb1Va8ItjbLUHt38-1709007585-1.0-AQQxOjOx1J/j6UtGsJeuYVWqh/FFElu2092ICEOhnpzc9ZcA82bL0UY7ECdqJPYdW1O+Cj4BIw+40y855C2TnMU=','_iidt': 'wo9xc9gOavwmVExu7E5CWMCLwiF3qTI+tXBgilO9HOyVgpyrjvfQEYsoSfQS/KJB1wwZ/ztZ6YDmWg==','_vid_t': 'pfX2YWSD/TcfrlwRbjBONA3rn4wG4eoZsadyV5eEPZn0tsaBE4YrD6b+lMal4C9AIQQX61LFs7QYeg=='}
		headers = {'authority': 'koala.sh','accept': 'application/json','accept-language': 'ar-EG,ar;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6','content-type': 'application/json','flag-real-time-data': 'true','origin': 'https://koala.sh','referer': 'https://koala.sh/chat?q=/dream','sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Android"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Linux; Android 14; Aymen_K_n_Y) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Supported With KNY'}
		json_data = {'input': f'/dream {dream}','inputHistory': [],'outputHistory': [],'model': 'gpt-3.5-turbo'}
		r = requests.post('https://koala.sh/api/gpt/', cookies=cookies, headers=headers, json=json_data)
		if r.status_code == 200:
			x = (r.text).split('(')[1].split(')')[0].strip()
			return x
def xvlib():
  log="""
  
  
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⡿⠛⠋⠉⠉⠉⠛⠿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⣶⣦⠀
⢿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠛⠛⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠇
⠈⢹⣿⠉⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⡀⠀⠀⠀⠀⠀⠈⣿⣿⠉⠀
⠀⢸⣿⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⢿⣿⠀⠀
⠀⠘⣿⣧⣤⣤⣤⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢠⣤⣤⣤⣿⡟⠀⠀
⠀⠀⠈⠉⠉⠉⠉⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⢠⣴⣶⣷⣶⣤⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠈⠉⠉⠉⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢠⣿⣿⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣠⣾⣿⣶⣄⣀⣀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠘⣿⣿⣿⣿⣿⣿⡏⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢀⣀⣀⣴⣾⣿⣦⠀
⢻⣿⣿⣿⠟⠛⠛⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⡈⠛⣿⣿⠟⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠘⠛⠛⢿⣿⣿⣿⠃
⠀⠉⠉⠁⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣰⣿⣿⣧⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠉⠉⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⢰⣿⣿⣿⣿⣆⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⣿⠿⠿⠿⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⣉⣉⣉⣉⣉⣉⣀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠸⠿⠿⢿⣷⣄⠀⠀
⠀⢸⣿⠁⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢻⣿⠀⠀
⠀⢸⣿⠀⠀⠀⠀⠀⠀⠘⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀
⣴⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣷⡄
⠻⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⠃
⠀⠈⠉⠀⠀⠀⠀⠀⢀⣴⣶⣦⡀⠀⠀⠀⣠⣿⡇⠀⠀⠀⣠⣾⣿⣦⡀⠀⠀⠀⣿⣧⡀⠀⠀⠀⣤⣶⣶⣄⠀⠀⠀⠀⠀⠈⠉⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠿⠿⠿⠿⠛⠀⠀⠀⠀⣿⣿⣿⣿⡇⠀⠀⠀⠈⠻⠿⠿⠿⠿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
  

This Lib named xvlib and the telegram channel of it : @xvlib you can message developer in : @UNPACKET •""";print(log)
