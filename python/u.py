import paho.mqtt.client as mqttClient
import time
import ssl

def on_connect(client, userdata, flags, rc):
  
    if rc == 0:
  
        print("Connected to broker")
  
        global Connected                #Use global variable
        Connected = True                #Signal connection 
  
    else:
  
        print("Connection failed")
  
def on_message(client, userdata, message):
    print("Message received: "  + message.payload.decode("utf-8") )
  
Connected = False   #global variable for the state of the connection
  
broker_address= "mqtt.cloud.yandex.net"  #Broker address
port = 8883                         #Broker port
user = "aresmv64htqk8lkmqr61"                    #Connection username
password = "ICLinnocamp2022"            #Connection password
  
client = mqttClient.Client("Python")               #create new instance
client.username_pw_set(user, password=password)    #set username and password
client.on_connect= on_connect                      #attach function to callback
client.on_message= on_message                      #attach function to callback
  
client.tls_set(r"C:\Users\Yowie\Downloads\rootCA.crt", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(True) 
  
client.connect(broker_address, port=port)          #connect to broker
  
client.loop_start()        #start the loop
  
while Connected != True:    #Wait for connection
    time.sleep(0.1)
  
client.subscribe("$devices/are9gnqohp4npug37mbs/events/raw")
  
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    print("exiting")
    client.disconnect()
    client.loop_stop()