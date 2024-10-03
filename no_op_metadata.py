from dataclasses import dataclass

from openfeature.provider.metadata import Metadata


@dataclass
class NoOpMetadata(Metadata):
    """Represents a metadata class with no operation."""
    name: str = "No-op Provider"
    is_default_provider: bool = True
