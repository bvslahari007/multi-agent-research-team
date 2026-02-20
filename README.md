# Multi-Agent Research Team  
### Compressed Context Collaboration Prototype

## Overview

A modular CLI-based multi-agent system that demonstrates structured research generation, evaluation-driven refinement, and API-based summarisation.
This project was built to explore how multiple agents can collaborate through orchestration rather than relying on a single raw generative output..

---

## What This Project Demonstrates

- Multi-agent architecture with clear role separation  
- Manager-based orchestration logic  
- Evaluation-driven refinement loop  
- API integration (Scaledown compression API)  
- Fault-tolerant fallback handling  
- Structured CLI interface

## How it works:
User Input
   ↓
Manager Agent
   ↓
Research Agent
   ↓
Critic Agent
   ↓
(Refinement if score is low)
   ↓
Summariser Agent (Scaledown API)
   ↓
Final Output

The system consists of three specialised agents coordinated through a central manager.

### Research Agent
- Detects topic genre    
- Generates structured analytical insights    
- Adds domain anchoring for AI-related topics
- Outputs explicit assumptions  

### Summarizer Agent
- Integrates with Scaledown compression API
- Uses the ScaleDown Community API for context compression
- Generates compressed executive summary   
- Includes fallback if API key is unavailable

### Critic Agent
- Evaluates reasoning coverage and depth  
- Scores output (0–3)  
- Returns structured feedback  
- Triggers refinement if necessary

### Manager Agent
- Orchestrates agent interaction  
- Controls output modes    
- Maintains system state    

---

## What Makes This Project Different

- Genre-aware research framing instead of generic reasoning  
- Explicit compressed context sharing to reduce redundancy  
- Transparent signalling of compression rather than hiding it  
- Clear and honest system scope  

---

## How to Use

1. Run the program using the command line  
2. Enter a research-oriented topic  
3. Optionally provide context to guide exploration  
4. Choose between structured exploration, compressed summary, or coordinated output
5. To run the project, provide your own ScaleDown Community API key by setting it as an environment variable in a local `.env` file. The API key is required for compressed context summarization.

---

## Tools and Technologies

- Python  
- ScaleDown Community API  
---

## Project Links

- [Link to the project report](https://docs.google.com/document/d/1ZQGTB_5Fv5nMvMRKUYEltIB0LcEKtiLuJfhR-RVFOlI/edit?tab=t.0)
- [Link to Demo Video](https://drive.google.com/file/d/1EUJcP3hM3Feur-yplGwpS8xGfexJG0YM/view?usp=sharing)

