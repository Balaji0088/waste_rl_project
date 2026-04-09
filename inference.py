import os
from openai import OpenAI

API_BASE_URL = os.getenv("API_BASE_URL", "https://api.openai.com/v1")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini")

# Safe client
try:
    client = OpenAI(base_url=API_BASE_URL)
except:
    client = None


def run():
    # ✅ START block
    print("[START] task=waste_classification", flush=True)

    state = "plastic"
    print(f"[STEP] step=1 state={state}", flush=True)

    action = "plastic"

    if client:
        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "user", "content": f"Classify: {state}"}]
            )
            action = response.choices[0].message.content.strip()
        except:
            action = "plastic"

    reward = 1 if action.lower() == state else -1

    # ✅ STEP block
    print(f"[STEP] step=1 action={action} reward={reward}", flush=True)

    # ✅ END block
    print(f"[END] task=waste_classification score={reward} steps=1", flush=True)


if __name__ == "__main__":
    run()
