import paho.mqtt.client as mqtt


BROKER_IP = "140.112.18.2"
PORT = 11053
LAG_TIME = 600
TOPIC = "device"

def on_connect(client, userdata, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(TOPIC+'/#')

def on_message(client, userdata, msg):
    # Do something
    from .models import TestData
    topic_r = str(msg.topic)
    msg_r = str(msg.payload)
    device_set = msg_r.split(",")
    for d in device_set:
        print (d)
    all_test = TestData.objects.all()
    print ("length", len(all_test))
    testdata = TestData()
    testdata.host = device_set[0]
    testdata.lan_ip = device_set[1]
    testdata.uuid = device_set[2]
    testdata.os_name = device_set[3]
    testdata.save()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER_IP, PORT, LAG_TIME)
client.subscribe(TOPIC+'/#')