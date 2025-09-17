from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

model = AutoModelForSeq2SeqLM.from_pretrained("./fine_tuned_model")
tokenizer = AutoTokenizer.from_pretrained("./fine_tuned_model")

gen = pipeline("text2text-generation", model=model, tokenizer=tokenizer)

print(gen("Suggest a recipe with: rice, carrot, peas")[0]["generated_text"])

# | Test ID | Ingredients Input       | Expected Output Example                                                                             |
# | ------- | ----------------------- | --------------------------------------------------------------------------------------------------- |
# | 1       | egg, onion              | Scrambled eggs with onions: Heat oil, sauté onions, add beaten eggs, cook until set.                |
# | 2       | egg, tomato             | Tomato omelette: Whisk eggs, add chopped tomato, fry until golden.                                  |
# | 3       | egg, spinach            | Spinach egg scramble: Sauté spinach, add eggs, stir until cooked.                                   |
# | 4       | rice, tomato, peas      | Tomato peas pulao: Sauté onions, add peas and tomato, cook rice with water until done.              |
# | 5       | chicken, onion, garlic  | Chicken curry: Sauté onion and garlic, add chicken and spices, simmer 20 mins.                      |
# | 6       | paneer, spinach         | Palak paneer: Sauté onion and garlic, add spinach puree and paneer, simmer 5 mins.                  |
# | 7       | potato, tomato          | Aloo tamatar sabzi: Sauté onion, add boiled potatoes, tomatoes, cook 10 mins with spices.           |
# | 8       | rice, chicken, spices   | Chicken biryani: Marinate chicken, sauté onions, cook chicken, layer with rice, steam 20 mins.      |
# | 9       | fish, garlic, tomato    | Fish curry: Sauté garlic, tomato, add fish, simmer 10 mins.                                         |
# | 10      | shrimp, peas, onion     | Shrimp peas stir fry: Sauté onion, add shrimp and peas, cook 5–7 mins, season with salt and pepper. |
# | 11      | egg, cheese, onion      | Cheese omelette with onions: Sauté onion, pour beaten eggs, add cheese, cook 3–4 mins.              |
# | 12      | rice, carrot, peas      | Vegetable pulao: Sauté carrots and peas, add rice and water, cook until rice is fluffy.             |
# | 13      | chicken, tomato, onion  | Chicken tikka masala: Marinate chicken, sauté onion and tomato, cook chicken, add cream, simmer.    |
# | 14      | paneer, capsicum, onion | Paneer capsicum stir fry: Sauté onion and capsicum, add paneer, cook 5–7 mins.                      |
# | 15      | potato, peas, tomato    | Aloo matar sabzi: Sauté cumin seeds, onion, tomatoes, potatoes, peas, cook 10 mins.                 |
# | 16      | egg, bread, milk        | French toast: Dip bread in beaten egg and milk, fry until golden on both sides.                     |
# | 17      | rice, mushroom, garlic  | Mushroom garlic rice: Sauté mushrooms and garlic, add rice, stir-fry 3–4 mins.                      |
# | 18      | chicken, garlic, chili  | Spicy garlic chicken: Marinate chicken, sauté garlic and chili, cook 15–20 mins.                    |
# | 19      | paneer, tomato, cream   | Paneer butter masala: Sauté onions and tomatoes, add paneer and cream, cook 5 mins.                 |
# | 20      | fish, onion, tomato     | Fish masala curry: Fry onions, add tomatoes and spices, add fish, simmer 10 mins.                   |
