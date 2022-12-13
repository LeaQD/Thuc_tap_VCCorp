import pika

# ket noi toi rabbitmq server
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost' )) 
channel = connection.channel()

# exchange
channel.exchange_declare(exchange='logs', exchange_type= 'fanout') 

# tao ra queue 
# result.method.queue chua mọt ten ngau nhien 
# exclusive = True: khi ket noi nguoi dung bi dong, hang doi se bi xoa de dam bao tinh doc quyen 
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue

# tao ra mot rang buoc giua exchange va queue : bind 
channel.queue_bind( exchange = 'logs', queue= queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch,method,properties, body ) : 
    print("[x] %r" % body ) 

channel.basic_consume(queue=queue_name, on_message_callback= callback , auto_ack= True) 

channel.start_consuming()