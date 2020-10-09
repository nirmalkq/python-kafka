from kafka import KafkaProducer
from time import sleep
from json import dumps
try:
    print('kafka producer')
    producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda x: dumps(x).encode('utf-8'))
    for i in range(9999):
        print("Iteration", i)
        data = {'count number': i}
        producer.send('mytopic1', value=data)
        sleep(0.5)
except Exception as e:
    print(e)
    # Logs the error appropriately.
    pass
