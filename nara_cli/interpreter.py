import re
import json

memory = {}

def run_nara_code(code: str):
    print("🔍 Interpreting NĀRA code...\n")

    # Parse agent
    agent_match = re.search(r"पुरुषः (.*?) अस्ति", code)
    if agent_match:
        agent_name = agent_match.group(1)
        print(f"🧠 Agent: {agent_name}")

    # Parse traits
    traits = re.findall(r"गुणाः: \[(.*?)\]", code)
    if traits:
        trait_list = [t.strip('" ') for t in traits[0].split(',')]
        print(f"✨ Traits: {trait_list}")

    # Simulate memory input
    input_context = "चिन्तायुक्तः"
    memory["भावना"] = input_context
    print(f"🧠 Input context: भावना = {input_context}\n")

    # Task logic
    if "यदि उपयोगकर्ता.भावना == " in code:
        condition_match = re.search(r"यदि उपयोगकर्ता.भावना == \"(.*?)\"", code)
        if condition_match:
            expected = condition_match.group(1)
            if expected == input_context:
                print("✅ Condition matched: invoking calm protocol")
                memory["प्रक्रिया"] = "चक्र सन्तुलन"
            else:
                print("🔁 अन्यथा path: using AI memory layer")
                memory["प्रक्रिया"] = "AI स्मृति"
        else:
            print("⚠️ No valid condition found.")
    else:
        print("🟡 No conditional block found.")

    # Simulate a स्मृति assignment
    if "स्मृति[" in code:
        mem_assignments = re.findall(r'स्मृति\[\"(.*?)\"]\s*=\s*\"(.*?)\"', code)
        for key, value in mem_assignments:
            memory[key] = value
            print(f"📥 स्मृति updated: {key} = {value}")

    # Show memory
    print("\n📦 स्मृति:")
    for k, v in memory.items():
        print(f"  {k}: {v}")

    # Export memory trace to JSON
    with open("nara_memory_trace.json", "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)
    print("\n📄 Exported trace: nara_memory_trace.json")

    print("\n✅ NĀRA execution complete.")
