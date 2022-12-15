import pika, sys 

# ket noi toi rabbitmq server 
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel() 

# exchange 
channel.exchange_declare(exchange='logs_topic', exchange_type='topic')

# queue 
result = channel.queue_declare(queue='', exclusive=True) 
name_queue = result.method.queue 

binding_keys = sys.argv[1:]
if len(binding_keys) == 0 : 
    sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0]) 
    sys.exit(1)

for binding_key in binding_keys: 
    channel.queue_bind(exchange='logs_topic', queue=name_queue, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body) : 
    print ("[x] Receive %r: %r" %(method.routing_key, body))

channel.basic_consume(queue=name_queue, on_message_callback= callback , auto_ack= True) 
channel.start_consuming()
