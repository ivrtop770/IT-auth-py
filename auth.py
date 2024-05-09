import requests
import json

class Auth:
    def __init__(self):
        self.base_url = "https://auth.ivrtop.co.il/"

    def whatsapp(self, phone):
        class WhatsApp:
            def __init__(self, phone, base_url):
                self.phone = phone
                self.base_url = base_url

            def send(self):
                response = requests.get(self.base_url + "whatsapp/" + self.phone)
                return response.json()

            def verify(self, code):
                headers = {'Content-Type': 'application/json'}
                data = json.dumps({'code': code})
                response = requests.post(self.base_url + "whatsapp/" + self.phone, headers=headers, data=data)
                return response.json()

        return WhatsApp(phone, self.base_url)

    def call(self, phone):
        class Call:
            def __init__(self, phone, base_url):
                self.phone = phone
                self.base_url = base_url

            def send(self):
                response = requests.get(self.base_url + "call/" + self.phone)
                return response.json()

            def verify(self, code):
                headers = {'Content-Type': 'application/json'}
                data = json.dumps({'code': code})
                response = requests.post(self.base_url + "call/" + self.phone, headers=headers, data=data)
                return response.json()

        return Call(phone, self.base_url)
