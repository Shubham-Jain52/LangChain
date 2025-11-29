# 🚀 Week 1 — AI Agent Journey  
### *Building Foundations in LangChain, LLMs & Prompt Engineering*

This repository contains my **Week 1 progress** toward becoming an AI Agent Engineer.  
The goal for this week was to understand the fundamentals of LLM-based agents,  
experiment with prompt templates, and build my first controlled-behavior agent.

---

## 🧭 What I Learned This Week

### ✔️ Core Concepts
- Difference between **Chatbots vs LLMs vs AI Agents**
- Understanding **system prompts, user prompts, and dynamic prompts**
- What is a **Chain** in LangChain
- Why **Prompt Templates** are essential for controlling LLM behavior
- How LLM personality, tone, and identity can be modified using structured prompts

---

## ⚡ Tools & Technologies Explored

| Tool / Library | Purpose |
|----------------|---------|
| **Python** | Core runtime and scripting |
| **LangChain** | LLM orchestration and prompt engineering |
| **ChatGroq** | Fast LLaMA inference using Groq API |
| **Virtual Environment** | Project isolation |
| **dotenv** | Managing API keys securely |

---

## 🎯 Week 1 Project

### 🧩 Mood-Based Reply Bot

An AI agent that responds based on the **user's emotional state**.  
The user provides a mood (e.g., *happy, sad, robotic, angry*)  
and the bot generates a reply in that tone.

#### 🛠️ Features
- Accepts mood as user input
- Injects this mood dynamically into a prompt template
- Replies in the same tone as the mood
- Uses **Groq LLaMA 3.3 70B** model for inference

---

## 🧱 Architectural Flow

User selects mood
↓
Prompt Template injects mood variable
↓
LLM generates mood-based response
↓
User receives emotionally aligned output

