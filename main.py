import requests
from time import sleep

url = 'http://transito.gtrans.com.br/cttupe/index.php/portal/getImg/192.168.10.105/'


count = 225
while True:
    response = requests.get(url)
    with open(f'./images/imagem_{count}.png', 'wb') as file:
        file.write(response.content)
    print(f'imagem_{count}.png criada')
    count += 1
    sleep(180)
