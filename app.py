from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import logging
from datetime import datetime
import os

app = FastAPI()

# Mount static folder for frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load your fine-tuned model
model_path = "./fine_tuned_model"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path)

# --- Logging setup ---
if not os.path.exists("logs"):
    os.makedirs("logs")

log_filename = f"logs/recipe_logs_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def log_request(user_input: str, bot_response: str):
    logging.info(f"User Input: {user_input}")
    logging.info(f"Bot Response: {bot_response}")
    logging.info("-" * 80)

# --- End Logging setup ---

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

@app.get("/generate/")
async def generate(ingredients: str):
    # Prepare input
    input_text = f"Suggest a recipe with: {ingredients}"
    inputs = tokenizer(input_text, return_tensors="pt", max_length=128, truncation=True)

    # Generate output
    outputs = model.generate(**inputs, max_length=128)
    recipe = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Log input & output
    log_request(ingredients, recipe)

    return JSONResponse({"recipe": recipe})
