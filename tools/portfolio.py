"""Portfolio management tools."""

from typing import Dict, List, Any


class Portfolio:
    """User portfolio manager."""

    def __init__(self):
        """Initialize portfolio."""
        self.positions: List[Dict[str, Any]] = []
        self.cash = 0.0

    def add_position(
        self, code: str, shares: int, entry_price: float, stop_loss: float
    ) -> bool:
        """Add position to portfolio.

        Args:
            code: Stock code
            shares: Number of shares
            entry_price: Entry price
            stop_loss: Stop loss price

        Returns:
            Success status
        """
        position = {
            "code": code,
            "shares": shares,
            "entry_price": entry_price,
            "stop_loss": stop_loss,
            "current_price": entry_price,
        }
        self.positions.append(position)
        return True

    def close_position(self, code: str) -> bool:
        """Close a position.

        Args:
            code: Stock code

        Returns:
            Success status
        """
        self.positions = [p for p in self.positions if p["code"] != code]
        return True

    def get_portfolio_value(self) -> float:
        """Get total portfolio value.

        Returns:
            Total value
        """
        total = self.cash
        for pos in self.positions:
            total += pos["shares"] * pos["current_price"]
        return total
