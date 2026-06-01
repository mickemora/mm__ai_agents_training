# MM AI Agents Training

This repository is a structured learning and experimentation workspace for **AI agents**, **agentic AI**, **tool-using agents**, **RAG agents**, **multi-agent systems**, and **enterprise AI use cases**.

The goal is to organize hands-on learning in a way that supports both technical growth and professional portfolio development.

## Purpose

This repository is intended to help build practical capability in AI agent development by progressing from foundational concepts to increasingly enterprise-relevant implementations.

The focus areas include:

- AI agent fundamentals
- Prompt engineering for agents
- Tool use and function calling
- Retrieval-Augmented Generation (RAG)
- Multi-agent collaboration
- Framework comparisons
- Amazon Bedrock agents and knowledge bases
- Agent evaluation and governance
- Enterprise AI use cases

## Repository Map

```text
.
├── README.md
├── ROADMAP.md
├── LEARNING_LOG.md
├── GLOSSARY.md
├── requirements.txt
├── .gitignore
│
├── 00_foundations/
├── 01_simple_agents/
├── 02_tool_using_agents/
├── 03_rag_agents/
├── 04_frameworks/
├── 05_aws_bedrock_agents/
├── 06_multi_agent_systems/
├── 07_enterprise_use_cases/
├── 08_evaluation_and_governance/
├── 09_diagrams/
├── 10_prompts/
└── 99_archive/
```

## Learning Path

The repository is organized as a progressive learning path:

```text
Foundations
    ↓
Simple Agents
    ↓
Tool-Using Agents
    ↓
RAG Agents
    ↓
Agent Frameworks
    ↓
AWS Bedrock Agents
    ↓
Multi-Agent Systems
    ↓
Enterprise Use Cases
    ↓
Evaluation and Governance
```

## Directory Purpose

| Directory | Purpose |
|----------|---------|
| `00_foundations/` | Conceptual notes on AI agents, workflows, memory, planning, and prompt design. |
| `01_simple_agents/` | Small beginner-friendly agent examples. |
| `02_tool_using_agents/` | Agents that interact with tools, APIs, files, databases, or external systems. |
| `03_rag_agents/` | Retrieval-Augmented Generation examples and document Q&A workflows. |
| `04_frameworks/` | Experiments and comparisons involving frameworks such as LangChain, CrewAI, and LlamaIndex. |
| `05_aws_bedrock_agents/` | Amazon Bedrock examples, knowledge bases, action groups, and AWS integrations. |
| `06_multi_agent_systems/` | Multi-agent orchestration patterns and collaboration examples. |
| `07_enterprise_use_cases/` | Business-oriented AI agent use cases such as warranty review, quality triage, and support automation. |
| `08_evaluation_and_governance/` | Notes and experiments related to quality, safety, security, cost, observability, and human-in-the-loop controls. |
| `09_diagrams/` | Architecture diagrams and visual explanations. |
| `10_prompts/` | Reusable prompt templates for agents, tools, RAG, multi-agent systems, and evaluation. |
| `99_archive/` | Deprecated experiments, old drafts, or historical learning artifacts. |

## Current Status

This repository is in the early setup stage.

The current work focuses on establishing a clean structure that can support future examples, experiments, notes, prompts, diagrams, and enterprise use cases.

## Suggested First Experiments

Initial experiments to add:

1. Simple Q&A agent
2. Calculator tool agent
3. File-reading agent
4. Local document Q&A / RAG agent
5. Planner-reviewer multi-agent workflow
6. Amazon Bedrock basic model invocation
7. Amazon Bedrock Knowledge Base example
8. Warranty claim review agent prototype

## Technology Stack Candidates

Potential technologies and frameworks to explore:

- Python
- LangChain
- CrewAI
- LlamaIndex
- OpenAI API
- Amazon Bedrock
- Amazon Bedrock Agents
- Amazon Bedrock Knowledge Bases
- AWS Lambda
- Amazon API Gateway
- Vector databases
- FAISS
- Chroma
- Streamlit

## Getting Started

Clone the repository:

```bash
git clone https://github.com/mickemora/mm__ai_agents_training.git
cd mm__ai_agents_training
```

For future Python-based examples, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Professional Relevance

AI agents are increasingly relevant to enterprise technology because they can help automate knowledge work, coordinate multi-step processes, retrieve internal knowledge, and interact with business systems.

Relevant enterprise use cases include:

- Warranty claim review
- Quality issue triage
- Dealer or technical support assistance
- Incident management
- Knowledge management
- Requirements analysis
- Project status summarization
- Risk assessment
- Workflow automation
- Decision support systems

## Key Supporting Documents

- `ROADMAP.md` - planned learning and implementation phases
- `LEARNING_LOG.md` - ongoing record of lessons learned
- `GLOSSARY.md` - AI agent terminology and definitions
- `requirements.txt` - Python dependencies for future examples

## Summary

This repository is intended to become a hands-on AI agents training lab. It will organize learning materials, experiments, prototypes, prompts, diagrams, and enterprise AI use cases related to agentic AI, RAG, tool use, multi-agent systems, and cloud-based AI development.
