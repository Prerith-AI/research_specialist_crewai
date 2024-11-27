from crewai import Task
from tools import tool
from agents import research_specialist, research_analyst

# Research task for identifying scientific papers
research_task = Task(
    description=(
        "Conduct a thorough literature review on {topic}. "
        "Identify 3-5 most impactful and recent peer-reviewed scientific papers. "
        "For each paper, provide: "
        "1. Direct link to the paper "
        "2. Brief overview of its significance "
        "3. Why it's considered impactful in the field "
        "Ensure all sources are from reputable scientific journals."
    ),
    expected_output='A detailed list of 3-5 significant scientific papers with links, summaries, and impact analysis.',
    tools=[tool],
    agent=research_specialist,
)

# Analysis task for scientific paper synthesis
write_task = Task(
    description=(
        "Analyze the identified scientific papers on {topic}. "
        "Create a comprehensive synthesis that includes: "
        "1. Detailed breakdown of research methodologies "
        "2. Key findings and their significance "
        "3. Implications for the field "
        "4. Comparative analysis of the different approaches "
        "Make the analysis accessible while maintaining scientific accuracy."
    ),
    expected_output='A detailed scientific analysis document with methodology breakdowns, findings, and implications, formatted in markdown.',
    tools=[tool],
    agent=research_analyst,
    async_execution=False,
    output_file='research-analysis.md'
)