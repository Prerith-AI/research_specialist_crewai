import os
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()
## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.6,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Modified researcher agent to focus on scientific papers
research_specialist = Agent(
    role="Scientific Research Specialist",
    goal='Conduct comprehensive research on {topic} and identify 3-5 most impactful scientific papers',
    verbose=True,
    memory=True,
    backstory=(
        "You are an expert research scientist with extensive experience in academic literature review. "
        "Your specialty lies in identifying groundbreaking peer-reviewed research papers and "
        "analyzing their scientific significance. You always provide direct links to papers and "
        "ensure they are from reputable scientific journals."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Modified writer agent to focus on scientific paper analysis
research_analyst = Agent(
    role='Research Analyst',
    goal='Synthesize and analyze the scientific papers about {topic} with detailed methodology and findings',
    verbose=True,
    memory=True,
    backstory=(
        "You are a specialized research analyst with a PhD in scientific communication. "
        "Your expertise lies in breaking down complex scientific papers into comprehensive analyses, "
        "highlighting key methodologies, findings, and their implications. You always maintain "
        "scientific accuracy while making the content accessible."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)
