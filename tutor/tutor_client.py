from openai import OpenAI, OpenAIError
from .config import OPENAI_API_KEY, MODEL_GPT
from .prompts import tutor_system_prompt
from .utils import parse_json_safe

class TutorClient:
    def __init__(self, api_key=OPENAI_API_KEY, model=MODEL_GPT):
        self.client = OpenAI(api_key=api_key)
        self.model = model
        self.system_prompt = tutor_system_prompt

    def ask_tutor(self, code: str) -> dict:
        user_prompt = f"Here is the code or error to analyze:\n\n{code}"
        try:
            response = self.client.chat.completions.create(
                model = self.model,
                messages = [
                    {"role": "system", "content": self.system_prompt},
                    {"role":"user", "content": user_prompt}
                ],
                response_format = {"type": "json_object"}
            )
            return parse_json_safe(response.choices[0].message.content)
        except OpenAIError as e:
            return {
                    "explanation": f"OpenAI API Error: {e}",
                    "fix": "No fix needed.",
                    "fixed_code": "",
                    "improvement": "No improvement needed.",
                    "improved_code": ""
                }
