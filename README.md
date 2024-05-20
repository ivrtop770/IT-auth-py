# Python API Model to OTP Verify.
## first you need to approve you server ip to access to this service.
### plaese contact us.



# To send by WhatsApp
```
from auth import Auth
auth = Auth()  # Create an instance of Auth

# Step 1: send the code by whatsapp
whatsapp = auth.whatsapp("1234567890")  # Replace "1234567890" with the actual phone number
response = whatsapp.send()
print(response)


# Step 2: To verify the code.
response = whatsapp.verify("1234")  # Replace "1234" with the actual code
print(response)
```



# To send a Phone Call (only israel phone numbers)
```
from auth import Auth
auth = Auth()  # Create an instance of Auth

# Step 1: send the code by phone call
call = auth.call("1234567890")  # Replace "1234567890" with the actual phone number
response = call.send()
print(response)



# Step 2: To verify the code
response = call.verify("1234")  # Replace "1234" with the actual code
print(response)
```
