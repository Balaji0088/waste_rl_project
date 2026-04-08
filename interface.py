import os
import random
from openai import OpenAI


API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")
HF_TOKEN = os.getenv("HF_TOKEN")


client = OpenAI(base_url=API_BASE_URL)


class WasteSegregationEnv:
    def __init__(self):
     
        self.waste_types = ["plastic", "metal", "paper", "glass"]

    def reset(self):
        self.current_item = random.choice(self.waste_types)
        return self.current_item

    def evaluate_action(self, action):
        
        if action == self.current_item:
            return 2   
        else:
            return -1


def run():
    print("START")

    env = WasteSegregationEnv()

    state = env.reset()
    print(f"STEP: Generated waste item = {state}")

    prompt = (
        f"You are an AI system for waste management.\n"
        f"Identify the correct category of this waste item: {state}.\n"
        f"Options: plastic, metal, paper, glass.\n"
        f"Respond with only one word."
    )

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}]
        )

        action = response.choices[0].message.content.strip().lower()

    except Exception as e:
       
        print(f"STEP: LLM failed, using fallback logic")
        action = random.choice(env.waste_types)

    print(f"STEP: LLM selected action = {action}")

    
    reward = env.evaluate_action(action)

    result = "Correct" if reward > 0 else "Incorrect"
    print(f"STEP: Evaluation result = {result}")
    print(f"STEP: Reward assigned = {reward}")

    print("END")


if __name__ == "__main__":
    run()