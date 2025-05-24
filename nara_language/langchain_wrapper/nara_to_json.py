"""
NĀRA to JSON Converter (Prototype)
"""

import re
import json

def nara_to_json(nara_code: str):
    data = {}
    data["agent"] = re.findall(r"पुरुषः (.*?) अस्ति", nara_code)
    data["traits"] = re.findall(r"गुणाः: \[(.*?)\]", nara_code)
    data["input"] = re.findall(r"प्रवेशः: (.*?)\n", nara_code)
    data["output"] = re.findall(r"निर्गमः: (.*?)\n", nara_code)
    data["task"] = re.findall(r'कर्मे "(.*?)"', nara_code)
    data["conditions"] = re.findall(r"यदि (.*?)\n", nara_code)
    data["feedback"] = "प्रत्युपकर्षः" in nara_code
    return json.dumps(data, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    code = open("../examples/healer_agent.nara", encoding="utf-8").read()
    result = nara_to_json(code)
    print(result)
