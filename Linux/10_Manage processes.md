


# **1. ps, top, htop command**

## **ps: process status** 

```ps```

PID: process ID.

TTY: Loại terminal.

TIME: Tổng thời gian process đã chạy.

CMD: tên của lệnh khởi chạy process.

[Xem thêm](https://vietnix.vn/lenh-ps-trong-linux/)

## **top**
---

```top```

Màn hình mặc định gồm 2 vùng thông tin; 

+ Vùng tóm tắt (hoặc bẳng điều khiển)

+ Vùng tác vụ (hoặc danh sách quy trình) 

top cập nhật màn hình của nó trong vòng 3s một lần.


Các tiêu đề cột trong danh sách quy trình như sau:

`PID`: ID tiến trình.

`USER`: Người sở hữu tiến trình.

`PR`: Tiến trình ưu tiên.

`NI`: Giá trị tốt đẹp của tiến trình.

`VIRT`: Lượng bộ nhớ ảo được sử dụng bởi tiến trình.

`RES`: Lượng bộ nhớ thường trú được sử dụng bởi tiến trình.

`SHR`: Lượng bộ nhớ dùng chung được sử dụng bởi tiến trình.

`S`: Trạng thái của tiến trình. 

`%CPU`: Tỷ lệ thời gian CPU được sử dụng bởi quy trình kể từ lần cập nhật cuối cùng.

`%MEM`: Phần bộ nhớ vật lý được sử dụng.

`TIME`+: Tổng thời gian CPU được sử dụng bởi tác vụ tính bằng phần trăm giây.

`COMMAND`: Tên lệnh hoặc dòng lệnh (tên + tùy chọn).

[Xem thêm](https://www.howtogeek.com/668986/how-to-use-the-linux-top-command-and-understand-its-output/)
---

## **htop**

Cài đặt htop 

```sudo apt install htop``` 


[Xem thêm](https://quantrimang.com/cong-nghe/dung-lenh-htop-theo-doi-cac-tien-trinh-he-thong-168988)

---

# **2.Foreground and Background Processes**

