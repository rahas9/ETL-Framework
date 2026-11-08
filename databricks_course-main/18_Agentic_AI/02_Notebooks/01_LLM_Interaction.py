# Databricks notebook source
from openai import OpenAI
import os

# How to get your Databricks token: https://docs.databricks.com/en/dev-tools/auth/pat.html
#DATABRICKS_TOKEN = os.environ.get('DATABRICKS_TOKEN')
# Alternatively in a Databricks notebook you can use this:
DATABRICKS_TOKEN = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()

client = OpenAI(
    api_key=DATABRICKS_TOKEN,
    base_url="https://150511393544475.ai-gateway.cloud.databricks.com/mlflow/v1"
)

response = client.chat.completions.create(
    model="databricks-gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "why are ai agents gettign popular. out put shall be brief"
        }
    ],
    max_tokens=5000
)

print(response.choices[0].message.content)

# COMMAND ----------

print(response.choices[0].message.content[1].get("text"))

# COMMAND ----------

# MAGIC %md
# MAGIC AI agents are gaining popularity because they:
# MAGIC
# MAGIC - **Automate complex tasks** — handle scheduling, data analysis, and customer support without constant human oversight.  
# MAGIC - **Boost productivity** — integrate with tools (email, calendars, APIs) to streamline workflows.  
# MAGIC - **Offer personalization** — adapt responses to user preferences and context.  
# MAGIC - **Scale knowledge** — leverage large language models to provide up‑to‑date information across domains.  
# MAGIC - **Lower entry barriers** — user‑friendly interfaces let non‑technical people deploy powerful automation.  
# MAGIC - **Drive innovation** — enable new services (e.g., autonomous agents, digital assistants) that were previously impractical.

# COMMAND ----------

# MAGIC %sql
# MAGIC select ai_query('databricks-gpt-oss-120b','why are ai agents gettin =g popular')

# COMMAND ----------

# MAGIC %md
# MAGIC **Why AI agents are becoming so popular**
# MAGIC
# MAGIC 1. **Rapid advances in core technology**  
# MAGIC    - **Large language models (LLMs)** such as GPT‑4, Claude, LLaMA 2 can understand and generate human‑like text, making agents far more capable than earlier rule‑based bots.  
# MAGIC    - **Multimodal models** (text + image + audio) let agents perceive and act across many data types.  
# MAGIC    - **Reinforcement‑learning‑from‑human‑feedback (RLHF)** and fine‑tuning improve safety, alignment, and task‑specific performance.
# MAGIC
# MAGIC 2. **Massively increased compute & data**  
# MAGIC    - Cloud providers now offer cheap, on‑demand GPU/TPU clusters, lowering the barrier to train or run sophisticated agents.  
# MAGIC    - Public datasets (web text, code, images, conversational logs) give models the breadth needed for general‑purpose reasoning.
# MAGIC
# MAGIC 3. **Clear business value**  
# MAGIC    - **Automation of repetitive tasks** (customer support, scheduling, data entry) cuts labor costs and speeds response times.  
# MAGIC    - **Decision‑support** (drafting contracts, code generation, market analysis) augments human expertise, increasing productivity.  
# MAGIC    - **Personalization**: agents can tailor recommendations, tutoring, or health advice to individual users, driving higher engagement and satisfaction.
# MAGIC
# MAGIC 4. **Ease of integration**  
# MAGIC    - **APIs and SDKs** (OpenAI, Anthropic, Cohere, Azure AI) let developers embed agents in apps, websites, and internal tools with just a few lines of code.  
# MAGIC    - **Tool‑use extensions** (retrieval‑augmented generation, code execution, web browsing) enable agents to fetch up‑to‑date information or perform actions beyond pure language generation.
# MAGIC
# MAGIC 5. **User‑centric experiences**  
# MAGIC    - Conversational interfaces feel natural; people can “talk” to software instead of learning complex UIs.  
# MAGIC    - Voice assistants (Alexa, Siri, Google Assistant) have familiarized the public with AI‑driven interaction, paving the way for more capable agents.
# MAGIC
# MAGIC 6. **Open‑source momentum**  
# MAGIC    - Projects like **LangChain**, **AutoGPT**, **Agentic‑LLM** frameworks provide reusable building blocks for creating autonomous agents.  
# MAGIC    - Community‑driven models (e.g., LLaMA 2, Mistral) lower cost and encourage experimentation, accelerating adoption.
# MAGIC
# MAGIC 7. **Regulatory and ethical focus**  
# MAGIC    - Growing standards for transparency, data privacy, and AI safety give enterprises confidence to deploy agents responsibly, reducing earlier legal hesitations.
# MAGIC
# MAGIC 8. **Cultural hype & media coverage**  
# MAGIC    - High‑profile demos (ChatGPT, DALL·E, GitHub Copilot) showcase tangible capabilities, sparking curiosity among developers, investors, and the general public.  
# MAGIC    - Venture capital funding has surged, creating a feedback loop of research, productization, and publicity.
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC ### Bottom line
# MAGIC AI agents are popular because the **technology has finally caught up with real‑world needs**: they’re more capable, cheaper to run, easy to integrate, and deliver measurable business and user benefits. The combination of technical breakthroughs, ecosystem support, and market demand creates a virtuous cycle that continues to drive rapid adoption.