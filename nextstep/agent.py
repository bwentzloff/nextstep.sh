import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class AIProjectAgent:
    def __init__(self):
        self.api_key = os.getenv("NEXTSTEP_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not found. Please set it in the .env file."
            )
        self.client = OpenAI(api_key=self.api_key)
        self.storage_file = "tasks.json"

    def generate_tasks(self, pg):
        """Generates a list of tasks based on a goal using OpenAI's GPT model."""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert project manager."},
                    {
                        "role": "user",
                        "content": (
                            f"Break down this goal into actionable tasks: {pg}",
                        ),
                    },
                ],
                max_tokens=500,
            )
            tasks = response.choices[0].message.content.strip().split("\n")

            structured_tasks = {
                "goal": pg,
                "tasks": [task.strip() for task in tasks if task.strip()],
            }

            self.save_tasks(structured_tasks)
            return structured_tasks
        except Exception as e:
            return f"Error generating tasks: {str(e)}"

    def save_tasks(self, data):
        """Saves structured task data to a local JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, "r") as file:
                existing_data = json.load(file)
        else:
            existing_data = []

        existing_data.append(data)

        with open(self.storage_file, "w") as file:
            json.dump(existing_data, file, indent=4)

        print(f"Tasks saved to {self.storage_file}")


# Example usage (for testing)
if __name__ == "__main__":
    agent = AIProjectAgent()
    goal = "Develop a user authentication system"
    tasks = agent.generate_tasks(goal)
    print(json.dumps(tasks, indent=4))
