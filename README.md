# Recipe Chatbot

A web-based chatbot that suggests recipes based on ingredients you provide. The project uses a **fine-tuned T5 model** (`flan-t5-small`) for generating recipes and a **FastAPI** backend with a simple HTML/JS frontend.

---

## Features
- Enter a list of ingredients and get recipe suggestions.
- Clean, responsive chat interface.
- Logs all user inputs and bot responses.
- Fine-tuned on a custom dataset (`train.csv`) for better recipe suggestions.

---

## Project Structure
```
├── app.py # FastAPI backend
├── fine_tune.py # Script to fine-tune the T5 model
├── train.csv # Dataset with ingredients and recipes
├── fine_tuned_model/ # Directory to save/load the fine-tuned model
├── static/
│ └── index.html # Frontend HTML
└── logs/ # Logs of user interactions
```

---

## Installation

## 1. Clone the repository

git clone <repo-url>
cd <repo-folder>

## 2.Create a virtual environment

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


## 3.Install dependencies

pip install fastapi uvicorn transformers datasets torch

## Fine-tuning the Model

1.Place your dataset train.csv in the root folder with the following format:

ingredients	recipe
"egg, onion"	"Omelette with onions..."
"rice, tomato"	"Tomato rice..."

2.Run the fine-tuning script:

python fine_tune.py


3.The fine-tuned model will be saved in ./fine_tuned_model.

## Running the App

1.Start the FastAPI server:

uvicorn app:app --reload


2.Open your browser and go to:

http://127.0.0.1:8000/


3.Enter ingredients in the input box and get recipe suggestions from the chatbot.
## Logging

All user inputs and generated recipes are logged in the logs/ folder daily:

logs/recipe_logs_YYYY-MM-DD.log

## Notes

Ensure your dataset is clean and properly formatted to improve recipe quality.

Adjust max_length and num_train_epochs in fine_tune.py depending on dataset size.

For production, consider adding input validation and more sophisticated frontend features.

## Developer

Sahana Khanai
