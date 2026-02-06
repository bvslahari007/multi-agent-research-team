# Multi-Agent Research Support System  
### Compressed Context Collaboration Prototype

## Overview

This project explores how multiple AI agents can collaborate on research-oriented tasks by sharing **compressed context instead of full reasoning histories**. The focus is on structuring research thinking and reducing redundancy rather than performing factual or web-based research.

The system demonstrates a cost-conscious and transparent approach to multi-agent coordination.

---

## Problem Statement

Build a collaborative research team of AI agents using compressed context sharing to reduce token costs while coordinating on complex research tasks.

---

## System Design

The system consists of three specialised agents coordinated through a central manager.

### Research Agent
- Frames the topic conceptually  
- Adapts reasoning style based on the genre of the topic  
- Produces structured research-oriented insights  

### Summarizer Agent
- Compresses verbose research output into compact representations  
- Uses the ScaleDown Community API for context compression  
- Explicitly marks compressed outputs using `[compressed]`  

### Manager Agent
- Orchestrates agent interaction  
- Controls execution flow and output selection  
- Maintains separation between reasoning and system control  

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

---

## Tools and Technologies

- Python  
- ScaleDown Community API  
---

## Project Links

- Project Report: [](https://docs.google.com/document/d/1ZQGTB_5Fv5nMvMRKUYEltIB0LcEKtiLuJfhR-RVFOlI/edit?tab=t.0) 

