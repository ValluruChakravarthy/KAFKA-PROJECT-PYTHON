import json
from kafka import KafkaProducer
from pizzacustom import pizzacustom
from fake import messagetype

folderName="./"
producer=KafkaProducer(
    bootstrap_servers="chakri-kafka-project-chakri-service.l.aivencloud.com:15079",
    security_protocol="SSL",
    ssl_cafile=folderName+"ca.pem",
    ssl_certfile=folderName+"service.cert",
    ssl_keyfile=folderName+"service.key",
    value_serializer=lambda v:json.dumps(v).encode('ascii'),
    key_serializer=lambda v:json.dumps(v).encode('ascii')
)

producer.send(
    "Remind-that",
   value=messagetype()

)
producer.flush()
#this is for pushing into the kafka Aiven cloud running on Aws