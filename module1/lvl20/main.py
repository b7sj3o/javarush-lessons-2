import http.client
import json


# conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
#
#
# conn.request("GET", "/posts/1")
#
# response = conn.getresponse()
# print(response.status, response.reason)
#
# data = response.read().decode('utf-8')
# print(data)
#
# conn.close()


# data = {
#     "title": "Привіт!",
#     "body": "bar",
#     "userId": 1
# }
# payload = json.dumps(data, ensure_ascii=False).encode("utf-8")
#
# headers = {
#     'Content-Type': 'application/json; charset=utf-8'
# }
#
#
# conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")
#
# conn.request("POST", "/posts", body=payload, headers=headers)
#
# response = conn.getresponse()
# print(response.status, response.reason)
#
# data = response.read().decode('utf-8')
# print(data)
#
# conn.close()


from email.message import EmailMessage

msg = EmailMessage()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'Привіт'          # кодування заголовка — автоматично
msg.set_content('Тіло листа українською')

with smtplib.SMTP(smtp_server, 587, timeout=10) as server:
    server.starttls()
    server.login(username, password)
    server.send_message(msg)        # не sendmail