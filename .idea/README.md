# Text Completion App

This is a simple command-line application that uses OpenAI's GPT-3.5 Turbo model to generate text completions based on user input. The app allows you to customize the **temperature** and **maximum token count** for each response.

---

## Features

- Prompt the user for text and generate completions
- Customize `temperature` and `max_tokens`
- Handles invalid inputs gracefully
- Displays helpful error messages (e.g., if API quota is exceeded)

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/text-completion-app.git
cd text-completion-app
```

### 2. Install Dependencies

```bash
pip install openai
```

---

## API Key Configuration

You'll need an OpenAI API key to run this app.

1. Go to [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) to generate an API key.
2. Set the key as an environment variable:

**On Linux/macOS:**

```bash
export OPENAI_API_KEY="your-api-key-here"
```

**On Windows (CMD):**

```cmd
set OPENAI_API_KEY=your-api-key-here
```



## Running the App

```bash
python text_completion_app.py
```

You will be prompted to enter:

- A **prompt** (e.g., "Write a short story about a dragon.")
- A **temperature** between 0.0 and 1.0 (optional; default is 0.7)
- A **max token count** (optional; default is 100)

---

## Example Session

```text
Welcome to the Text Completion App!

Enter your prompt (or type 'exit' to quit): Tell me a joke about cats.
Temperature (0.0-1.0, default=0.7): 0.6
Max tokens (default=100): 50

AI Response:
Why did the cat sit on the computer? Because it wanted to keep an eye on the mouse!
```

---


