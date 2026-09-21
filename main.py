from transformers import pipeline

print("Fake News Detection Using BERT")
print("-" * 40)

# Load BERT-based fake news classification model
classifier = pipeline(
    "text-classification",
    model="mrm8488/bert-tiny-finetuned-fake-news"
)

while True:
    news = input("\nEnter news text (or type 'exit' to stop): ")

    if news.lower() == "exit":
        print("Program ended.")
        break

    result = classifier(news)[0]

    label = result["label"]
    confidence = result["score"] * 100

    print("\nPrediction:", label)
    print(f"Confidence: {confidence:.2f}%")
