import json

def parse_json_safe(json_str: str) -> dict:
    """
    Safely parse JSON returned by the AI. 
    Returns a dictionary or empty dict on failure.
    """
    try:
        return json.loads(json_str)
    except Exception as e:
        return {"explanation": f"JSON parsing error: {e}",
                "fix": "No fix needed",
                "fixed_code": "",
                "improvement": "No improvement needed",
                "improved_code": ""}
