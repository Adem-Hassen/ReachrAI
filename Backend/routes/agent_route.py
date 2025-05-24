from fastapi import APIRouter,UploadFile,File
from services.agent_services import run_agent
import tempfile


agent_api=APIRouter(prefix="/agent",tags=["AgentAPI"])

@agent_api.post("/")
async def get_companies(resume:UploadFile=File(...)):
    if not resume :
        return {"error":"resume not found"}
    with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf")as temp:
        content=await resume.read()
        temp.write(content)
        resume_path=temp.name
    
    companies=run_agent(resume_path=resume_path)
    return companies
