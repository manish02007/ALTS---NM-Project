!pip install transformers sentencepiece --quiet

from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch

# Load model & tokenizer
model_name = "facebook/mbart-large-50-many-to-many-mmt"
tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
model = MBartForConditionalGeneration.from_pretrained(model_name)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Language codes for Indian languages + English
LANGUAGE_CODES = {
    "English": "en_XX",
    "Hindi": "hi_IN",
    "Tamil": "ta_IN",
    "Malayalam": "ml_IN",
    "Telugu": "te_IN",
    "Bengali": "bn_IN",
    "Marathi": "mr_IN",
    "Gujarati": "gu_IN",
    "Punjabi": "pa_IN",
    "Urdu": "ur_IN"
}

def translate(text, src_lang, tgt_lang):
    if src_lang not in LANGUAGE_CODES or tgt_lang not in LANGUAGE_CODES:
        return "Unsupported language"
    text = text.strip()
    if text[-1] not in [".", "!", "?"]:
        text += "."
    tokenizer.src_lang = LANGUAGE_CODES[src_lang]
    encoded = tokenizer(text, return_tensors="pt").to(device)
    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.lang_code_to_id[LANGUAGE_CODES[tgt_lang]]
    )
    return tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

# Interactive example:
print("Supported languages:", list(LANGUAGE_CODES.keys()))
src_lang = input("Enter source language: ")
tgt_lang = input("Enter target language: ")
text = input("Enter text to translate: ")

translation = translate(text, src_lang, tgt_lang)
print(f"\n{src_lang} ➡ {tgt_lang}: {translation}")
