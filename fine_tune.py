from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq, TrainingArguments, Trainer

# Load dataset from CSV
dataset = load_dataset("csv", data_files={"train": "train.csv"})

# Model and tokenizer
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# Preprocess function
def preprocess(examples):
    inputs = [f"Suggest a recipe with: {ing}" for ing in examples["ingredients"]]
    targets = examples["recipe"]
    model_inputs = tokenizer(inputs, max_length=128, truncation=True)
    labels = tokenizer(targets, max_length=128, truncation=True)
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

tokenized = dataset["train"].map(preprocess, batched=True)

# Data collator
data_collator = DataCollatorForSeq2Seq(tokenizer=tokenizer, model=model)

# Training arguments (small steps for demo)
# Training arguments (minimal for compatibility)
training_args = TrainingArguments(
    output_dir="./results",
    learning_rate=5e-5,
    per_device_train_batch_size=2,
    num_train_epochs=10,   # increase epochs
    save_total_limit=1,
    logging_dir="./logs",
    logging_steps=10,
)




# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized,
    tokenizer=tokenizer,
    data_collator=data_collator,
)

# Train
trainer.train()

# Save fine-tuned model
model.save_pretrained("./fine_tuned_model")
tokenizer.save_pretrained("./fine_tuned_model")






