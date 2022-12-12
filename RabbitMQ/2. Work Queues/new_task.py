import pika, sys 

# ket noi toi RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host = 'localhost')) 
channel = connection.channel()

# tao ra mot queue 
# khi RabbitMQ thoat hoac gap su co, cac tin nhan va hang doi se bi quen
# de khac phuc dieu nay, phai khai bao durable = True 
# tu do, hang doi va thu se lau ben
channel.queue_declare(queue = 'task_queue', durable = True)

# message 
message = ' '.join(sys.argv[1:]) or "Hello World!" 

# cac message duoc gui di bang exchange mac dinh, routinh_key = 'task_queue' 
# danh dau thu cua minh la co dac tinh lien tuc bang cach
# cung cap thuoc tinh delivery_mode = pika.spec.PERSISTENT_DELIVERY_MODE
channel.basic_publish(exchange = '' , 
routing_key= 'task_queue' , 
body= message, 
properties=pika.BasicProperties(delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE))

print("[x] Sent %r" % message ) 

connection.close() 
