"""Main conversational trading agent."""

from typing import Any, Optional
import json


class TradingAgent:
    """AI-powered trading agent for stock analysis and screening."""

    def __init__(
        self,
        provider: Optional[Any] = None,
        model: str = "gemini-2.0-flash",
        system_prompt: Optional[str] = None,
    ):
        """Initialize trading agent.

        Args:
            provider: LLM provider instance (Gemini, Claude, or OpenAI)
            model: Model name
            system_prompt: Custom system prompt
        """
        self.provider = provider
        self.model = model
        self.system_prompt = system_prompt or self._get_default_system_prompt()
        self.chat_history = []

    def _get_default_system_prompt(self) -> str:
        """Get default system prompt for trading analysis."""
        return """You are an expert trading analyst specializing in:
- Wyckoff method volume-price analysis
- Technical analysis and chart patterns
- Fundamental stock valuation
- Risk management and portfolio construction

When users ask about stocks:
1. Analyze volume and price action using Wyckoff principles
2. Identify support/resistance levels and breakout points
3. Assess risk/reward ratios
4. Provide actionable trading signals
5. Always mention relevant disclaimer about investment risk

Be concise, analytical, and data-driven.
"""

    def analyze_stock(self, stock_code: str, days: int = 60) -> str:
        """Analyze a single stock using technical and fundamental analysis.

        Args:
            stock_code: Stock ticker or code (e.g., '000001', 'AAPL')
            days: Number of days of historical data to analyze

        Returns:
            Analysis result as string
        """
        if not self.provider:
            return "Error: No LLM provider configured. Run 'trading-agent model add' first."

        prompt = f"""Analyze the stock {stock_code} using Wyckoff method analysis.
Provide:
1. Current price and key levels
2. Volume-price relationship
3. Recent patterns and structures
4. Potential entry/exit points
5. Risk assessment

Use technical analysis principles and be specific with price targets and timeframes.
"""

        try:
            response = self.provider.generate(prompt, self.system_prompt)
            return response
        except Exception as e:
            return f"Error analyzing stock: {str(e)}"

    def screen_market(self, criteria: Optional[dict] = None) -> str:
        """Screen market for stocks matching given criteria.

        Args:
            criteria: Dictionary of screening criteria
                - min_price: Minimum stock price
                - max_price: Maximum stock price
                - min_volume: Minimum daily volume
                - market: Market to screen ('a-share', 'us', 'hk')

        Returns:
            List of stocks matching criteria
        """
        if not self.provider:
            return "Error: No LLM provider configured."

        criteria = criteria or {"market": "a-share"}

        prompt = f"""Screen the {criteria.get('market', 'A-share')} market for stocks with Wyckoff buy signals.

Criteria:
{json.dumps(criteria, indent=2)}

Return:
1. Top 5-10 stock candidates
2. Current price and key levels for each
3. Signal strength (strong/moderate/weak)
4. Risk level for each
5. Brief reason for selection
"""

        try:
            response = self.provider.generate(prompt, self.system_prompt)
            return response
        except Exception as e:
            return f"Error screening market: {str(e)}"

    def chat(self, message: str) -> str:
        """Conversational interface for trading queries.

        Args:
            message: User query

        Returns:
            Agent response
        """
        if not self.provider:
            return "Error: No LLM provider configured."

        self.chat_history.append({"role": "user", "content": message})

        try:
            response = self.provider.generate(
                message,
                self.system_prompt,
                history=self.chat_history[:-1] if len(self.chat_history) > 1 else [],
            )
            self.chat_history.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            return f"Error: {str(e)}"

    def get_portfolio_status(self) -> str:
        """Get current portfolio status and P&L.

        Returns:
            Portfolio summary
        """
        return "Portfolio status feature coming soon."

    def backtest_strategy(self, strategy_name: str, start_date: str, end_date: str) -> str:
        """Backtest a trading strategy.

        Args:
            strategy_name: Name of strategy to backtest
            start_date: Start date (YYYYMMDD)
            end_date: End date (YYYYMMDD)

        Returns:
            Backtest results
        """
        return "Backtest feature coming soon."
