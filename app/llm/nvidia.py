from openai import OpenAI

from app.config.settings import NVIDIA_API_KEY

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=NVIDIA_API_KEY,
)