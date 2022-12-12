import pika, time 

# ket noi toi RabbitMQ server 
connection = pika.BlockingConnection(pika.ConnectionParameters( host = 'localhost')) 
channel = connection.channel() 

# tao ra mot queue 
channel.queue_declare(queue = 'task_queue', durable = True )

print("[*] Waiting for messages. To exit press CTRL+C'")

def callback( ch, method, properties, body ): 
    print("[x] Received %r" % body.decode() )
    time.sleep(body.count(b'.'))
    print("[x] Done ")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# han che trong mot thoi gian khong gui qua ...(n)..  tin nhan cho worker
# khong gui tin nhan moi cho worker den khi nó xu ly xong va xac nhan tin nhan truoc do 
# thay vao do, no se gui den worker tiep theo khong ban 
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming() 



