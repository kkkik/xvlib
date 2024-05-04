# My Username :@unpacket
# run it.
import os 
from bs4 import BeautifulSoup as Un;from requests import get as getURI
class Ch:
	def __init__(self,user):
		self.username = user
	def User(user):
		head = {'User-Agent': 'Apple Webkit iOS17 ;','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate, br','Connection': 'keep-alive','Upgrade-Insecure-Requests': '1','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'none','Sec-Fetch-User': '?1','TE': 'trailers'} 
		response = getURI(f'https://fragment.com/username/{user}', headers=head)
		UN = Un(response.content, 'html.parser')
		req = UN.find("meta", property="og:description").get("content")
		if "is taken" in req:
			return 'taken'
		elif "An auction to get the Telegram" in req or "Telegram and secure your ownership" in req or "Check the current availability of" in req or "Secure your name with blockchain in an ecosystem of 700+ million users" in req:
			return 'auction'
		else:
			url=getURI(f'https://t.me/'+user).text
			if 'cdn' or'cdn4' or 'xml+' not in url:
			     	return 'available'
			else:
				return 'banned'