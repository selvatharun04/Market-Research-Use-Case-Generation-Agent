# 🧠 GenAI Multi-Agent Use Case Generator

This project is a multi-agent AI system built using LangChain, Google Gemini Pro, Tavily API, and Streamlit. It dynamically generates AI/ML/GenAI use cases for any industry or company, along with related datasets, open-source resources, and GenAI solution ideas.

## 🚀 Features

- Real-time industry research using Tavily web search
- Use case generation using Gemini LLM
- Relevant dataset lookup from Kaggle, HuggingFace, GitHub
- GenAI tool suggestions like chatbots, RAG systems, and report generators
- Streamlit-based user interface

## 🛠️ Tech Stack

| Component        | Tool / Library               |
|------------------|-------------------------------|
| Language Model   | Google Gemini Pro             |
| Agent Framework  | LangChain                     |
| Web Search       | Tavily API                    |
| Frontend UI      | Streamlit                     |
| Dataset Lookup   | Kaggle, HuggingFace, GitHub   |

## 📁 Project Structure

```
genai-multiagent-app/
├── app.py
├── requirements.txt
├── .env.template
├── utils/
│   └── llm.py
├── agents/
│   ├── industry_research_agent.py
│   ├── usecase_generator_agent.py
│   ├── resource_collector_agent.py
│   └── genai_solutions_agent.py
└── README.md
```

## ⚙️ How to Run

1. Clone the repo and install requirements:

   ```bash
   git clone https://github.com/yourusername/genai-multiagent-app.git
   cd genai-multiagent-app
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

2. Add your API keys to .env:

   ```env
   GEMINI_API_KEY=your_gemini_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

3. Start the app:

   ```bash
   streamlit run app.py
   ```

## 🧠 How It Works

- User enters an industry (e.g., Healthcare)
- Research agent uses Tavily to gather live web data
- Gemini LLM processes that info to generate insights
- Use case agent creates practical AI/ML/GenAI use cases
- Dataset agent links relevant public datasets
- GenAI agent proposes tools like RAG systems, bots, and auto-report generators

