from dotenv import load_dotenv
from agent.model import create_model
from serpapi import GoogleSearch
import os

load_dotenv()
def extract_keywords(text):
    prompt=f"Extract 5 to 10 relevant keywords that best describe this resume text :{text}"
    model=create_model()
    response=model.invoke(prompt)
    return(response.content)

def companies_search(keywords):
    query=f"{keywords} site:linkedin.com/company"
    params={
        "engine":"google",
         "q":query,
         "api_key":os.environ.get("SERP_API")
}
    
    try:
        search=GoogleSearch(params)
        results=search.get_dict()
        companies_links=[]
        for result in results.get("organic_results",[]):
            companies_links.append({"name":result.get("title"),"link":result.get("link"),"about":result.get("snippet")})
        return companies_links
        
    except Exception as e:
        return {"error":e}
             

        


    

