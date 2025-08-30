# Coding-Tutor-Agent
AI Coding Tutor

AI Coding Tutor is a Streamlit web app that helps developers understand their code or errors. You can paste code, ask the tutor to explain it, get fixes, and see suggestions for improvements.

Features

Code explanation: Understand what your code does and why errors occur.

Fix suggestions: Get actionable fixes for your code errors.

Improvements: Receive optimized or cleaner code suggestions.

Supports multiple languages: Works with common programming languages like Python, C++, etc.

Installation

Clone the repository:

git clone https://github.com/yourusername/ai-coding-tutor.git
cd ai-coding-tutor


Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies:

pip install -r requirements.txt


Add your API key in secrets.toml or .env (recommended):

# secrets.toml
TUTOR_API_KEY="your_api_key_here"

Usage

Run the Streamlit app:

streamlit run app.py


Paste your code or error into the text area.

Click Ask Tutor to get explanations, fixes, and improvements.

Click Clear to reset the text area.
