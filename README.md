```
from auth import Auth
auth = Auth()  # Create an instance of Auth
whatsapp = auth.whatsapp("1234567890")  # Replace "1234567890" with the actual phone number

# To send a WhatsApp message
response = whatsapp.send()
print(response)

# To verify a code
response = whatsapp.verify("1234")  # Replace "1234" with the actual code
print(response)
```
