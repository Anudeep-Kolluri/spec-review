import streamlit as st
import os

from crewai import Crew
from crewai_tools import ScrapeWebsiteTool, SerperDevTool

from agents import TechAgents
from tasks import TechTasks

from langchain_openai import ChatOpenAI

st.set_page_config(page_title="SpecReview", page_icon="🔥", layout="centered", initial_sidebar_state="expanded")

# Sidebar
st.sidebar.header("Configuration")
st.session_state.openai_key = st.sidebar.text_input("API Key", type="password")
st.session_state.serper_key = st.sidebar.text_input("Serper Key", type="password")

st.session_state.llm_model_name = st.sidebar.selectbox(
    "Select Model",
    options=["gpt-3.5-turbo", "gpt-4", "gpt-4o"],
    index=0  # Default is the first option which is "gpt-3.5-turbo"
)


if st.sidebar.button("Configure") and st.session_state.openai_key and st.session_state.serper_key:

    os.environ["SERPER_API_KEY"] = st.session_state.serper_key

    st.session_state.llm = ChatOpenAI(
        model=st.session_state.llm_model_name,
        api_key=st.session_state.openai_key
    )
    st.toast(f"Configuration is successful, running on {st.session_state.llm_model_name}", icon='😍')

# Main Section
st.title("SpecReview")
st.subheader("In-depth Laptop Comparison")
st.write("It is recommended to use gpt-4o model to perform this task")

col1, col2 = st.columns(2)

with col1:
    st.session_state.item1 = st.text_area("Laptop 1", height=150)

with col2:
    st.session_state.item2 = st.text_area("Laptop 2", height=150)

if st.button("Compare"):
    search_tool = SerperDevTool()
    scrape_tool = ScrapeWebsiteTool()
    tools = [search_tool, scrape_tool]

    if (not st.session_state.openai_key) or (not st.session_state.serper_key):
        st.write("Check api keys")
    else:
        agents = TechAgents(st.session_state.llm, tools)
        tasks = TechTasks(tools)

        researcher = agents.researcher()
        writer = agents.writer()
        
        product1_research = tasks.gather_information(agent = researcher)
        product2_research = tasks.gather_information(agent = researcher)

        document1 = tasks.format_text(agent = writer)
        document1.context = [product1_research]
        document2 = tasks.format_text(agent = writer)
        document2.context = [product2_research]

        crew1 = Crew(
            agents = [researcher],
            tasks = [product1_research, document1],
            verbose = True
        )

        crew2 = Crew(
            agents = [researcher],
            tasks = [product2_research, document2],
            verbose = True
        )

        if (not st.session_state.item1) or (not st.session_state.item2):
            st.write("Text fields cannot be empty")
        
        else:
            print(st.session_state.item1)
            result1 = crew1.kickoff(inputs = {"item" : st.session_state.item1})
            result2 = crew2.kickoff(inputs = {"item" : st.session_state.item2})


            with open("result1.txt", 'w') as file:
                file.write(result1)

            with open("result2.txt", 'w') as file:
                file.write(result2)

            with col1:
                st.write(result1)
            
            with col2:
                st.write(result2)

            print("END OF QUERY")