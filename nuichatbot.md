<a name="chuyenapi"></a>  
# Hướng dẫn chuyển đổi sang API của NuiChatbot:  
  
- Bạn cần lấy token (đầu NUIEAA...) từ web của NuiChatbot.  
- Đối với những chỗ trong code của bạn tạo request tới graph.facebook.com/..., chuyển thành api.chatbot.ngxson.com/graph/...  
- Chúng mình hỗ trợ các endpoint và method như bảng sau:  

|graph.facebook.com|api.chatbot.ngxson.com|method|Ghi chú|  
|-------|-------|------|------|
|/{user-id}|/graph/{user-id}|GET||
|/{page-id}/message|/graph/{page-id}/message|POST||
|/{page-id}/messenger_profile|/graph/{page-id}/messenger_profile|POST, GET||
|/{page-id}/broadcast_messages|/graph/{page-id}/broadcast_messages|POST|[[1]](#chuyenapi1)|
|/{page-id}/message_creatives|/graph/{page-id}/message_creatives|POST|[[1]](#chuyenapi1)|

- Ví dụ:  https://graph.facebook.com/me/message sẽ phải đổi thành https://api.chatbot.ngxson.com/graph/me/message
- **Lưu ý quan trọng**: Đừng quên tham khảo [Giới hạn số lần gặp lỗi](#gioihanloi)

<a name="chuyenapi1"></a> 
Ghi chú [1]: Để sử dụng API Broadcast, bạn cần xin quyền page_messaging_subscription từ phần "Cài đặt page" trên facebook.

<a name="gioihanloi"></a>  
# Giới hạn số lần gặp lỗi  
  
  Để tránh bị spam lỗi, và cũng là đảm bảo các bạn chú ý hơn về hiệu năng server, chúng mình sẽ có các giới hạn số lần lỗi.  
  
Lỗi có thể do gửi sai dạng dữ liệu, gửi tin nhắn ngoài khung 24+1,... Để tránh vượt giới hạn, bên server bạn phải đc lập trình để nhớ và không lặp lại request lỗi.  
  
__Đối với webhook__
- Giới hạn 500 lần lỗi / ngày. Nếu vượt quá, webhook sẽ bị xoá đối với page đó, và bạn sẽ phải đăng ký lại qua web của NuiChatbot.  
- Bạn sẽ nhận đc thông báo lỗi qua inbox khi đạt ngưỡng 350 lỗi / ngày.  
  
__Đối với Graph API__
- Khi số lỗi đạt đến "warning level", bạn sẽ nhận đc 1 cảnh báo qua inbox.
- Nếu vượt quá "max level", bạn sẽ bị **ngắt kết nối** khỏi app. Điều này có nghĩa là webhook+token của **tất cả các page** bạn đã đăng ký đều sẽ bị xoá. (Xin lỗi bạn nếu điều này hơi quá đáng, nhưng facebook không cho revoke 1 token duy nhất và nó chỉ cho ngắt kết nối với app)
- Để tiếp tục sử dụng, bạn cần vào lại web NuiChatbot, đăng ký lại webhook+token cho **tất cả các page**

|endpoint|warning level|max level|
|-----|-----|-----|
|/graph/{user-id}|3500 lỗi / ngày|5000 lỗi / ngày|
|/graph/{page-id}/message|8000 lỗi / ngày|10000 lỗi / ngày|
|/graph/{page-id}/messenger_profile|50 lỗi / ngày|150 lỗi / ngày|
|/graph/{page-id}/broadcast_messages|50 lỗi / ngày|150 lỗi / ngày|
|/graph/{page-id}/message_creatives|50 lỗi / ngày|150 lỗi / ngày|

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
