
# To send a WhatsApp message
```
from auth import Auth
auth = Auth()  # Create an instance of Auth
whatsapp = auth.whatsapp("1234567890")  # Replace "1234567890" with the actual phone number

response = whatsapp.send()
print(response)

# To verify a code By Whatsapp
response = whatsapp.verify("1234")  # Replace "1234" with the actual code
print(response)
```



# To send a Phone Call
```
from auth import Auth
auth = Auth()  # Create an instance of Auth
call = auth.call("1234567890")  # Replace "1234567890" with the actual phone number

response = call.send()
print(response)

# To verify a code By The Phone Call
response = call.verify("1234")  # Replace "1234" with the actual code
print(response)
```
