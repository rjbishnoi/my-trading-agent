# Architecture

## Overview

My Trading Agent is built with a modular architecture supporting:
- Multiple LLM providers (Gemini, Claude, OpenAI)
- Extensible tool system
- Pluggable data providers
- CLI, TUI, and Web interfaces

## Components

### Core Agent (`agents/`)

- **chat_agent.py** - Main conversational agent
- **tools.py** - Tool registry and definitions

### CLI (`cli/`)

- **__main__.py** - Command-line interface
- **auth.py** - Authentication and model management
- **tui.py** - Terminal user interface

### Core Logic (`core/`)

- **prompts.py** - System prompts and templates
- **wyckoff.py** - Wyckoff analysis engine
- **screening.py** - Stock screening logic

### Tools (`tools/`)

- **stock_analysis.py** - Technical analysis tools
- **portfolio.py** - Portfolio management
- **research.py** - Research and fundamentals

### Integrations (`integrations/`)

- **llm_providers.py** - LLM API integration
- **market_data.py** - Data provider integration
- **database.py** - Data persistence

## Data Flow

```
User Input
    ↓
[CLI/TUI/Web]
    ↓
[Agent]
    ↓
[Tool Selection]
    ↓
[Tool Execution]
    ↓
[Data Processing]
    ↓
[LLM Analysis]
    ↓
[Response]
    ↓
[Output]
```

## Extension Points

### Adding New Tools

```python
from agents.tools import ToolRegistry

registry = ToolRegistry()
registry.register(
    "my_tool",
    my_tool_function,
    "Tool description"
)
```

### Adding Data Providers

Implement the `DataProvider` interface:

```python
class MyDataProvider:
    def get_price(self, code: str):
        pass
    
    def get_history(self, code: str, days: int):
        pass
```

### Implementing New Analyses

Add methods to `WyckoffAnalyzer` or create new analyzer classes.
