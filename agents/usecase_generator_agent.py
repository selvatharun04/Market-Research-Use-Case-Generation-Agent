from utils.llm import get_gemini_model

def run_usecase_generator(industry_summary):
    model = get_gemini_model()
    prompt = f"""
    You are a GenAI Strategist. Based  on the industry report, Propose AI/ML/GenAI Use cases.
    And Also Discuss How  these use cases can be helpful to improve mprove their processes, enhance customer satisfaction, and boost operational efficiency
    Organize like :
    -Title
    -Description
    -Value to Business
    -Category where it will be helpful
    
 {industry_summary}
 """
    return model.generate_content(prompt).text
