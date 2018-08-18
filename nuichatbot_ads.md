
<a name="adspolicy"></a>
# Chính sách đặt quảng cáo của NuiChatbot  
  
Để lấy kinh phí duy trì domain và server, từ ngày 21/08/2018, hệ thống NuiChatbot sẽ gửi 1 tin nhắn quảng cáo ngay sau tin nhắn đầu tiên của người dùng tới fanpage. Chính sách này chỉ áp dụng cho các fanpage không tham gia gói trả phí.  
  
Chính sách sẽ đảm bảo người dùng không bị làm phiền quá nhiều bởi quảng cáo, cụ thể là flow sau:  
1. Sau tin nhắn đầu tiên của user vào fanpage, 1 tin nhắn quảng cáo sẽ được gửi tới người đó.  
2. Hệ thống sẽ ghi nhận thời điểm vừa xong (gọi là thời điểm A)  
3. Với mỗi tin nhắn tiếp theo user gửi về page, hệ thống gọi đó là thời điểm B  
4. Nếu thời điểm B - A > 14 ngày, hệ thống sẽ gửi thêm 1 quảng cáo user, sau đó đặt lại thời điểm A  
5. Lặp lại bước 3  
  
**Lưu ý:** hệ thống sẽ **không tự động gửi quảng cáo** nếu user không inbox đến page, tránh làm người dùng cảm thấy phiền.
  
**Format quảng cáo:**  
- Quảng cáo gồm 9 cards chứa thông tin quảng cáo theo chiều ngang (generic template)  
- 1 card cuối cùng giải thích rằng chatbot của bạn được trợ giúp bởi NuiChatbot. Card này chứa 1 mã checkcode để tránh bị giả mạo.
