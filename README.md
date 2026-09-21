Fake News Detection Using BERT-based Transformer Models

📌 Overview

Fake News Detection is an NLP-based machine learning project designed to classify news content as Fake or Real.

The project uses a BERT-based Transformer model from Hugging Face to understand the contextual information in news text and perform binary text classification.

🎯 Objective

The main objective is to build a text classification system that can identify patterns commonly associated with fake and real news content.

🛠️ Technologies Used

* Python
* Natural Language Processing (NLP)
* BERT
* Hugging Face Transformers
* Scikit-learn
* Pandas
* NumPy

⚙️ Workflow

News Text → Tokenization → BERT Transformer → Text Classification → Fake / Real Prediction

✨ Features

* Accepts news text as input
* Processes text using BERT tokenization
* Uses Transformer-based contextual representations
* Classifies input into Fake or Real
* Displays prediction confidence

📂 Project Structure
```
Fake-News-Detection-Using-BERT/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── data/
```
🚀 How to Run

1. Clone the repository

git clone <your-repository-link>

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python main.py

📊 Evaluation

The model can be evaluated using standard classification metrics such as:

* Accuracy
* Precision
* Recall
* F1-Score

Actual performance depends on the dataset and model configuration.

⚠️ Disclaimer

This project is intended for educational and research purposes. Model predictions should not be considered definitive verification of news authenticity.

👨‍💻 Author

Nithiyanandan
