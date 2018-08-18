<a name="chuyenapi"></a>  
# Hướng dẫn chuyển đổi sang API của NuiChatbot:  
  
**API này đang trong giai đoạn thử nghiệm**. Nếu bạn gặp lỗi, hãy liên hệ qua fanpage NuiChatbot.
  
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

Bộ đếm số lỗi sẽ đc reset vào lúc 4 giờ 20 hằng ngày
  
__Đối với webhook__
- Tham khảo tại: [Yêu cầu đối với webhook](https://github.com/ngxson/storeData/blob/master/nuichatbot_webhook.md)
  
__Đối với Graph API__
- Khi số lỗi đạt đến "warning level", bạn sẽ nhận đc 1 cảnh báo qua inbox.
- Nếu vượt quá "max level", token bạn đang dùng sẽ bị khóa. Bạn sẽ cần lên web NuiChatbot để lấy token mới.

|endpoint|warning level|max level|
|-----|-----|-----|
|/graph/{user-id}|3500 lỗi / ngày|6000 lỗi / ngày|
|/graph/{page-id}/message|8000 lỗi / ngày|14000 lỗi / ngày|
|/graph/{page-id}/messenger_profile|50 lỗi / ngày|150 lỗi / ngày|
|/graph/{page-id}/broadcast_messages|50 lỗi / ngày|150 lỗi / ngày|
|/graph/{page-id}/message_creatives|50 lỗi / ngày|150 lỗi / ngày|

---
<a name="lienhe"></a>
# Liên hệ

1. Email: contact@ngxson.com
2. Số điện thoại (số nước ngoài, xin chỉ liên hệ khi thực sự cần thiết)
  * <img src="https://raw.githubusercontent.com/ngxson/storeData/master/sdt.jpg" width="150px">
