import pika, sys, os

def main():
    # ket noi den may chu RabbitMQ 
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    
    #tao ra mot queue, de dam bao queue da co
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    # khi message da duoc nhan tu queue: 'hello' (ack = true), thu vien pika se goi ham callback
    # sau do thuc hien chuc nang cua ham callback
    channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
    
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
