import os
import openai

# Set your API key
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text(prompt, temperature=0.7, max_tokens=100):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("Welcome to the Text Completion App!")
    while True:
        prompt = input("\nEnter your prompt (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            break
        elif not prompt.strip():
            print("Please enter a non-empty prompt.")
            continue

        temperature = input("Temperature (0.0–1.0, default=0.7): ").strip()
        max_tokens = input("Max tokens (default=100): ").strip()

        try:
            temperature = float(temperature) if temperature else 0.7
        except:
            temperature = 0.7

        try:
            max_tokens = int(max_tokens) if max_tokens else 100
        except:
            max_tokens = 100

        result = generate_text(prompt, temperature, max_tokens)
        print("\nAI Response:")
        print(result)

if __name__ == "__main__":
    main()
