import pika, sys 

# ket noi toi rabbitmq server 
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost'))
channel = connection.channel()

# exchange 
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(queue='', exclusive=True)
name_queue = result.method.queue 

severities = sys.argv[1:]
if len(severities) == 0 : 
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

# tao ra cac rang buoc giua exchange va queue 
for sevverity in severities : 
    channel.queue_bind(exchange='direct_logs', queue= name_queue, routing_key=sevverity ) 

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch,method,properties, body) : 
    print("[x] Receive %r: %r" %(method.routing_key, body )) 

channel.basic_consume(queue=name_queue, on_message_callback=callback, auto_ack= True) 

channel.start_consuming()
