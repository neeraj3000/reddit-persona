import sys
import asyncio
import os
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableLambda
from langchain_groq import ChatGroq

# Windows event loop fix
if sys.platform.startswith("win"):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Load GROQ API key
GROQ_API_KEY = os.getenv("groq_api_key")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set in environment variables. Set it before running.")

# Prompt template — rich persona format like Lucas Mellor
prompt = PromptTemplate(
    template="""
You are an expert UX researcher. Based on the Reddit posts and comments below, generate a detailed user persona report.

The format should follow this structure:

------------------------
👤 **Identity**
- **Name**:
- **Age**:
- **Occupation**:
- **Status**:
- **Location**:
- **Tier**: (e.g., Early Adopter, Mainstream)
- **Archetype**: (e.g., The Creator, The Explorer)
- **Traits**: (e.g., Practical, Adaptable, Spontaneous...)

💡 **Motivations**
- Convenience: (1-5 scale)
- Wellness:
- Speed:
- Preferences:
- Comfort:
- Dietary Needs:

🧠 **Personality**  
(Indicate where they fall on each scale)
- Introvert ⇄ Extrovert  
- Sensing ⇄ Intuition  
- Thinking ⇄ Feeling  
- Judging ⇄ Perceiving  

🧍‍♂️ **Behaviour & Habits**  
Write 3-5 bullet points summarizing lifestyle patterns, digital usage, routines, etc.

💥 **Frustrations**  
Summarize key pain points. Use bullet points.

✅ **Goals & Needs**  
Summarize aspirations and needs. Use bullet points.

🔗 **Citations**
List **exact Reddit URLs** used in the analysis. Only include links found in the input content.

(If there’s anything unique or interesting about this person that doesn’t fit in the above categories, include it in any relevant section.)

------------------------

Reddit User Content:
------------------------
{reddit_text}
""",
    input_variables=["reddit_text"]
)

# Groq LLaMA3 LLM
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama3-70b-8192",
    temperature=0.4
)

# LangChain pipeline
def build_chain():
    return (
        RunnableLambda(lambda input: {"reddit_text": input})
        | RunnableLambda(lambda d: {"prompt": prompt.format(**d)})
        | RunnableLambda(lambda d: {"structured": llm.invoke(d["prompt"]).content})
    )

chain = build_chain()
