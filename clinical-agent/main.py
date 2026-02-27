from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from tool_agent import run_tool_agent
from explain_agent import explain_disease
from scraper_tool import scrape_disease_info


app = FastAPI()


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)


@app.get("/")
def home():

    return {"message": "Clinical Trial AI Agent Running"}



@app.get("/agent/{disease}")
def agent_trial(disease):

    result = run_tool_agent(disease)

    return result



@app.get("/explain/{disease}")
def explain(disease):

    text = explain_disease(disease)

    return {

        "disease": disease,
        "explanation": text

    }



@app.get("/scrape/{disease}")
def scrape(disease):

    text = scrape_disease_info(disease)

    return {

        "disease": disease,
        "scraped_text": text

    }