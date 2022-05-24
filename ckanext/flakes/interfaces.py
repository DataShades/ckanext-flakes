from __future__ import annotations

from typing import Any

from ckan.plugins import Interface


class IFlakes(Interface):
    """Extend functionality of ckanext-flakes"""

    def get_flake_schemas(self) -> dict[str, dict[str, Any]]:
        """Register named validation schemas.

        Returns:
            Mapping of names to the corresponding validation schemas.

        Example:
            def get_flake_schemas(self) -> dict[str, dict[str, Any]]:
                return {
                    "name-only": {"name": [not_missing]}
                }
        """
        return {}

    def get_flake_factories(self) -> dict[str, dict[str, Any]]:
        """Register named example factories.

        Returns:
            Mapping of names to the corresponding validation factories.

        Example:
            def get_flake_factories(self) -> dict[str, dict[str, Any]]:
                def factory(payload: dict[str, Any]):
                    return {"field": "value"}

                return {
                    "test-factory": factory
                }
        """
        return {}
