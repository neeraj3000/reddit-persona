# 🧠 Reddit Persona Generator

This is an AI-powered web application that analyzes a Reddit user's posts and comments to generate a detailed **User Persona Report**. It uses **LangChain**, **Groq (LLaMA3)**, and **Streamlit** to extract meaningful insights like motivations, behaviors, frustrations, values, and more — making it useful for user research, marketing, and UX design.

---

## ✨ Features

- Accepts any public Reddit profile URL  
- Collects recent posts and comments  
- Uses LLM (Groq / LLaMA3) via LangChain for persona generation  
- Downloadable structured persona report  
- Clean, responsive Streamlit UI  

---

## 🚀 Demo

Try it on your local machine 👇

---

## 🔧 Tech Stack

- [Streamlit](https://streamlit.io/) – For frontend UI  
- [LangChain](https://www.langchain.com/) – LLM orchestration  
- [Groq API](https://console.groq.com/) – Ultra-fast inference using LLaMA3  
- [PRAW (Python Reddit API Wrapper)](https://praw.readthedocs.io/) – Reddit data retrieval  
- [Python Dotenv](https://pypi.org/project/python-dotenv/) – For managing API keys  

---

## 📦 Requirements

- Python 3.8 or higher (recommended: 3.10 or 3.11)

---

## 🛠️ Setup Instructions

### 1. **Clone the repository**

```bash
git clone https://github.com/neeraj3000/reddit-persona.git
cd reddit-persona
```

### 2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
# Activate it:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. **Install dependencies**

```bash
pip install -r requirements.txt
```

### 4. **Set up environment variables**

Create a `.env` file in the root directory and add:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_app_name
groq_api_key=your_groq_api_key
```

> 🔑 Get Groq API key from [console.groq.com](https://console.groq.com/)  
> 🔑 Create a Reddit app at [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps)

---

## 🧪 Run the App

```bash
streamlit run app.py
```

Then open the link in your browser (usually http://localhost:8501)

---

## 📁 Output

- You’ll get a well-structured **Persona Report**
- Option to **Download** the report as a `.txt` file  
- Includes key fields like:  
  - Identity (Name, Age, Occupation, etc.)  
  - Personality & Motivations  
  - Behavior & Frustrations  
  - Citations used from Reddit  

---

## 📸 Screenshot

_Add a screenshot of your app in action here_

---

## 📄 License

MIT License — feel free to use, modify, and share.
