# Cycle Agent Lab

This lab is intended to demonstrate the basic execution cycle of an AI agent.

## Purpose

The goal of this folder is to organize the `cycle_lab.py` experiment, which should focus on the fundamental agent loop:

```text
User Input
    ↓
Interpret Goal
    ↓
Plan or Decide Next Step
    ↓
Act
    ↓
Observe Result
    ↓
Respond
```

## Recommended File Placement

Place the Python lab file here:

```text
01_simple_agents/cycle_agent_lab/cycle_lab.py
```

## Learning Objectives

- Understand the basic agent execution cycle
- Separate user input from agent decision logic
- Practice simple planning or next-step selection
- Demonstrate how an agent can maintain a simple workflow loop
- Prepare for more advanced tool-using and multi-agent examples

## Suggested Implementation Pattern

A simple version of this lab may include:

1. Receive a user request
2. Identify the user's intent or goal
3. Decide the next action
4. Execute a simple action or simulated action
5. Return an observation
6. Produce a final response

## Future Enhancements

- Add `cycle_lab.py`
- Add comments explaining each stage of the cycle
- Add simple state tracking
- Add tool-use simulation
- Add logging for each agent step
- Add a diagram showing the cycle
- Compare the cycle to more advanced ReAct-style agent patterns

## Relationship to Other Sections

This lab belongs under `01_simple_agents` because it focuses on the foundational agent loop.

If the lab later adds API calls, file access, or external tools, a more advanced version can be placed under:

```text
02_tool_using_agents/
```

If the lab later adds document retrieval, a RAG version can be placed under:

```text
03_rag_agents/
```
