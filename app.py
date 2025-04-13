import streamlit as st 
from agents.industry_research_agent import run_industry_research
from agents.usecase_generator_agent import run_usecase_generator
from agents.resource_collector_agent import run_resource_collector
from agents.genai_solutions_agents import run_genai_solutions

st.title("Market Research & Use Case Generation Agent")

industry = st.text_input("Enter the industry or company you want to research:")

if st.button("Generate"):
    with st.spinner("Researching the industry..."):
        summary = run_industry_research(industry)
        st.subheader("\U0001F50D Industry Research")
        st.markdown(summary)

    with st.spinner("Generating use cases..."):
        usecases = run_usecase_generator(summary)
        st.subheader("\U0001F4A1 AI/ML Use Cases")
        st.markdown(usecases)

    with st.spinner("Finding datasets..."):
        datasets = run_resource_collector(usecases)
        st.subheader("📂 Related Datasets & Projects")
        st.markdown(datasets, unsafe_allow_html=True)

    with st.spinner("Suggesting GenAI tools..."):
        genai_solutions = run_genai_solutions(summary)
        st.subheader("🤖 GenAI Tool Suggestions")
        st.markdown(genai_solutions)