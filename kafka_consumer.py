from kafka import KafkaConsumer

try:
    print('Kafka Consumer')
    consumer = KafkaConsumer('mytopic1', bootstrap_servers='localhost:9092')
    for message in consumer:
        print(message)
except Exception as e:
    print(e)
    pass
