from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

import os
import datetime
import requests

load_dotenv()

# ---------------- MEMORY ---------------- #
memory_store = {}

# ---------------- TOOLS ---------------- #

@tool
def calculator(a: float, b: float, operation: str = "add") -> str:
    """Perform arithmetic operations: add, subtract, multiply, divide"""
    try:
        if operation == "add":
            result = a + b
        elif operation == "subtract":
            result = a - b
        elif operation == "multiply":
            result = a * b
        elif operation == "divide":
            if b == 0:
                return "Error: Division by zero"
            result = a / b
        else:
            return "Invalid operation"

        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"


@tool
def advanced_math(expression: str) -> str:
    """Evaluate a math expression"""
    try:
        result = eval(expression)
        return f"Result: {result}"
    except Exception as e:
        return f"Error: {str(e)}"


@tool
def get_current_time() -> str:
    """Get current date and time"""
    now = datetime.datetime.now()
    return f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}"


@tool
def read_text_file(file_path: str) -> str:
    """Read content from a text file"""
    try:
        if not os.path.exists(file_path):
            return "File not found."

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return f"File content:\n{content[:1000]}"
    except Exception as e:
        return f"Error reading file: {str(e)}"


@tool
def list_files(directory: str = ".") -> str:
    """List files in a directory"""
    try:
        files = os.listdir(directory)
        return "\n".join(files)
    except Exception as e:
        return str(e)


@tool
def fetch_api(url: str) -> str:
    """Fetch data from an API endpoint"""
    try:
        response = requests.get(url, timeout=5)
        return response.text[:1000]
    except Exception as e:
        return str(e)


@tool
def web_search(query: str) -> str:
    """Search for information on the web (mock)"""
    return f"Search results for '{query}': (integrate real API like Tavily here)"


@tool
def save_memory(key: str, value: str) -> str:
    """Save information in memory"""
    memory_store[key] = value
    return f"Saved {key}"


@tool
def get_memory(key: str) -> str:
    """Retrieve information from memory"""
    return memory_store.get(key, "No memory found")


@tool
def summarize_text(text: str) -> str:
    """Summarize a given text"""
    model = ChatOpenAI(temperature=0)
    response = model.invoke(f"Summarize this:\n{text}")
    return response.content


@tool
def explain_code(code: str) -> str:
    """Explain a piece of code"""
    model = ChatOpenAI(temperature=0)
    response = model.invoke(f"Explain this code:\n{code}")
    return response.content


# ---------------- MAIN ---------------- #

def main():
    model = ChatOpenAI(temperature=0)

    tools = [
        calculator,
        advanced_math,
        get_current_time,
        read_text_file,
        list_files,
        fetch_api,
        web_search,
        save_memory,
        get_memory,
        summarize_text,
        explain_code
    ]

    agent_executor = create_react_agent(model, tools)

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.")
    print("I can perform calculations, read files, call APIs, remember things, and more.")

    chat_history = []

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            break

        chat_history.append(HumanMessage(content=user_input))

        print("\nAssistant: ", end="")

        try:
            for chunk in agent_executor.stream(
                {"messages": chat_history}
            ):
                if "agent" in chunk and "messages" in chunk["agent"]:
                    for message in chunk["agent"]["messages"]:
                        print(message.content, end="")
        except Exception as e:
            print(f"\nError: {str(e)}")

        print()


if __name__ == "__main__":
    main()