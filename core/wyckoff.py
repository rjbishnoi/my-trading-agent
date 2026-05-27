"""Wyckoff method analysis core."""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class WyckoffPhase:
    """Represents a phase in Wyckoff method."""

    name: str  # Accumulation, Markup, Distribution, Markdown
    start_date: str
    end_date: Optional[str] = None
    description: str = ""


@dataclass
class VolumeAnalysis:
    """Wyckoff volume analysis."""

    price_change: float
    volume: int
    relative_volume: float  # vs average
    strength: str  # weak/normal/strong


class WyckoffAnalyzer:
    """Perform Wyckoff analysis on price data."""

    @staticmethod
    def identify_support_resistance(prices: List[float]) -> tuple:
        """Identify support and resistance levels.

        Args:
            prices: List of price data

        Returns:
            Tuple of (support_level, resistance_level)
        """
        if not prices:
            return None, None

        support = min(prices[-20:]) if len(prices) >= 20 else min(prices)
        resistance = max(prices[-20:]) if len(prices) >= 20 else max(prices)

        return support, resistance

    @staticmethod
    def analyze_volume_spread(prices: List[float], volumes: List[int]) -> str:
        """Analyze volume spread relationship.

        Args:
            prices: Price data
            volumes: Volume data

        Returns:
            Analysis string
        """
        if not prices or not volumes:
            return "Insufficient data"

        # Simple analysis
        recent_vol = sum(volumes[-5:]) / 5  # Average recent volume
        total_vol = sum(volumes[-20:]) / 20  # Average 20-day volume

        if recent_vol > total_vol * 1.5:
            return "High volume - Potential breakout"
        elif recent_vol < total_vol * 0.7:
            return "Low volume - Consolidation"
        else:
            return "Normal volume - Trending"

    @staticmethod
    def identify_accumulation_distribution(prices: List[float], volumes: List[int]) -> str:
        """Identify accumulation or distribution phase.

        Args:
            prices: Price data
            volumes: Volume data

        Returns:
            Phase identification
        """
        if len(prices) < 10:
            return "Insufficient data"

        # Simple heuristic
        recent_prices = prices[-10:]
        recent_volumes = volumes[-10:]

        price_range = max(recent_prices) - min(recent_prices)
        avg_volume = sum(recent_volumes) / len(recent_volumes)

        if price_range > 0 and avg_volume > 0:
            if max(recent_prices) == prices[-1]:  # Higher high
                return "Potential Markup Phase"
            else:
                return "Potential Accumulation Phase"

        return "Unknown Phase"
