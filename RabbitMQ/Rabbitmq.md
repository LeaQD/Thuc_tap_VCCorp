# RabbitMQ

**1. RabbitMQ là gì?**

- RabbitMQ là một message boker hay còn gọi là phần mềm quản lý hàng đợi message (thường được gọi là môi giới message hay trình quản lý message). Là phần mềm định nghĩa hàng đợi một ứng dụng khác có thể kết nối tới để bỏ message vào và gửi message dựa trên nó.

- Phương thức phổ biến RabbitMQ sử dụng là AMQP.

![markdown](https://wiki.tino.org/wp-content/uploads/2021/07/word-image-1453.png)

--- 
**2. Các thuật ngữ trong RabbitMQ**

`Producer`: Bên phát hành message

`Consumer`: Bên nhận tin

`Exchange`: Làm nhiệm vụ điều hướng message đến các queue bên trong.

`Routing key`: Là một khóa mà exchange dùng nó để quyết định cách đưa vào hàng đợi. Routing key có thể hiểu như một địa chỉ của message.

`Queues`: có nhiệm vụ lưu trữ bản tin được gửi lên

`Connection`: Là một kết nối TCP giữa ứng dụng và RabbitMQ

`Channel`: Một channel là một kết nối ảo bên trong một connection. Khi bạn đẩy đi hoặc nhận các message từ hàng đợi, tất cả phải đi qua channel

`Binding`: Là một kết nối giữa hàng đợi và exchange

`User`: người dùng có thể kết nối đến #RabbitMQ bằng username/password. Mỗi người dùng được cấp quyền như đọc, ghi và cấu hình quyền bên trong một instance. User còn có quyền trên một host ảo.

`Virtual Host`: Cung cấp chức năng tách ứng dụng dùng trên cùng #RabbitMQ. Người dùng khác nhau có quyền hạn khác nhau trên virtual host, hàng đợi hay exchange khác nhau. Chúng chỉ tồn tại trong một virtual host.

---


**3. RabbitMQ hoạt động như thế nào?**

Muốn hiểu được cơ chế hoạt động cơ bản của RabbitMQ, bạn có thể tưởng tượng rằng nó hoạt động giống như một bưu điện. Dựa theo quy ước RabbitMQ, site A là Producer và các site khác là Consumer. Đây là những người nhận các thông điệp được gửi từ site A. Lúc này, producer sẽ kết nối tới Message broker để thực hiện nhiệm vụ đẩy tin nhắn vào hàng đợi (queue), Consumer sẽ nhận tin nhắn đó qua hệ thống Message Broker. 


---
**4. Những lợi ích mà RabbitMQ mang lại**

- Phân phối xác nhận hoặc xác nhận để tăng độ tin cậy của Message Broker bằng cách giảm mất message. 

- Định tuyến linh hoạt cho phép gửi các thông điệp cụ thể tới người dùng và hàng đợi cụ thể. 

- Định tuyến thông điệp đến người tiêu dùng thông qua nhiều loại trao đổi với các cách thức khác nhau. 

- RabbitMQ là phương pháp đơn giản, an toàn để bạn triển khai cho các đám mây doanh nghiệp và công cộng nhờ dung lượng nhẹ. 

**5. Ý nghĩa của các loại exchange**

**Exchange** là một phần của RabbitMQ, phân chia thành nhiều dạng khác nhau.

- Topic Exchange là phương pháp được sử dụng để định hướng message tới một hay nhiều queue khác nhau trong trường hợp bị trùng routing key và pattern. Thông thường, loại exchange này sẽ được ứng dụng vào định hướng thông điệp đa hướng của một số trường hợp như điều phối dịch vụ khác nhau trong Cloud, phân phối bản tin tới 1 vị trí cụ thể khác. 
- Direct Exchange là phương thức được sử dụng trong quá trình trao đổi trực tiếp, định hướng message vào queue thông qua routing key. Các loại exchange này được dùng cho định tuyến tin nhắn đơn hướng. Thông qua một routing key, mỗi queue lại ràng buộc với một Direct Exchange. 
- Headers Exchange là một định tuyến có nhiều thuộc tính, thực hiện dưới dạng Header của message, định hướng tất cả trên Header thay vì routing key. Một message có giá trị của header  bằng giá trị ràng buộc sẽ được đánh giá là phù hợp. 
- Fanout Exchange là phương thức hỗ trợ định tuyến Message tới toàn bộ queue đã kết hợp với bất cứ một routing key nào. Nó được đánh giá là exchange hữu ích cho người dùng khi muốn gửi message tới các ứng dụng khác nhau. 


--- 
Nguồn tham khảo: [Tìm hiểu về RabbitMQ](https://gpcoder.com/6828-gioi-thieu-rabbitmq/)
