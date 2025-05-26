from dotenv import load_dotenv
from agent.model import create_model
from serpapi import GoogleSearch
import os

load_dotenv()
def extract_keywords(text):
    if not text or not text.strip():
        return {"error":"no resume provided"}

    prompt=f"Extract 5 to 10 relevant keywords that best describe this resume text(return the keywords in format that best suit googleSearch with no extra informations ):{text}"
    model=create_model()
    response=model.invoke(prompt)
    return(response.content)

def companies_search(keywords,country):
    query = (
        f'site:linkedin.com/company '
        f'("{keywords}" OR "startup" OR "company") '
        f'("{country}" OR "based in {country}")'
        
    )
    params={
        "engine":"google",
         "q":query,
         "api_key":os.environ.get("SERP_API") , 
          }
    
    try:
        model=create_model()
        
        search=GoogleSearch(params)
        results=search.get_dict()
        companies=[]
       
        for result in results.get("organic_results",[]):
            companies.append({"name":result.get("title"),"link":result.get("link"),"about":result.get("snippet")})
        
        return companies
        
    except Exception as e:
        return {"error":e}
             

        


    

