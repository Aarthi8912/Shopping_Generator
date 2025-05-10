# Shopping_Generator

🛍️ AI Shopping Generator Application


This is a smart shopping assistant powered by AI. Users input product preferences, and the app suggests the best matching items using Cohere or Phi agents via a web interface built with Streamlit.

🔗 GitHub Repository:
https://github.com/<your-username>/ShoppingGenerator

-------------------------------------------
📦 Requirements
-------------------------------------------
- Python 3.8 or higher
- Streamlit
- Cohere (or Phi with supported tools like Firecrawl)
- API keys for Cohere (or proper setup for Phi agents)

-------------------------------------------
🚀 Setup Instructions
-------------------------------------------

1. Clone the repository:
   git clone https://github.com/<your-username>/ShoppingGenerator.git
   cd ShoppingGenerator

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate         (on Windows)
   source venv/bin/activate      (on macOS/Linux)

3. Install required packages:
   pip install streamlit cohere

4. Set up your API keys:
   - Open `app.py` (or `shopping.py`)
   - Replace placeholders like `'your-api-key'` with your actual API keys

5. Run the app:
   streamlit run shopping.py

-------------------------------------------
🧠 How It Works
-------------------------------------------
- You enter preferences like product type, budget, color, or features
- The app uses a language model (via Cohere or Phi) to search or generate suitable product options
- Results are neatly displayed in the browser

-------------------------------------------
📝 Example Usage
-------------------------------------------
1. Launch the app:
   streamlit run shopping.py

2. In your browser:
   - Input: `I need black running shoes under Rs. 5000`
   - Click on "🔍 Recommend Products"
   - View product suggestions

-------------------------------------------
🛠 Sample `requirements.txt`
-------------------------------------------
streamlit
cohere


(Adjust based on whether you use Cohere, Phi, or both.)

-------------------------------------------
📄 License
-------------------------------------------
MIT License – open-source and free to use!

-------------------------------------------
🛒 Happy Shopping with AI! 🎯
-------------------------------------------
