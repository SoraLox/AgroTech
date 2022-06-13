import paho.mqtt.client as mqttClient
import time
import ssl


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        # succes connection
        global Connected
        Connected = True
    else:
        print("Connection failed")
  
def on_message(client, userdata, message):
    f = open('jsondata.txt', 'w+')
    
    print("Message received: "  + message.payload.decode("utf-8") )
    
    f.write(str(message.payload.decode("utf-8")))
    f.close()
    # file has been updated
    
Connected = False
  
broker_address= "mqtt.cloud.yandex.net"
port = 8883
icluser = "aresmv64htqk8lkmqr61"
iclinno = "ICLinnocamp2022"

client = mqttClient.Client("Python")
client.username_pw_set(icluser, iclinno=iclinno)
client.on_connect= on_connect
client.on_message= on_message
  
client.tls_set(r"C:\Users\Yowie\Downloads\rootCA.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True) 
  
client.connect(broker_address, port=port)

client.loop_start()
  
while Connected != True:
    time.sleep(0.1)
  
client.subscribe("$devices/are9gnqohp4npug37mbs/events/raw")
  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()
    