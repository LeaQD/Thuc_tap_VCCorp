import pika , sys 

# ket noi toi rabbitmq server 
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# exchange 
channel.exchange_declare(exchange='direct_logs', exchange_type= 'direct' ) 

# routing_key : severity 
severity = sys.argv[1] if len(sys.argv) > 1 else "info" 
message = ' '.join(sys.argv[2:]) or "Hello World!" 

channel.basic_publish(exchange='direct_logs',routing_key=severity,body=message) 
print("[x] Sent %r: %r" % (severity, message) ) 
channel.close()