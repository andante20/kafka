from kafka import KafkaProducer

producer = KafkaProducer(acks=1, compression_type='gzip', bootstrap_servers='peter-kafka001:9092,peter-kafka002:9092,peter-kafka003:9092')

producer.send('peter-topic', 'Apache Kafka is a distributed streaming platform')
