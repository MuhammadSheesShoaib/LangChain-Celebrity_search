# 🌟 LangChain Celebrity Search  

This is a **Streamlit web app** that uses **LangChain and Groq API** to fetch information about celebrities. Just enter a celebrity's name, and the app will generate details about them.  

---

## 📌 Features  
- ✅ **Search for any celebrity** using AI  
- ✅ **Powered by LangChain & Groq API**  
- ✅ **Simple and interactive Streamlit UI**  

---

## 🛠️ Installation & Setup  

### 1️⃣ **Clone the Repository**  
First, download the project files:  
```bash
git clone https://github.com/MuhammadSheesShoaib/LangChain-Celebrity_search.git
cd LangChain-Celebrity_search
```
2️⃣ Install Dependencies
Ensure you have Python 3.8+ installed, then run:

```bash
pip install -r requirements.txt
```
3️⃣ Set Up the API Key
The project requires a Groq API Key to function.

Create a file called constant.py in the project folder.
Open constant.py and add the following line:
groq_api = "your_groq_api_key_here"
Replace "your_groq_api_key_here" with your actual Groq API Key.

🚀 Running the App
Once everything is set up, run the Streamlit app using:

```bash
streamlit run groq_main.py
```
This will open the app in your browser, where you can search for any celebrity!
