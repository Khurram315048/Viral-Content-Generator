import streamlit as st
from app.agent import build_agent_graph
from app.memory import get_past_interactions

st.set_page_config(page_title="TrendPilot: Reel Agent",layout="wide")

st.title("🚀 TrendPilot: Agentic AI for Instagram Reels")
st.markdown("Build By Muhammad Khurram-AI/ML Intern")
st.markdown("Enter any topic below. The AI agent will plan,script,review, and save a complete viral content package.")


with st.sidebar:
    st.header("⚙️ Configuration")
    tone=st.selectbox("Select Tone",["High-Energy & Hyped","Professional & Educational","Humorous & Casual","Inspirational"])
    st.info("Ensure Ollama is running (`ollama run gemma3:4b`) in your terminal.")

    st.divider()
    st.header("🧠Recent Memory")
    try:
        past_runs=get_past_interactions(limit=10)
        if past_runs:
            for idx,run in enumerate(past_runs,1):
                topic_name,tone_val,out_type,content,timestamp=run
                with st.expander(f"{idx}. {topic_name} ({tone_val})"):
                    st.caption(f"**Saved At:** {timestamp} | **Type:** {out_type}")
                    st.markdown(content) 
        else:
            st.caption("No history in memory yet.")
    except Exception as e:
        st.caption(f"Loading memory... (Run a generation first)")
    
    # st.divider()
    # st.header("🧠 Agent Memory (Recent)")
    # try:
    #     all_memory=get_past_interactions(limit=20)
    #     if all_memory:
    #         for idx,run in enumerate(all_memory,1):
    #             st.markdown(f"**{idx}. Topic:** {run[0]}")
    #             st.caption(f"Tone: {run[1]} | Type: {run[2]} | Saved At: {run[3]}")
    #             st.divider()
    #     else:
    #         st.info("No past runs found")        
    #     recent_runs=get_past_interactions(limit=5)

    # except Exception as e:
    #     st.caption("Memory DB not initialized yet.")


topic_input=st.text_input("Enter your topic (e.g.,'Python coding mistakes','Gym routines'):")


if st.button("Generate Viral Reel Plan",type="primary"):

    if not topic_input.strip():
        st.warning("Please enter a valid topic first.")
    else:
        with st.spinner("Agent is reasoning,calling tools,and generating content..."):
            agent_app=build_agent_graph()
            initial_state={
                "topic":topic_input,
                "tone":tone,
                "trends":"",
                "script":"",
                "hashtags":"",
                "review":"",
                "saved_path":"",
                "logs":[]
            }
            result=agent_app.invoke(initial_state)
            st.success("Agent execution complete!")
            
            with st.expander("🔍 View Agent Execution Logs (Tool Routing)",expanded=False):
                for log in result["logs"]:
                    st.code(log,language="text")
            
           
            col1,col2=st.columns(2)
            with col1:
                st.subheader("💡 Viral Concepts")
                st.markdown(result["trends"])
                st.subheader("🏷️ Targeted Hashtags")
                st.markdown(result["hashtags"])
            with col2:
                st.subheader("🎬 Reel Script")
                st.markdown(result["script"])
                st.subheader("⭐ Agent Review")
                st.markdown(result["review"])
                
            st.divider()
            st.success(f"📁 Successfully saved Markdown output to:`{result['saved_path']}`")