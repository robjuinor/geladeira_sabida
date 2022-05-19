# modulo e funcao usados para conectar ao meu WiFi:
def connect():
    print("Comecou: connect")
    import network
    
    from main import led  # led aceso quando ele esta conectado ao WiFi
    
    ssid = "meu_ssid"
    password =  "minha_senha"
       
    station = network.WLAN(network.STA_IF)
 
    if station.isconnected() == True:
        print("Already connected")
        return
 
    station.active(True)
    station.connect(ssid, password)
 
    while station.isconnected() == False:
        pass
 
    print("Connection successful")
    led.value(1)
    print(station.ifconfig())