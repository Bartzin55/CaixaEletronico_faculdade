from datetime import datetime, timedelta
import random

def gerarcartao(iduser, senhacartao):
    cvv = f'{random.randint(1, 999):03}' 
    year = datetime.now().year
    
    numerocartao = f'{year}{iduser:012}'
    validade = (datetime.today() + timedelta(days=2920)).strftime('%m/%Y')
    return numerocartao, validade, cvv