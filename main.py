print("Rodando main.py")
import urequests

from machine import Pin,PWM, ADC
from time import sleep

import ConnectWifi

api_key = 'minha_chave'
request_headers = {'Content-Type': 'application/json'}

global led  # led para acusar conexao com WiFi... global para ser usada em modulo de conexao WiFi
led = Pin(15, Pin.OUT)
led.value(0)

adc = ADC(Pin(34))  # Pino para leitura do led receptor infravermelho
adc.atten(ADC.ATTN_11DB)

led_adc = Pin(2, Pin.OUT)  # Led usado para testar limiares de tensao da leitura ADC sem necessitar da planilha escrita atraves do IFTTT
led_adc.value(0)

ledi = PWM(Pin(22))  # Led infravermelho recebendo sinal PWM
ledi.freq(40000)  # frequencia de 40kHz para eliminar influencia de outras fontes de luz durante modulacao/demodulacao
ledi.duty(512)  #duty cycle de 50%


ConnectWifi.connect()

while(True):
    valor1 = adc.read()  # lendo conversor AD
    if valor1 >= 300:  # limiar obtido empiricamente para indicar abertura da porta
        print(valor1)  # usado para obter limiar em testes
        led_adc.value(1)  # indica que porta esta aberta
        request = urequests.post(
            'url_ifttt_com_minha_chave',
            json = {'value1':1},
            headers = request_headers)
        print(request.text)
        request.close()
        while valor1 >=5:  # limiar obtido empiricamente para detectar que porta foi fechada e evitar oscilacoes
            valor1 = adc.read()  # atualizando leitura
            sleep(0.25)   # Delay para minimizar resposta a oscilacoes
        print(valor1)  # usado para entendimento do funcionamento durante testes
        sleep(2)  # Delay para minimizar resposta a oscilacoes quando aporta treme ao fechar
        led_adc.value(0)  # indica que porta esta fechada
    sleep(0.25) # Delay para minimizar resposta a oscilacoes


