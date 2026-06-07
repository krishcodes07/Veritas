from app.llm.nvidia import client


class LLMService:

    def generate(
        self,
        prompt: str,
        model: str = "minimaxai/minimax-m2.7"
    ):

        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content