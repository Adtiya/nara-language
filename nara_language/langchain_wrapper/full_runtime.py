"""
LangChain Agent with NĀRA + OpenAI Integration
"""

from langchain.agents import Tool
from langchain.llms import OpenAI
from langchain.agents import initialize_agent

# Dummy NĀRA intent processor
def process_nara(code):
    if "चिन्तायुक्तः" in code:
        return "Activate calm protocol with चक्र सन्तुलन"
    return "Default: apply harmony layer using AI स्मृति"

# Define the NĀRA tool
nara_tool = Tool(
    name="NARA_Healer_Agent",
    func=lambda input: process_nara(input),
    description="Executes spiritual and emotional health logic from Sanskrit `.nara` file"
)

# Initialize LangChain agent
llm = OpenAI(temperature=0)
agent = initialize_agent([nara_tool], llm, agent="zero-shot-react-description", verbose=True)

# Run example
if __name__ == "__main__":
    query = "My energy is blocked, I'm anxious (चिन्तायुक्तः)"
    response = agent.run(query)
    print("💡 Agent Response:", response)
