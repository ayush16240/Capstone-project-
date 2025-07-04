import google.generativeai as genai
from typing import List, Dict, Any

class GeminiChat:
    def __init__(self, api_key: str, model_name: str = "gemini-2.5-pro"):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name)
        self.chat = self.model.start_chat(history=[])

    def send_message(self, message: str) -> str:
        response = self.chat.send_message(message)
        return response.text

    def get_chat_history(self) -> List[Dict[str, Any]]:
        return [{"role": msg.role, "text": msg.parts[0].text}
                for msg in self.chat.history]