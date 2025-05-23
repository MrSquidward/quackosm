"""Constants used across the project."""

import os

WGS84_CRS = "EPSG:4326"

FEATURES_INDEX = "feature_id"

GEOMETRY_COLUMN = "geometry"

FORCE_TERMINAL = os.getenv("FORCE_TERMINAL_MODE", "false").lower() == "true"
