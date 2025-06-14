import asyncio
import json
import os
from datetime import datetime
from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv

load_dotenv()

# Initialize the language model
llm = ChatOpenAI(model="gpt-4o")


def save_done_result(data: dict, filename: str = "results/final_result.json") -> None:
    """
    Save the final 'done' result to a JSON file in the results directory.

    Args:
        data (dict): The data to save.
        filename (str): The path to the output JSON file.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"✅ Saved 'done' result to {filename}")


async def main() -> None:
    agent = Agent(
        task="""Accesează site-ul https://automationteststore.com. Navighează la categoria 'Fragrance',
        selectează primul produs afișat și adaugă-l în coșul de cumpărături. Apoi, spune-mi numele și prețul produsului.""",
        llm=llm,
    )

    result = await agent.run()
    print(result)

    # ✅ Use correct method: model_actions()
    model_outputs = result.model_actions()

    # ✅ Extract the "done" step
    for output in reversed(model_outputs):
        if isinstance(output, dict) and "done" in output:
            done_info = output["done"]
            save_done_result(done_info)  # ✅ Save to file
            break
    else:
        print("⚠️ No 'done' key found in model_actions()")

if __name__ == "__main__":
    asyncio.run(main())
