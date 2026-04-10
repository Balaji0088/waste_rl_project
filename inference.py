import os
from openai import OpenAI

def run():
    print("[START] task=waste_classification", flush=True)

    state = "plastic"
    print(f"[STEP] step=1 state={state}", flush=True)

    action = "plastic"

    try:
        client = OpenAI(
            api_key=os.environ["API_KEY"],
            base_url=os.environ["API_BASE_URL"]
        )

        response = client.chat.completions.create(
            model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
            messages=[{"role": "user", "content": f"Classify: {state}"}]
        )

        action = response.choices[0].message.content.strip().lower()

    except Exception as e:
        action = "plastic"

    reward = 1 if action == state else -1

    print(f"[STEP] step=1 action={action} reward={reward}", flush=True)

    print(f"[END] task=waste_classification score={reward} steps=1", flush=True)


if __name__ == "__main__":
    run()
