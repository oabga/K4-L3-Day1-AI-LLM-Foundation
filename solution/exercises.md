# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Ở mức temperature 0.0 và 0.5, phản hồi có tính nhất quán cao, câu từ chuẩn xác, tập trung và cấu trúc mạch lạc. Khi tăng lên 1.0, mô hình bắt đầu sử dụng từ vựng đa dạng và cách diễn đạt phong phú, sáng tạo hơn. Tuy nhiên ở mức 1.5, độ ngẫu nhiên quá cao khiến văn phong bị lặp từ, cấu trúc ngữ pháp bất ổn và nội dung có nguy cơ bị ảo tưởng (hallucination).

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Tôi sẽ đặt temperature khoảng 0.0 đến 0.2. Lý do là chatbot hỗ trợ khách hàng cần cung cấp thông tin chính xác, nhất quán và đáng tin cậy về chính sách/sản phẩm; việc đặt temperature thấp sẽ hạn chế tối đa nguy cơ mô hình tự bịa ra thông tin sai sự thật (hallucination).

### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> GPT-4o đắt hơn GPT-4o-mini khoảng 16.7 lần (với 10.5M token đầu ra mỗi ngày, GPT-4o tốn ~$105/ngày trong khi mini chỉ tốn ~$6.3/ngày). GPT-4o xứng đáng chi phí khi giải quyết các tác vụ phức tạp yêu cầu tư duy logic sâu, lập trình hoặc phân tích tài liệu pháp lý chuyên sâu. Ngược lại, GPT-4o-mini nên được áp dụng cho các tác vụ thường nhật như trả lời câu hỏi FAQ khách hàng, phân loại email hoặc tóm tắt văn bản đơn giản để tối ưu chi phí.

---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Phản hồi cho trẻ 8 tuổi dùng ngôn từ đơn giản, ẩn dụ gần gũi (như cuốn sổ nhật ký chung của cả lớp) với câu ngắn và độ dài vừa phải. Trái lại, phản hồi chuyên gia tài chính sử dụng từ vựng chuyên ngành như "sổ cái phân tán (DLT)", "cơ chế đồng thuận", "mã hóa cryptographic" với độ dài chi tiết và cấu trúc chặt chẽ. System prompt đóng vai trò định hình ngữ cảnh (context) và persona, điều khiển toàn bộ giọng văn, thuật ngữ và mức độ phức tạp trong phản hồi của mô hình.

### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Số token đếm qua tiktoken thường lớn hơn ước lượng số từ / 0.75 từ 30% đến 60% (khoảng 130-160 tokens cho 100 từ). Tiếng Việt tốn nhiều token hơn tiếng Anh vì các tokenizer (như cl100k_base) được huấn luyện chủ yếu trên dữ liệu tiếng Anh, do đó các từ tiếng Việt mang dấu thanh và từ ghép thường bị chia tách thành nhiều sub-word tokens hoặc byte tokens lẻ.

---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất trong các ứng dụng chat tương tác trực tiếp với người dùng (như chatbot tư vấn, trợ lý ảo) để giảm Time To First Token (TTFT), giúp người dùng thấy câu trả lời ngay lập tức thay vì phải chờ đợi toàn bộ câu trả lời hoàn tất. Trái lại, non-streaming phù hợp hơn khi thực hiện xử lý ngầm (background jobs), gọi API lấy dữ liệu JSON cấu trúc (Structured Outputs), chạy tự động hóa hàng loạt (batch processing) hoặc khi cần phân tích/tóm tắt toàn bộ dữ liệu trước khi gửi cho hệ thống tiếp theo.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff giúp tăng thời gian chờ sau mỗi lần thất bại, cho phép hệ thống API có đủ thời gian phục hồi sau các đợt quá tải đột biến. Nếu hàng nghìn client cùng retry với delay cố định (như 1 giây), sẽ xảy ra hiện tượng "thảm họa dồn dập" (Thundering Herd Problem / Retry Storm), làm API liên tục bị ngập trong các request lặp lại và vĩnh viễn không thể khôi phục trạng thái bình thường.

---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Tôi chọn persona "Trợ lý lập trình Python thông minh". System prompt: "Bạn là một chuyên gia lập trình Python lâu năm. Hãy giải thích ngắn gọn, đi thẳng vào vấn đề, luôn đưa ra ví dụ code minh họa chuẩn PEP8 và trả lời bằng tiếng Việt." Giải thích: 1) Cụm "trả lời ngắn gọn, đi thẳng vào vấn đề" giúp tiết kiệm số lượng token đầu ra (giảm chi phí) và giúp người dùng nhanh chóng nắm bắt giải pháp. 2) Cụm "chuẩn PEP8 và trả lời bằng tiếng Việt" đảm bảo code đầu ra đạt chất lượng cao, dễ đọc và phù hợp với ngôn ngữ làm việc của người dùng.

### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất là history bị giới hạn chỉ 3 lượt gần nhất (6 messages) và không lưu trữ bộ nhớ dài hạn giữa các phiên làm việc. Đề xuất cải thiện: Triển khai cơ chế Tóm tắt lịch sử (Conversation Summarization) kết hợp với lưu trữ Database (như SQLite/Redis). Cách triển khai: Khi lịch sử chat vượt quá 6 messages, sử dụng một cuộc gọi LLM phụ để tóm tắt các đoạn hội thoại cũ thành một đoạn văn ngắn gọn và chèn đoạn tóm tắt đó vào System Prompt. Nhờ đó, trợ lý vẫn nắm được ngữ cảnh từ đầu buổi nói chuyện mà không làm phồng số lượng token truyền vào.

---

## Danh Sách Kiểm Tra Nộp Bài

- [x] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [x] Cả 4 checkpoint pytest đều pass
- [x] Tất cả 9 câu trong file này đã được trả lời
- [x] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
