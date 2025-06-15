from datetime import datetime

def time():
    agora = datetime.now()
    return agora.strftime('%d/%m/%Y - %H:%M')

def line():
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------')

def smallline():
    print('----------')