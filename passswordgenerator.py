import random

num = "1234567890"
symbols = "!@#$%^&*_-+=/,. "
letters = 'asdfgqwhertyjukilopmnbvczx'
upper = letters.upper()

new_symbol = random.choice(symbols)
rand_num = random.randint(0,9)
new_num = num[rand_num]
new_upper = random.choice(upper)
new_letter = random.choice(letters)
new_passcode=""


rand = int(random.randint(8,15))
new_word =""
for i  in range(rand):
    new_word += random.choice(num + symbols + letters + upper)

new_passcode= [new_letter, new_num, new_symbol, new_upper] + list(new_word)
random.shuffle(new_passcode)

new_passcode = "".join(new_passcode)

print(f"Your password is : {new_passcode}")
