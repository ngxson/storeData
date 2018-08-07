<a name="chuyenapi"></a>  
# Hướng dẫn chuyển đổi sang API của NuiChatbot:  
  
- Bạn cần lấy token (đầu NUIEAA...) từ web của NuiChatbot.  
- Đối với những chỗ trong code của bạn tạo request tới graph.facebook.com/..., chuyển thành api.chatbot.ngxson.com/graph/...  
- Chúng mình hỗ trợ các endpoint và method như bảng sau:  

|graph.facebook.com|api.chatbot.ngxson.com|method|Ghi chú|  
|-------|-------|------|------|
/{user-id}|/graph/{user-id}|GET||
/{page-id}/message|/graph/{page-id}/message|POST||
/{page-id}/messenger_profile|/graph/{page-id}/messenger_profile|POST, GET||
/{page-id}/broadcast_messages|/graph/{page-id}/broadcast_messages|POST|[[1]](#chuyenapi1)|
/{page-id}/message_creatives|/graph/{page-id}/message_creatives|POST|[[1]](#chuyenapi1)|

- Ví dụ:  https://graph.facebook.com/me/message sẽ phải đổi thành https://api.chatbot.ngxson.com/graph/me/message
- **Lưu ý quan trọng**: Đừng quên tham khảo [Giới hạn số lần gặp lỗi](#gioihanloi)

<a name="chuyenapi1"></a> 
Ghi chú [1]: Để sử dụng API Broadcast, bạn cần xin quyền page_messaging_subscription từ phần "Cài đặt page" trên facebook.

<a name="banggia"></a>
# Bảng giá Nui Chatbot

Bảng giá này chỉ áp dụng với các page **có lợi nhuận** (ví dụ: page bán hàng, chăm sóc khách hàng, thu tiền từ nội dung quảng cáo qua inbox,...)

Bạn chỉ phải trả **1 lần duy nhất** cho mỗi page. Trả trong vòng 7 ngày kể từ khi bạn đăng ký Lượt like được tính vào lúc bạn đăng ký page trên hệ thống Nui Chatbot.

| Số Like Page | Giá |
|----------|---------|
| dưới 800 likes | 100.000đ |
| từ 800 đến 2500 likes | 180.000đ |
| trên 2500 likes | 300.000đ |

__Cách trả phí:__
1. Chuyển khoản qua TK với nội dung `nuichatbot-(tên page)`:
  * Tài khoản 2200201279439, chủ TK Bùi Thị Xuân, NH Agribank chi nhánh Hà Tây.
2. Chụp lại phiếu, hoá đơn hoặc màn hình kết quả chuyển khoản.
3. Vào trang sau: https://nuichatbot.ngxson.com/#!/paid , chọn page và bấm vào nút "Đăng ký page trả phí", sau đó điền các thông tin cần thiết.

<a name="lienhe"></a>
# Liên hệ

1. Email: contact@ngxson.com
2. Số điện thoại (số nước ngoài, xin chỉ liên hệ khi thực sự cần thiết)
  * <img src="https://raw.githubusercontent.com/ngxson/storeData/master/sdt.jpg" width="150px">
