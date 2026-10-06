import colorama
from colorama import Fore, Style
from textblob import TextBlob

colorama.init(autoreset=True)

history = []
pos = 0
neu = 0
neg = 0

def show_processing_animation():
    print(f"{Fore.CYAN}Analyzing text sentiment...{Style.RESET_ALL}")
    for x in range(5000000):
        pass

def analyze_sentiment(text):
    global pos, neu, neg
    show_processing_animation()
    
    polarity = TextBlob(text).sentiment.polarity
    
    if polarity > 0.1:
        print(f"{Fore.GREEN}Result: Positive (Score: {polarity:.2f})\n")
        pos += 1
    elif polarity < -0.1:
        print(f"{Fore.RED}Result: Negative (Score: {polarity:.2f})\n")
        neg += 1
    else:
        print(f"{Fore.YELLOW}Result: Neutral (Score: {polarity:.2f})\n")
        neu += 1
        
    history.append(text)

def execute_command(command):
    global pos, neu, neg
    if command == "history":
        print(f"Past sentences: {history}\n")
    elif command == "reset":
        history.clear()
        pos = neu = neg = 0
        print("Cleared all data!\n")

def get_valid_name():
    while True:
        name = input("Enter your name (letters only): ").strip()
        if name.isalpha():
            return name
        print("Error: Letters only please.")

print("--- Welcome to Sentiment Spy ---")
user_name = get_valid_name()

print(f"\nHello Agent {user_name}!")
print("Options: Type any sentence for sentiment analysis, or use commands: history, reset, exit\n")

while True:
    user_input = input(">> ").strip()
    
    if not user_input:
        continue
    if user_input == "exit":
        break
        
    if user_input in ["history", "reset"]:
        execute_command(user_input)
    else:
        analyze_sentiment(user_input)

print("\nSaving final summary report...")

with open(f"{user_name}_sentiment_analysis.txt", "w") as f:
    f.write("Sentiment Analysis Summary Report\n")
    f.write(f"Positive messages: {pos}\n")
    f.write(f"Neutral messages: {neu}\n")
    f.write(f"Negative messages: {neg}\n")

print("Done! File saved. Goodbye!")