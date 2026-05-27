# Contributing to My Trading Agent

Thank you for your interest in contributing! Here's how you can help:

## Getting Started

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes
4. Run tests: `pytest`
5. Commit with clear messages: `git commit -m "Add feature X"`
6. Push to your fork and submit a Pull Request

## Development Setup

```bash
git clone https://github.com/rjbishnoi/my-trading-agent.git
cd my-trading-agent
pip install -e ".[dev]"
```

## Code Style

- Use `black` for formatting
- Use `ruff` for linting
- Type hints required for all functions
- Docstrings for all public methods

```bash
black .
ruff check --fix .
```

## Areas for Contribution

- [ ] Stock data providers integration (Yahoo Finance, Polygon, etc.)
- [ ] Additional technical indicators
- [ ] Web dashboard implementation
- [ ] Backtesting engine
- [ ] Real-time data streaming
- [ ] Database persistence
- [ ] Documentation improvements
- [ ] Bug fixes and optimizations

## Reporting Issues

Include:
- Python version
- Operating system
- Error message and traceback
- Steps to reproduce
- Expected vs actual behavior

## License

By contributing, you agree your contributions will be licensed under AGPL-3.0.
