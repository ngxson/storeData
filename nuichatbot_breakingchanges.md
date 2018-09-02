# Các thay đổi quan trọng
  
<a name="02092018"></a>  
__02/09/2018__
Do máy chủ SSL của NuiChatbot thiếu ổn định, hệ thống có 1 vài thay đổi như sau để tránh bị gián đoạn trong tương lai:

- Bỏ hoàn toàn https đối với domain api.chatbot.ngxson.com
- Lập thêm domain dự phòng là api1.chatbot.ngxson.com (KHÔNG có https)
- Đối với các request **bắt buộc** dùng https, hãy sử dụng domain apis.chatbot.ngxson.com
