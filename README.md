# DevRise-Task-3-AI-Career-Assistant
An intelligent AI Career Assistant built with Python and Streamlit, powered by Gemini, Groq, and Mistral LLMs. Features conversational memory, ChatGPT-inspired UI, chat history, and personalized career guidance.

# 🤖 AI Career Assistant

An intelligent **AI Career Assistant** built with **Python** and **Streamlit**, powered by multiple Large Language Models (**Google Gemini, Groq, and Mistral**). The application provides personalized career guidance, programming assistance, interview preparation, and maintains long-term user memory for more contextual conversations.

---

> ## ⚠️ Important
>
> This project is fully configured and ready to use.
>
> **The only setup required is adding your own API keys** in a `.env` file. Everything else is already configured.
>
> After adding your API keys, simply install the dependencies and run:
>
> ```bash
> streamlit run app.py
> ```

---

# ✨ Features

- 🤖 Multi-LLM Support
  - Google Gemini
  - Groq
  - Mistral AI

- 💬 Modern ChatGPT-inspired Interface

- 🧠 Long-Term Memory
  - Automatically extracts important user information
  - Stores personalized user memory
  - Displays memory in JSON format

- 💼 Career Guidance
  - Resume Review
  - Career Advice
  - Interview Preparation
  - Job Guidance

- 💻 Programming Assistance
  - Python
  - Artificial Intelligence
  - Machine Learning
  - Data Science
  - Web Development

- 📜 Chat History

- 🎨 Professional Dark Theme

- ⚡ Fast and Responsive Streamlit UI

---

# 📸 Screenshots

## Home Page

![Home](screenshots/home.png)

---

## Chat Interface

![Chat](screenshots/chat.png)

---

## User Memory

![Memory](screenshots/memory.png)

---

## Model Selection

![Models](screenshots/models.png)

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- Groq API
- Mistral API
- CSS
- JSON
- python-dotenv

---

# 📂 Project Structure

```
AI-Career-Assistant/
│
├── app.py
├── chatbot.py
├── memory.py
├── config.py
├── prompts.py
├── style.css
├── requirements.txt
├── README.md
├── .env.example
│
├── providers/
│   ├── gemini_provider.py
│   ├── groq_provider.py
│   └── mistral_provider.py
│
├── screenshots/
│   ├── home.png
│   ├── chat.png
│   ├── memory.png
│   └── models.png
│
└── assets/
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/KGF-GARUDA/AI-Career-Assistant.git

cd AI-Career-Assistant
```

---

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

Create a `.env` file in the project root and add your own API keys.

```env
GEMINI_API_KEY=your_gemini_api_key

GROQ_API_KEY=your_groq_api_key

MISTRAL_API_KEY=your_mistral_api_key
```

### That's it! 🎉

No additional configuration is required.

Simply run:

```bash
streamlit run app.py
```

---

# 💡 How to Use

1. Launch the application.
2. Select your preferred AI model.
3. Start chatting with the assistant.
4. Ask career-related questions.
5. Get programming help.
6. Receive resume and interview guidance.
7. The assistant automatically remembers important information for personalized conversations.

---

# 🎯 Key Features

✔ Multiple AI Models

✔ ChatGPT-like User Interface

✔ Long-Term User Memory

✔ Chat History

✔ Career Guidance

✔ Programming Support

✔ Resume Assistance

✔ Interview Preparation

✔ JSON Memory Viewer

✔ Responsive Dark Theme

---

# 📈 Future Improvements

- Voice Input
- Voice Output
- PDF Resume Analysis
- Job Recommendation System
- Export Chat as PDF
- Multiple Chat Sessions
- Authentication System
- Docker Support
- Cloud Deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Create a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Kanishk Singh

**MCA Graduate | AI & Machine Learning Enthusiast | AWS Certified Cloud Practitioner**

### Connect with me

- 💼 LinkedIn: https://www.linkedin.com/in/kanishk-singh2000
- 💻 GitHub: https://github.com/KGF-GARUDA

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

It helps support the project and motivates future development.

---

## 📌 Project Highlights

- ✅ Python + Streamlit
- ✅ Google Gemini Integration
- ✅ Groq Integration
- ✅ Mistral Integration
- ✅ Modern ChatGPT-like UI
- ✅ Persistent User Memory
- ✅ Career Assistance
- ✅ AI-Powered Conversations
- ✅ Easy Setup (Only API Keys Required)
- ✅ Portfolio-Ready Project
