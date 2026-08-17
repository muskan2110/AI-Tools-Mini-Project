print("===== AI TEXT ASSISTANT =====")

text = input("Enter your text: ")

print("\nOriginal Text:")
print(text)

print("\nWord Count:", len(text.split()))
print("Character Count:", len(text))

print("\nAI Assistant Suggestion:")
print("AI tools like ChatGPT, Gemini and Microsoft Copilot can help with coding, research and productivity.")

print("\nSummary:")
words = text.split()

if len(words) <= 10:
    print("Your text is short and concise.")
else:
    print("Your text contains multiple words and can be summarized using AI tools.")

print("\nThank you for using AI Text Assistant!")
