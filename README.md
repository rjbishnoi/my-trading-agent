# My Trading Agent 📈

**AI-Powered Wyckoff Trading Agent for Stock Analysis & Screening**

An open-source intelligent trading agent that combines Wyckoff method analysis, volume-price action, and LLM-powered research to identify trading opportunities and manage portfolios.

## Features

- **Conversational Agent** — Use natural language to trigger stock analysis, screening, and research
- **Wyckoff Analysis** — Volume-price pattern recognition and market structure analysis
- **Multi-Market Support** — A-shares, Hong Kong stocks, US stocks
- **Stock Screening** — 5-layer funnel screening with custom filters
- **AI Research Reports** — LLM-powered fundamental and technical analysis
- **Portfolio Management** — Track positions, manage risk, execute trading commands
- **MCP Server** — Model Context Protocol integration for Claude and other AI tools
- **Dashboard** — Local visualization panel for monitoring
- **CLI & Web UI** — Both terminal and web-based interfaces

## Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/rjbishnoi/my-trading-agent.git
cd my-trading-agent

# Install dependencies
pip install -e .

# Or using uv
uv pip install -e .
```

### Setup

```bash
# Add LLM model (Gemini/Claude/OpenAI)
trading-agent model add

# Configure data sources (optional)
trading-agent config tushare <token>
trading-agent config tickflow <api-key>

# Start the agent
trading-agent
```

## Commands

```bash
trading-agent                      # Start TUI chat
trading-agent screen               # Run full market screening
trading-agent backtest             # Strategy backtesting
trading-agent report 000001,600519 # AI research report
trading-agent dashboard            # Launch web dashboard
trading-agent portfolio list       # View positions
trading-agent model list           # List configured models
```

## Architecture

```
my-trading-agent/
├── agents/                 # Core agent implementations
│   ├── chat_agent.py      # Main conversational agent
│   └── tools.py           # Tool definitions
├── cli/                    # Command-line interface
│   ├── __main__.py        # CLI entry point
│   ├── auth.py            # Authentication
│   └── tui.py             # Terminal UI
├── core/                   # Core business logic
│   ├── prompts.py         # System prompts
│   ├── wyckoff.py         # Wyckoff analysis
│   └── screening.py       # Stock screening
├── integrations/          # External integrations
│   ├── supabase_*.py      # Database
│   ├── market_data.py     # Data providers
│   └── llm_providers.py   # LLM APIs
├── tools/                 # Tool implementations
│   ├── stock_analysis.py  # Technical analysis
│   ├── portfolio.py       # Portfolio tools
│   └── research.py        # Research tools
├── pyproject.toml         # Project metadata
└── README.md              # This file
```

## Configuration

Create `.env` file in project root:

```bash
# LLM API Keys
GEMINI_API_KEY=your-key
ANTHROPIC_API_KEY=your-key
OPENAI_API_KEY=your-key

# Data Sources
TUSHARE_TOKEN=your-token
TICKFLOW_API_KEY=your-key

# Database (optional)
SUPABASE_URL=your-url
SUPABASE_KEY=your-key
```

## Example Usage

### Interactive Chat

```
> 分析平安银行的技术面形态
Agent analyzing 000001 (平安银行)...

> 筛选出最近有买点信号的股票
Screening market for buy signals...

> 生成600519的深度研报
Generating AI research report for 600519...
```

### Programmatic Usage

```python
from agents.chat_agent import TradingAgent
from cli.auth import load_model_configs, load_default_model_id

agent = TradingAgent()
result = agent.analyze_stock("000001")  # Ping An Bank
print(result)
```

## LLM Providers

Supported providers:
- **Gemini** (Google) - Fast, affordable
- **Claude** (Anthropic) - Best reasoning
- **OpenAI** (GPT-4o) - Strong general purpose

Easily switch between providers:

```bash
trading-agent model default gemini
trading-agent model default claude
```

## Documentation

- [Architecture](docs/ARCHITECTURE.md)
- [Wyckoff Method](docs/WYCKOFF_METHOD.md)
- [API Reference](docs/API.md)
- [Contributing](CONTRIBUTING.md)

## Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Lint
ruff check .

# Format
ruff format .
```

## Disclaimer

⚠️ **Risk Disclosure**: This tool is for educational and research purposes only. It does not provide investment advice and should not be used for actual trading without thorough testing and validation. Past performance does not guarantee future results.

## License

AGPL-3.0 © 2026 rjbishnoi

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review documentation and examples

## Acknowledgments

Inspired by:
- [WyckoffTradingAgent](https://github.com/YoungCan-Wang/WyckoffTradingAgent)
- Wyckoff method trading community
- Open-source AI and finance projects
