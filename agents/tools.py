"""Tool definitions for trading agent."""

from typing import Any, Callable, Dict, List


class ToolRegistry:
    """Registry of tools available to the trading agent."""

    def __init__(self):
        """Initialize tool registry."""
        self.tools: Dict[str, Callable] = {}
        self.descriptions: Dict[str, str] = {}
        self._register_default_tools()

    def _register_default_tools(self) -> None:
        """Register default trading tools."""
        self.register(
            "analyze_stock",
            self._analyze_stock,
            "Analyze a single stock using technical analysis",
        )
        self.register(
            "screen_market",
            self._screen_market,
            "Screen market for stocks with buy signals",
        )
        self.register(
            "get_price",
            self._get_price,
            "Get current price and key levels for a stock",
        )
        self.register(
            "get_indicators",
            self._get_indicators,
            "Get technical indicators (RSI, MACD, Bollinger Bands, etc)",
        )

    def register(
        self, name: str, func: Callable, description: str
    ) -> None:
        """Register a new tool.

        Args:
            name: Tool name
            func: Callable tool function
            description: Tool description
        """
        self.tools[name] = func
        self.descriptions[name] = description

    def get_tool(self, name: str) -> Callable:
        """Get a registered tool.

        Args:
            name: Tool name

        Returns:
            Tool function
        """
        return self.tools.get(name)

    def list_tools(self) -> Dict[str, str]:
        """List all available tools.

        Returns:
            Dictionary of tool names and descriptions
        """
        return self.descriptions.copy()

    # Default tool implementations

    @staticmethod
    def _analyze_stock(stock_code: str, days: int = 60) -> Dict[str, Any]:
        """Analyze a stock."""
        return {
            "status": "pending",
            "message": f"Analyzing {stock_code}...",
            "code": stock_code,
        }

    @staticmethod
    def _screen_market(market: str = "a-share") -> Dict[str, Any]:
        """Screen market."""
        return {
            "status": "pending",
            "message": f"Screening {market} market...",
            "market": market,
        }

    @staticmethod
    def _get_price(stock_code: str) -> Dict[str, Any]:
        """Get stock price."""
        return {
            "status": "pending",
            "code": stock_code,
            "message": "Fetching price data...",
        }

    @staticmethod
    def _get_indicators(stock_code: str) -> Dict[str, Any]:
        """Get technical indicators."""
        return {
            "status": "pending",
            "code": stock_code,
            "message": "Calculating indicators...",
        }
