from mody import Mody
import requests

token = Kobra.ELHYBA
tkn = int(token)
chat_id = Kobra.OWNER
urlp = "https://t.me/bb_bb18"
url = f"https://api.telegram.org/bot{tkn}/getChat?chat_id={chat_id}"

req = requests.get(url).json()
print(req)
