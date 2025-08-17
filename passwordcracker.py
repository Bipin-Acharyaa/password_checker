import random
password = '123'
chars = '1234567890!@$#$%^&*()_+=/,.| qawsdefrgthyjukilopmznxbcvZAQXSWCDEVFRBGTNHYMJUKILOP'
e = ""

while e!= password:
    e = "".join(random.choice(chars) for i in range(len(password)))
print(f'The passcode is {e}')
