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

### 📜 Documentation
- Swagger API Docs at `/docs`

### 🎨 Modern UI
- Responsive, clean, and user-friendly
  <img width="549" height="735" alt="image" src="https://github.com/user-attachments/assets/05a7533a-4910-4356-943d-93e520993896" />
  <img width="536" height="727" alt="image" src="https://github.com/user-attachments/assets/735b725d-1a3b-4e1f-850e-4c1ba93a8f18" />
  <img width="531" height="732" alt="image" src="https://github.com/user-attachments/assets/39614d89-4550-49fe-86e5-9f0598778f98" />




---

## Installation

## 1. Clone the repository
```bash
git clone <repo-url>
cd <repo-folder>
```
## 2.Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

## 3.Install dependencies
```bash
pip install fastapi uvicorn transformers datasets torch
````
## Fine-tuning the Model

1.Place your dataset train.csv in the root folder with the following format:
```
ingredients	recipe
"egg, onion"	"Omelette with onions..."
"rice, tomato"	"Tomato rice..."
```
2.Run the fine-tuning script:
```bash
python fine_tune.py
```

3.The fine-tuned model will be saved in ./fine_tuned_model.

## Running the App

1.Start the FastAPI server:
```bash
uvicorn app:app --reload
```

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

---

## 🧑‍💻 Author

Developed by **Sahana Khanai**
