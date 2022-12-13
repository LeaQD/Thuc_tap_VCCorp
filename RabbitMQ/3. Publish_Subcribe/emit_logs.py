import pika , sys 

# ket noi toi Rabbitmq server 
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# exchange
channel.exchange_declare( exchange= 'logs', exchange_type= 'fanout' ) 

# message 
message = ' '.join(sys.argv[1:]) or "info : Hello World!"

# gui message 
channel.basic_publish(exchange='logs', routing_key= '', body= message ) 
print("[x] Sent %r" % message ) 
channel.close() 
