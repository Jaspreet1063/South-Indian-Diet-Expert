import gradio as gr
import random

# Dictionary of South Indian diet information
south_indian_diet_info = {
    "breakfast": [
        "Idli with Sambar and Coconut Chutney",
        "Dosa with Potato Masala and Tomato Chutney",
        "Upma with mixed vegetables",
        "Pongal with Coconut Chutney",
        "Rava Uttapam with Tomato and Onion"
    ],
    "lunch": [
        "Rice with Sambar, Rasam, and Mixed Vegetable Poriyal",
        "Bisi Bele Bath with Papad and Yogurt",
        "Curd Rice with Pickle and Vegetable Salad",
        "Vegetable Pulao with Raita and Papad",
        "Lemon Rice with Roasted Papad and Vegetable Curry"
    ],
    "dinner": [
        "Chapati with Vegetable Kurma and Cucumber Raita",
        "Millet Dosa with Tomato Chutney and Vegetable Stew",
        "Ragi Mudde with Soppu Saaru (Greens Curry)",
        "Vegetable Uthappam with Coconut Chutney",
        "Adai (Multi-lentil Dosa) with Avial"
    ],
    "healthy_tips": [
        "Include a variety of vegetables in your meals for essential nutrients.",
        "Opt for brown rice or millet instead of white rice for added fiber.",
        "Use coconut oil in moderation for authentic flavor and healthy fats.",
        "Include protein-rich lentils and legumes in your daily diet.",
        "Incorporate yogurt or buttermilk for probiotics and calcium."
    ],
    "low_calorie": [
        "Rasam (spicy tamarind soup)",
        "Vegetable Soup (without cream)",
        "Cucumber Kosambari (salad)",
        "Steamed Idlis",
        "Vegetable Upma (made with less oil)"
    ],
    "protein_sources": [
        "Lentils (Dal)",
        "Chickpeas (Chana)",
        "Tofu curry",
        "Sprouts salad",
        "Buttermilk or Yogurt"
    ]
}

def generate_response(message, history):
    message = message.lower()
    
    if "breakfast" in message:
        return f"For a healthy South Indian breakfast, you could try: {random.choice(south_indian_diet_info['breakfast'])}. Remember to pair it with a small portion of chutney or sambar for a balanced meal."
    
    elif "lunch" in message:
        return f"A typical nutritious South Indian lunch could include: {random.choice(south_indian_diet_info['lunch'])}. This provides a good balance of carbohydrates, proteins, and vegetables."
    
    elif "dinner" in message:
        return f"For dinner, consider having: {random.choice(south_indian_diet_info['dinner'])}. This is a lighter option that's still satisfying and nutritious."
    
    elif "low calorie" in message or "weight loss" in message:
        return f"If you're looking for low-calorie South Indian options, try: {', '.join(random.sample(south_indian_diet_info['low_calorie'], 3))}. These dishes are lighter but still flavorful."
    
    elif "protein" in message:
        return f"To incorporate more protein in your South Indian diet, include foods like: {', '.join(random.sample(south_indian_diet_info['protein_sources'], 3))}. These can be easily incorporated into various South Indian dishes."
    
    elif "tip" in message or "advice" in message:
        return f"Here's a helpful tip for maintaining a healthy South Indian diet: {random.choice(south_indian_diet_info['healthy_tips'])}"
    
    else:
        return "I'm sorry, I didn't quite understand your question. Could you please ask about specific South Indian meals, low-calorie options, protein sources, or general diet tips?"

iface = gr.ChatInterface(
    generate_response,
    title="South Indian Diet Expert",
    description="Ask me about South Indian cuisine, diet plans, and nutritional advice!",
    theme="default",
    examples=[
        "What's a healthy South Indian breakfast?",
        "Can you suggest a South Indian lunch option?",
        "What are some low-calorie South Indian dishes?",
        "How can I incorporate more protein into my South Indian diet?",
        "Any tips for a healthy South Indian diet?"
    ],
    cache_examples=False,
)

iface.launch()