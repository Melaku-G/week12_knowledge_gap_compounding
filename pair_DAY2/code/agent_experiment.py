import time
import json
from typing import Dict, Any, List

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

# =========================
# CONFIG
# =========================

MODEL_NAME = "gpt-4o-mini"  # replace with your model
MAX_STEPS = 5

USE_STRONG_SCHEMA = True
USE_STOP_CONDITION = True

# =========================
# TOOL DEFINITION
# =========================

def get_enrichment(company_name: str) -> Dict[str, Any]:
    """Mock tool"""
    return {
        "company": company_name,
        "enriched": True,
        "employees": 120,
        "industry": "SaaS"
    }

TOOLS = {
    "get_enrichment": get_enrichment
}

# =========================
# SCHEMA
# =========================

def tool_schema_prompt():
    if USE_STRONG_SCHEMA:
        return """
You can call tools using STRICT JSON ONLY.

Format:
{
  "tool": "get_enrichment",
  "arguments": {
    "company_name": "string"
  }
}

Do not output anything else when calling a tool.
"""
    else:
        return """
You may call tools informally if needed.
"""

# =========================
# PROMPT
# =========================

def build_prompt(task: str, history: List[str]) -> List:
    system = SystemMessage(content=f"""
You are an agent solving tasks step by step.

{tool_schema_prompt()}

Decide at each step:
- Continue reasoning
- OR call a tool

Stop when task is complete.
""")

    history_text = "\n".join(history)

    user = HumanMessage(content=f"""
Task: {task}

Previous steps:
{history_text}

What do you do next?
""")

    return [system, user]

# =========================
# TOOL PARSER
# =========================

def try_parse_tool_call(output: str):
    try:
        data = json.loads(output)
        if "tool" in data:
            return data
    except:
        return None
    return None

# =========================
# EXPERIMENT LOOP
# =========================

def run_agent(task: str):
    model = ChatOpenAI(model=MODEL_NAME, temperature=0)

    history = []
    logs = []

    start_time = time.time()

    for step in range(MAX_STEPS):
        step_start = time.time()

        messages = build_prompt(task, history)
        response = model(messages)
        output = response.content.strip()

        tool_call = try_parse_tool_call(output)

        log = {
            "step": step,
            "output": output,
            "type": "reasoning",
            "tool": None,
            "valid": None,
            "latency": None
        }

        if tool_call:
            log["type"] = "tool_call"
            tool_name = tool_call.get("tool")
            args = tool_call.get("arguments", {})

            if tool_name in TOOLS:
                try:
                    result = TOOLS[tool_name](**args)
                    log["tool"] = tool_name
                    log["valid"] = True
                    history.append(f"Tool result: {result}")
                except Exception as e:
                    log["valid"] = False
                    history.append(f"Tool error: {str(e)}")
            else:
                log["valid"] = False
                history.append("Invalid tool called")

        else:
            history.append(output)

        log["latency"] = time.time() - step_start
        logs.append(log)

        # STOP CONDITION
        if USE_STOP_CONDITION:
            if "FINAL ANSWER" in output.upper():
                break

    total_time = time.time() - start_time

    return logs, total_time

# =========================
# METRICS
# =========================

def compute_metrics(logs, total_time):
    tool_calls = [l for l in logs if l["type"] == "tool_call"]
    valid_calls = [l for l in tool_calls if l["valid"]]

    hallucination_rate = 0
    if tool_calls:
        hallucination_rate = 1 - (len(valid_calls) / len(tool_calls))

    return {
        "steps": len(logs),
        "tool_calls": len(tool_calls),
        "valid_calls": len(valid_calls),
        "hallucination_rate": hallucination_rate,
        "total_latency": total_time,
        "avg_step_latency": total_time / len(logs)
    }

# =========================
# RUN EXPERIMENT
# =========================

if __name__ == "__main__":
    TASKS = [
        "Find enrichment data for company Stripe",
        "Get enrichment for OpenAI and summarize",
    ]

    for task in TASKS:
        logs, total_time = run_agent(task)
        metrics = compute_metrics(logs, total_time)

        print("\n==============================")
        print("TASK:", task)
        print("METRICS:", metrics)
        print("STEPS LOG:")
        for l in logs:
            print(l)