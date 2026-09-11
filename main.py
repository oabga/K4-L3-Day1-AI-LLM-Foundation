import os
from template import call_openai

# Prompt bài tập yêu cầu
prompt = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."

# Các mức temperature cần thử nghiệm
temperatures = [0.0, 0.5, 1.0, 1.5]

print("--- THỬ NGHIỆM ĐỘ NHẠY TEMPERATURE ---")
for temp in temperatures:
    print(f"\n================ Temperature = {temp} ================")
    try:
        # Bạn có thể truyền model='meta/llama-3.1-8b-instruct' nếu chưa đổi .env
        text, latency = call_openai(prompt=prompt, temperature=temp)
        print(f"⏱️ Độ trễ: {latency:.2f}s")
        print(f"💬 Phản hồi:\n{text}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")
