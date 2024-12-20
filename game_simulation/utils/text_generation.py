import re
import os
from dotenv import load_dotenv
from transformers import pipeline
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"), # Get OpenAI API key from environment variables
    base_url=os.getenv("DEEPSEEK_BASE_URL"),
)

def generate(prompt: str, use_openai: bool = True):
    """ 
    Generates a text completion for a given prompt using either the OpenAI or the HuggingFace model.

    Args:
    - prompt (str): The text prompt to generate a completion for.
    - use_openai (bool): A boolean flag indicating whether to use the OpenAI API (True) or the HuggingFace model (False)

    Returns
    - str: The generated text completion.
    """
    if use_openai:
        response = client.chat.completions.create(
            model = "deepseek-chat",
            messages=[
               # {"role": "system", "content": "尽可能使用中文来回答问题。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
        )
        message = response.choices[0].message.content
        return message.strip() # strip()主要用于移除字符串两端的空白字符或指定字符。
    else:
        hf_generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B', device=0)
        output = hf_generator(prompt, max_length=len(prompt)+128, do_sample=True)
        out = output[0]['generated_text']
        if '### Response:' in out:
            out = out.split('### Response:')[1]
        if '### Instruction:' in out:
            out = out.split('### Instruction:')[0]
        return out.strip()


def get_rating(x: str):
    """
    Extracts a rating from a string.
    
    Args:
    - x (str): The string to extract the rating from.
    
    Returns:
    - int: The rating extracted from the string, or None if no rating is found.
    """
    nums = [int(i) for i in re.findall(r'\d+', x)] # 从字符串 x 中提取所有的数字并将其转换为整数
    if len(nums)>0:
        return min(nums)
    else:
        return None

# Summarize simulation loop with OpenAI GPT-4
def summarize_simulation(log_output):
    prompt = f"Summarize the simulation loop:\n\n{log_output}"
    response = generate(prompt)
    return response

if __name__ == "__main__":
    print("---- test: get_rating ----")
    x = "我有8个苹果, 他有90个苹果; --> 提取string中最小的数字"
    print("input:", x)
    print("extract output:", get_rating(x))

    print("---- test: summarize_simulation ----")
    log_output = """Toblen Stonehill action: I get out of bed and have breakfast. Then, I go to the market to buy supplies for the trading post. After that, I arrive at the trading post and unload the supplies. Finally, I start trading."""
    print("log_output:", log_output)
    print("summary:", summarize_simulation(log_output))