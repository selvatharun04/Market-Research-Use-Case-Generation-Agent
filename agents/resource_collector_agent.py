def search_kaggle(query):
    return  f"https://www.kaggle.com/search?q={query.replace(' ', '+')}"

def search_huggingface(query):
    return f"https://huggingface.co/datasets?search={query.replace(' ', '+')}"

def run_resource_collector(usecase_summary):
    lines = usecase_summary.split("\n")
    keywords = [line.strip() for line in lines if line and not line.startswith("-")][:5]
    output = "### Datasets:\n"
    for kw in keywords:
        output += f"- {kw}\n  - [Kaggle]({search_kaggle(kw)})\n  - [HuggingFace]({search_huggingface(kw)})\n"
    return output
