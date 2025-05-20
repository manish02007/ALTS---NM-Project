# Multilingual Indian Language Translator using MBart

## Overview
This Python script leverages Facebook's **MBart-large-50** multilingual model to perform translation between English and multiple Indian languages (and vice versa). It supports bidirectional translation, allowing conversion from English to Indian languages and from Indian languages back to English with good quality and fluency.

---

## Features

- Supports 10+ languages including English, Hindi, Tamil, Telugu, Bengali, Marathi, Malayalam, Gujarati, Punjabi, and Urdu.
- Bidirectional translation: English ↔ Indian languages.
- Uses state-of-the-art transformer-based MBart model.
- Simple interactive command-line interface for quick translations.
- Automatically handles sentence punctuation for better translation results.
- Runs on CPU or GPU (if available).

---

## Requirements

- **Operating System:** Linux, macOS, or Windows
> **Disclaimer**  
> If you are using **Linux** or **macOS**, it is recommended to perform the following steps within a **virtual environment** to avoid conflicts with system-wide packages.
- Python 3.7 or higher  
- `transformers` library  
- `sentencepiece` library  
- PyTorch (`torch`)  
- Internet connection (for downloading pretrained models)

Install dependencies using pip:

```bash
pip install transformers sentencepiece torch
```

Clone the repository:
   ```bash
   git clone https://github.com/manish02007/Naan-Mudhalvan---NLP.git
   ```
Navigate to the project directory:
   ```bash
   cd Naan-Mudhalvan---NLP
   ```
Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
> **NOTE**  
> *To Use GPU Acceleration (NVIDIA CUDA):*
> If you have an NVIDIA GPU and want to use CUDA for acceleration, install the appropriate version of PyTorch manually.
> Visit the official PyTorch installation page to get the correct command for your system: https://pytorch.org/get-started/locally

Run translator by:
   ```bash
   python alts.py
   ```
