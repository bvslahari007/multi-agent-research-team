import os
import requests

def summarize(research_output):
    text = " ".join(research_output["insights"])
    api_key = os.getenv("SCALEDOWN_API_KEY")

    if not api_key:
        return {
    "summary": f"=== SUMMARY REPORT ===\n\n{text[:600]}\n\n[compressed]"
}


    url = "https://api.scaledown.xyz/compress/raw/"
    headers = {
        "x-api-key": api_key,
        "Content-Type": "application/json"
    }
    payload = {
        "prompt": text,
        "context": ""
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        compressed = response.text.strip()
        if compressed:
            return {"summary": compressed}
        raise ValueError
    except Exception:
        return {
    "summary": f"=== SUMMARY REPORT ===\n\n{text[:600]}\n\n[compressed]"
    }


