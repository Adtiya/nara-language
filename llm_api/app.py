from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["5 per minute"]
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/api/guru", methods=["POST"])
def guru_response():

    user_token = request.headers.get("X-NARA-TOKEN")
    required_token = os.getenv("NARA_ACCESS_TOKEN")
    if required_token and user_token != required_token:
        return jsonify({"error": "Unauthorized access"}), 403

    data = request.get_json()
    code = data.get("code", "")
    user_state = data.get("context", "No emotional state provided.")

    prompt = f"""
You are a Guru AI. Interpret the following Sanskrit AI-agent code and respond with emotional, spiritual, or wise advice.

.nara code:
{code}

User context: {user_state}

Respond like a compassionate guide.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a wise AI guru."},
                {"role": "user", "content": prompt}
            ]
        )
        return jsonify({"reply": response.choices[0].message["content"].strip()})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "🕉️ NĀRA LLM Agent is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
