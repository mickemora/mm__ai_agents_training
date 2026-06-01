# MM AI Agents Training

This repository is intended to document and organize hands-on learning, experiments, and practice projects related to **AI agents**, **agentic AI**, and modern AI application development.

The current repository is an early-stage training workspace. It can be used to capture examples, notes, exercises, prototypes, and code related to building AI agents that can reason, use tools, retrieve information, and coordinate multi-step tasks.

## Project Purpose

The purpose of this repository is to create a structured learning space for AI agent development.

The repository can support exploration of topics such as:

- AI agent fundamentals
- Agentic workflows
- Tool use by language models
- Retrieval-Augmented Generation (RAG)
- Multi-agent collaboration
- Prompt engineering for agents
- Function calling and tool orchestration
- Memory and context management
- Evaluation of agent behavior
- Enterprise AI use cases

## Learning Objectives

This repository can be used to build practical understanding of how AI agents work and how they can be applied to real-world business and technology scenarios.

Key learning objectives include:

1. Understand what makes an AI system agentic
2. Learn how agents use tools to perform actions
3. Explore how agents break down tasks into steps
4. Practice designing prompts and instructions for agents
5. Understand how memory and context affect agent performance
6. Experiment with RAG-based agent workflows
7. Compare single-agent and multi-agent patterns
8. Study enterprise use cases for AI automation
9. Build small prototypes that demonstrate agent behavior
10. Connect AI agent design to practical business value

## What Is an AI Agent?

An AI agent is a software system that can use a language model, instructions, context, tools, and goals to perform tasks on behalf of a user or process.

A simple AI agent may:

- Receive a user request
- Interpret the goal
- Decide what steps are needed
- Use tools or APIs
- Retrieve relevant information
- Produce an answer or take an action

More advanced agents may include:

- Planning
- Memory
- Tool selection
- Multi-step reasoning
- Human-in-the-loop review
- Multi-agent coordination
- Observability and evaluation

## Suggested Repository Structure

As this training repository grows, the following structure may be useful:

```text
.
├── README.md
├── notes/
│   └── ai_agents_fundamentals.md
├── examples/
│   ├── simple_agent/
│   ├── tool_using_agent/
│   ├── rag_agent/
│   └── multi_agent_workflow/
├── prompts/
│   ├── system_prompts.md
│   └── evaluation_prompts.md
├── diagrams/
│   └── agent_architecture.md
├── experiments/
│   └── README.md
└── requirements.txt
```

## Topics to Explore

### 1. AI Agent Fundamentals

Core concepts to study:

- Agent
- Tool
- Goal
- Task
- Context
- Memory
- Planning
- Action
- Observation
- Evaluation

### 2. Tool Use

Agents become more useful when they can interact with external systems.

Potential tools include:

- Search tools
- APIs
- Databases
- File systems
- Calculators
- Code execution tools
- Enterprise systems
- Cloud services

### 3. Retrieval-Augmented Generation

RAG allows an AI system to retrieve relevant information before generating an answer.

A RAG-enabled agent may:

1. Receive a question
2. Search a knowledge base
3. Retrieve relevant documents
4. Use the retrieved content as context
5. Generate a grounded response

### 4. Multi-Agent Systems

Multi-agent systems use multiple specialized agents that collaborate on a shared goal.

Example roles may include:

- Planner Agent
- Research Agent
- Coding Agent
- Review Agent
- Testing Agent
- Domain Expert Agent

### 5. Enterprise AI Use Cases

Potential enterprise use cases include:

- Warranty claim review
- Quality issue triage
- Technical support assistance
- Software development support
- Incident management
- Knowledge management
- Requirements analysis
- Project status summarization
- Risk assessment
- Workflow automation

## Example Agent Architecture

A simple agent architecture may look like this:

```text
User Request
    ↓
Agent Instructions / System Prompt
    ↓
Language Model
    ↓
Planning / Reasoning Step
    ↓
Tool Selection
    ↓
External Tool or Knowledge Source
    ↓
Observation / Retrieved Context
    ↓
Final Response or Action
```

## Potential Technology Stack

This repository may eventually include experiments using tools and frameworks such as:

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

At this stage, the repository is a workspace for organizing AI agent training content.

As code examples are added, setup instructions can be expanded to include:

```bash
git clone https://github.com/mickemora/mm__ai_agents_training.git
cd mm__ai_agents_training
```

Future Python-based examples may use:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Suggested First Exercises

Potential first exercises for this repository include:

1. Build a simple question-answering agent
2. Build an agent that uses a calculator tool
3. Build an agent that retrieves information from a small local knowledge base
4. Build a RAG workflow using a few sample documents
5. Build a multi-agent workflow with planner and reviewer roles
6. Create a prompt library for different agent behaviors
7. Document lessons learned from each experiment

## Skills Demonstrated

As this repository develops, it can demonstrate skills such as:

- AI agent design
- Prompt engineering
- Python development
- Tool orchestration
- RAG architecture
- Workflow automation
- Multi-agent design
- Cloud AI integration
- AI solution evaluation
- Enterprise AI thinking

## Professional Relevance

AI agents are becoming increasingly important in enterprise technology because they can help automate knowledge work, coordinate multi-step processes, and interact with internal systems.

For enterprise IT and technology leadership, AI agents are relevant to:

- Operational efficiency
- Software delivery acceleration
- Knowledge management
- Customer and dealer support
- Quality management
- Warranty analysis
- Incident response
- Business process automation
- Decision support systems

## Current Status

This repository is currently in an early setup stage.

Planned next steps may include:

- Add foundational notes on AI agents
- Add basic Python examples
- Add sample prompts
- Add a simple tool-using agent
- Add a RAG-based example
- Add architecture diagrams
- Add links to relevant training resources
- Add lessons learned from hands-on experiments

## Summary

This repository is intended to become a hands-on AI agents training workspace. It will organize learning materials, experiments, examples, and prototypes related to agentic AI, tool use, RAG, multi-agent systems, and enterprise AI applications.
