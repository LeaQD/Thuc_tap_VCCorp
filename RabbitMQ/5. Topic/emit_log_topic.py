import pika, sys 

# ket noi toi rabbitmq server 
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# exchange 
channel.exchange_declare(exchange='logs_topic', exchange_type= 'topic')

key = sys.argv[1] if len(sys.argv) > 2 else "nothing.info" 
message = ' '.join(sys.argv[2:]) or "Hello World!" 

# gui message 
channel.basic_publish(exchange='logs_topic' , routing_key= key , body= message ) 
print("[x] Sent %r: %r" %( key, message)) 
channel.close() 
