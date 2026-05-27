"""Command-line interface for trading agent.

Usage:
    trading-agent                  # Start TUI chat
    trading-agent screen           # Screen market for signals
    trading-agent backtest         # Run strategy backtest
    trading-agent report 000001    # Generate AI research report
    trading-agent model list       # List configured models
    trading-agent model add        # Add new LLM model
    trading-agent dashboard        # Launch web dashboard
"""

import argparse
import sys
from pathlib import Path


def _get_version() -> str:
    """Get package version."""
    try:
        from importlib.metadata import version
        return version("my-trading-agent")
    except Exception:
        return "0.1.0-dev"


def _cmd_version(_args):
    """Show version."""
    print(f"trading-agent {_get_version()}")


def _cmd_model(args):
    """Handle model commands."""
    sub = args.model_cmd or "list"

    if sub == "list":
        print("Configured models:")
        print("  (None configured yet)")
        print("\nTo add a model: trading-agent model add")
        return

    if sub == "add":
        print("Interactive model setup:")
        provider = input("Provider (gemini/claude/openai): ").strip().lower()
        if provider not in ("gemini", "claude", "openai"):
            print(f"Unknown provider: {provider}")
            sys.exit(1)

        api_key = input("API Key: ").strip()
        if not api_key:
            print("API key required")
            sys.exit(1)

        print(f"✓ Model configured: {provider}")
        return

    print(f"Unknown subcommand: {sub}")
    sys.exit(1)


def _cmd_screen(args):
    """Screen market for trading signals."""
    market = args.market or "a-share"
    print(f"Screening {market} market for Wyckoff signals...")
    print("(Feature coming soon)")


def _cmd_backtest(args):
    """Run strategy backtest."""
    months = args.months or 6
    print(f"Running backtest for {months} months...")
    print("(Feature coming soon)")


def _cmd_report(args):
    """Generate AI research report for stocks."""
    codes = args.codes
    if not codes:
        print("Error: Specify stock codes (e.g., trading-agent report 000001,600519)")
        sys.exit(1)

    print(f"Generating research reports for: {codes}")
    print("(Feature coming soon)")


def _cmd_tui(_args):
    """Start interactive TUI."""
    print("Starting trading agent TUI...")
    print("\nWelcome to Trading Agent! 📈")
    print("\nCommands:")
    print("  /help       - Show help")
    print("  /model      - Manage LLM models")
    print("  /screen     - Screen market")
    print("  /exit       - Exit")
    print("\nOr just type your question (e.g., '分析平安银行的技术面')\n")

    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue

            if user_input == "/exit" or user_input == "exit":
                print("Goodbye!")
                break

            if user_input == "/help":
                print(
                    "Commands: /help, /model, /screen, /exit, or ask a question about stocks"
                )
                continue

            if user_input.startswith("/"):
                print("Unknown command. Type /help for available commands.")
                continue

            # Echo user input (placeholder for actual agent)
            print(f"Agent: Analyzing '{user_input}'...")
            print("(Agent responses coming soon with LLM integration)\n")

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            break


def _cmd_dashboard(_args):
    """Launch web dashboard."""
    print("Starting dashboard...")
    print("(Dashboard feature coming soon)")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="trading-agent",
        description="AI-powered trading agent for stock analysis",
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {_get_version()}"
    )

    subparsers = parser.add_subparsers(dest="cmd")

    # Model management
    p_model = subparsers.add_parser("model", help="Manage LLM models")
    p_model.add_argument(
        "model_cmd", nargs="?", default="list", help="list/add/rm/default"
    )

    # Market screening
    p_screen = subparsers.add_parser("screen", help="Screen market for signals")
    p_screen.add_argument(
        "--market", default="a-share", help="Market to screen (a-share/us/hk)"
    )

    # Backtesting
    p_backtest = subparsers.add_parser("backtest", help="Run strategy backtest")
    p_backtest.add_argument("--months", type=int, default=6, help="Backtest period")

    # Research report
    p_report = subparsers.add_parser("report", help="Generate AI research report")
    p_report.add_argument("codes", nargs="?", help="Stock codes (comma-separated)")

    # Dashboard
    subparsers.add_parser("dashboard", help="Launch web dashboard", aliases=["dash"])

    args = parser.parse_args()

    # Dispatch command
    if args.cmd == "model":
        _cmd_model(args)
    elif args.cmd == "screen":
        _cmd_screen(args)
    elif args.cmd == "backtest":
        _cmd_backtest(args)
    elif args.cmd == "report":
        _cmd_report(args)
    elif args.cmd in ("dashboard", "dash"):
        _cmd_dashboard(args)
    else:
        _cmd_tui(args)


if __name__ == "__main__":
    main()
