from fastapi import FastAPI
from routes.agent_route import agent_api

app=FastAPI()
app.include_router(agent_api)







