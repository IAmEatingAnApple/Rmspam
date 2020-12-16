import requests, random, time
 
setts = {
    "nickname":"def",
    "content":"def"
}
chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
 
a = 1
b = False
nname = ''
msg = ''
 
def rangen():
    global b
    global nname
    global msg
    b = True
    nname = ''
    msg = ''
    for i in range(15):
        nname+=random.choice(chars)
        msg+=random.choice(chars)
    setts["nickname"] = nname
    setts["content"] = msg
 
def login():
    global a
    global nname
    global msg
    global op1
    op1 = int(input('Сколько раз отправить: '))
    op = int(input('0 - Сгенерировать случайные данные. 1 - Ввести свои: '))
    if op == 1:
        nname = input('ник: ')
        msg = input('сообщение: ')
    elif op == 0:
        rangen()
    else:
        exit()
    setts["nickname"] = nname
    setts["content"] = msg
    print(f'Никнейм: {nname}; Сообщение: {msg}.')
    spam()
    
def spam():
    global a
    global b
    global op1
    for i in range(op1):
	    if b == True:
	        rangen()
	    else:
	        pass
	    requests.post('http://rmchat.7m.pl/send.php', data=setts)
	    print(f'{a} сообщение отправлено!')
	    if b == True:
	        print(f'Ник {nname}    Сообщение {msg}')
	    else:
	        pass
	    a+=1
    
login()
