"""
LangChain wrapper for running `.nara` agents
"""

def parse_nara_to_tool(nara_code: str):
    tool = {
        "name": "nara_agent",
        "description": "Executes intention from NĀRA Sanskrit script",
        "run": lambda input: "समानुभूति मार्गदर्शः प्रारभ्यते" if "चिन्तायुक्तः" in nara_code else "AI स्मृति कार्यान्वितम्"
    }
    return tool

# Usage (simulated)
if __name__ == "__main__":
    code = open("../examples/healer_agent.nara", encoding="utf-8").read()
    agent = parse_nara_to_tool(code)
    print("🧠 Agent Response:", agent["run"]("चिन्तायुक्तः"))
