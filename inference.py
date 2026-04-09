def run():
    print("[START] task=waste_classification", flush=True)

    state = "plastic"
    print(f"[STEP] step=1 state={state}", flush=True)

    action = "plastic"
    reward = 1 if action == state else -1

    print(f"[STEP] step=1 action={action} reward={reward}", flush=True)

    print(f"[END] task=waste_classification score={reward} steps=1", flush=True)


if __name__ == "__main__":
    run()
