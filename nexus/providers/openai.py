from openai import OpenAI


class OpenAIProvider:
    """OpenAI compatible LLM provider.

    Supports OpenAI compatible endpoints such as OpenAI,
    GLM, Qwen, DeepSeek and internal gateways.
    """

    def __init__(self, api_key, base_url=None, model="gpt-5"):
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )
        self.model = model

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        return response.choices[0].message.content
