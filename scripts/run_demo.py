#!/usr/bin/env python3
"""Demo runner for NeuroPhoton scaffold"""
from src.neurophoton.core import example_model
params = {"mode": "demo", "value": 42}
out = example_model(params)
print("Demo output:", out)
