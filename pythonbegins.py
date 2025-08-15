print('Note : Password must contain numeric values,symbols,capital letter and must have length between 8 to 22!!')
symbols= "!@#$%^ &*+=-_/.,*"
alphas="qertyuiopasdfghjklzxcvbnm".upper()
num = "0134256789"
def pas():
    pw = input("Enter the password : ")
    is_alpha = False
    is_symbol = False
    is_num = False
    for p in pw:
        for s in symbols:
            if p == s:
                is_symbol = True
        for n in num:
            if p == n:
                is_num = True
        for a in alphas:
            if p == a:
                is_alpha = True

    if len(pw)>8 and len(pw) < 22:
        if is_alpha and is_num and is_symbol:
            print('Thanks the password meet the requirement!!')
            print(f'The pasword is {pw}.')
        else:
            print("Either number or symbol or capital letter is missing !!")
            pas()
    else:
        print("Sorry the length of password doesnot meet the criteria , please look above the mentioned Note!!!!")
        pas()
pas()
