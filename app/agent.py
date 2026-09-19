from typing import TypedDict,List
from langgraph.graph import StateGraph,END
from app.tools import(generate_trend_ideas,generate_reel_script,generate_hashtags,review_content,save_to_file)
from app.memory import save_interaction

class AgentState(TypedDict):
    topic:str
    tone:str
    trends:str
    script:str
    hashtags:str
    review:str
    saved_path:str
    logs:List[str]


def node_trend_generator(state:AgentState):
    print("Node Start:")
    state["logs"].append("[Tool called]: Trend Idea Generator")
    state["trends"]=generate_trend_ideas(state["topic"],state["tone"])
    print("Node End.")
    return state


def node_script_writer(state:AgentState):
    state["logs"].append("[Tool called]: Reel Script Writer")
    state["script"]=generate_reel_script(state["trends"],state["tone"])
    return state

def node_hashtag_generator(state:AgentState):
    state["logs"].append("[Tool called]: Hashtag Generator")
    state["hashtags"]=generate_hashtags(state["topic"])
    return state

def node_reviewer(state:AgentState):
    state["logs"].append("[Tool called]: Content Review")
    combined_content=f"Script;\n{state['script']}\n\nHashtags:\n{state['hashtags']}"
    state["review"]=review_content(combined_content)
    return state


def node_file_saver(state:AgentState):
    state["logs"].append("[Tool called]: File Saver & Memor")
    full_output=(
        f"#Viral Reel Plan: {state['topic']}\n\n"
        f"##Trends\n{state['trends']}\n\n"
        f"##Scripts\n{state['script']}\n\n"
        f"##Hashtags\n{state['hashtags']}\n\n"
        f"##Review\n{state['review']}\n\n"
    )
    save_to_file(state["topic"],state["script"],output_type="script")
    save_to_file(state["topic"],state["review"],output_type="post")
    saved_file_path=save_to_file(state["topic"],full_output,output_type="saved_results")
    state["saved_path"]=saved_file_path
    # state["saved_path"]=save_to_file(state["topic"],full_output,output_type="script")
    save_interaction(state["topic"],state["tone"],"Reel Script",full_output)
    return state

def build_agent_graph():
    workflow=StateGraph(AgentState)
    workflow.add_node("trend_generator",node_trend_generator)
    workflow.add_node("script_writer",node_script_writer)
    workflow.add_node("hashtag_generator",node_hashtag_generator)
    workflow.add_node("reviewer",node_reviewer)
    workflow.add_node("file_saver",node_file_saver)
    
    workflow.set_entry_point("trend_generator")
    workflow.add_edge("trend_generator","script_writer")
    workflow.add_edge("script_writer","hashtag_generator")
    workflow.add_edge("hashtag_generator","reviewer")
    workflow.add_edge("reviewer","file_saver")
    workflow.add_edge("file_saver",END)

    return workflow.compile()

