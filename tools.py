from decouple import config
import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import YouTubeSearchTool


os.environ["OPENAI_API_KEY"] = config("OPENAI_API_KEY")


class Brain:
    def __init__(self,):
        self.yt_tool = YouTubeSearchTool()
        
    def create_learning_path(self, query):
        # Define your agents with roles and goals
        researcher = Agent(
            role='Learning Path Specialist',
            goal='Create a comprehensive learning path for a given subject',
            backstory="""You have years of experience in educational technology and curriculum design. 
            Your expertise lies in identifying relevant resources and building effective learning paths. 
            You have a knack for understanding individual learning needs and tailoring recommendations accordingly.""",
            verbose=True,
            allow_delegation=False,
            tools=[self.yt_tool]
        )
        
        # Create tasks for your agents
        task1 = Task(
            description=query,
            agent=researcher
        )
        
        # Instantiate your crew with a sequential process
        crew = Crew(
            agents=[researcher,],
            tasks=[task1,],
            verbose=2, # You can set it to 1 or 2 to different logging levels
        )
        
        # Get your crew to work!
        result = crew.kickoff()

        return result
        
    def get_yt_videos(self, query):
        result = self.yt_tool.run(query)
        return result


