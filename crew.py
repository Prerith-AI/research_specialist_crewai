from crewai import Crew,Process
from tasks import research_task,write_task
from agents import research_specialist ,research_analyst

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[research_specialist ,research_analyst],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Small Language Models'})
print(result)