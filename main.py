print("Rodando main.py")
import urequests

from machine import Pin


import ConnectWifi

api_key = 'minha_chave'  # Chave para o webhook
request_headers = {'Content-Type': 'application/json'}

global led  # led para indicar conexao WiFi bem sucedida
#led = Pin(15, Pin.OUT)
#led.value(0)
led = Pin(15, Pin.OUT)
botao = Pin(23, Pin.IN)  # botao usado para testar webhook
led_botao = Pin(2, Pin.OUT)  # led para indicar estado do botao
led_botao.value(0)

led.value(0)
ConnectWifi.connect()

while(True):
    logic_state = botao.value()
    if logic_state == True:  # se botao foi apertado
        led_botao.value(1)
        request = urequests.post(  # realiza webhook
            'url_ifttt_com_minha_chave',
            json = {'value1':1},
            headers = request_headers)
        print(request.text)
        request.close()
        while logic_state == True:  # posso segurar o botao sem efeitos adversos
            logic_state = botao.value()
        led_botao.value(0)









