import requests
myurl = "https://api.telegram.org/bot توکن رباتتون /SendMessage?chat_id=ایدی عددی تون&text="
message = input("che befrestam ??")
result = requests.post(myurl+message)
result = result.text
if result.find('{"ok":true,') == -1 :
    print("i cant send message right now")
else:
    print("message sent")
