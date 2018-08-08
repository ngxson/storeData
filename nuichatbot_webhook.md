<a name="yeucauwebhook"></a>  
# NuiChatbot - Yêu cầu đối với webhook
  
Để đảm bảo chắc chắn bên server bạn nhận đc webhook, cũng như hiệu năng server NuiChatbot, webhook cần đạt những tiêu chuẩn nhất định. Các tiêu chuẩn này được mình làm giống nhất với [webhook chuẩn của facebook](https://developers.facebook.com/docs/messenger-platform/webhook#unsubscribe) nhất có thể:

- Phản hồi tất cả sự kiện webhook bằng code 200.
- Phản hồi tất cả sự kiện webhook trong tối đa 12 giây.

Nếu nhận đc code khác 200 hoặc timeout (quá 12s), NuiChatbot sẽ tự động gửi lại tối đa 6 lần, với khoảng thời gian tăng dần (lần lượt là 5s, 10s, 20s, 30s, 30s, 60s). Nếu gửi đến **lần thứ 2** mà không thành công, hệ thống sẽ đếm đây là 1 lần lỗi. Giới hạn số lần lỗi như sau:

- Nếu quá **600 lỗi**, bạn sẽ nhận đc 1 cảnh báo
- Nếu quá **800 lỗi**, bạn sẽ bị **xóa webhook**

Khi bị xóa webhook, bạn cần lên web NuiChatbot để cài lại webhook. Bộ đếm số lỗi sẽ đc reset vào 4h20 hằng ngày, hoặc ngay khi bạn đặt lại webhook

<a name="goiywebhook"></a>  
__Gợi ý để tránh gặp lỗi webhook__
- Bạn nên trả lại code 200 ngay sau khi nhận webhook, sau đó mới xử lý nội dung.
- Đảm bảo server của bạn luôn trả lại code 200, ngày cả khi process chính bị down (tức cần có process phụ thay thế).
 
