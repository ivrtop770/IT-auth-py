import requests
import json

class Auth:
    def __init__(self):
        self.base_url = "https://auth.ivrtop.co.il/"

    def whatsapp(self, phone):
        class Whatsapp:
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

        return Whatsapp(phone, self.base_url)