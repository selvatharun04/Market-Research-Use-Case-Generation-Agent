from utils.llm import get_gemini_model
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()

def search_with_tavily(query):
    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results = tavily.search(query=query, search_depth='advanced',include_answer=True,max_results=5)
    sources = "\n".join([f"-{result['title']} ({result['url']})" for result in results["results"]])
    return f"{results.get('answer',' ')}\n\nSources:\n{sources}"

def run_industry_research(industry):
    model = get_gemini_model()
    research = search_with_tavily(f"{industry} AI ML Trends and Business overview")
    prompt= f"""
    You are an industry analyst. Based on this data, summarize:
- Industry Overview
- Segement the companies working  in (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare, etc.).
- Company's Key Offerings
- strategic focus areas (e.g., operations, supply chain, customer experience, etc.)
- Strategic Priorities
- Vision and Product Information on the industry should be fine as well
- AI/ML Trends

{research}
"""
    response = model.generate_content(prompt)
    return response.text
    