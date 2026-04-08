# Support Ticket Environment (OpenEnv)

## Overview
This environment simulates real-world customer support tasks.

## Tasks
- Easy: Order tracking
- Medium: Damaged product
- Hard: Billing issue

## Observation Space
- ticket (string)
- history (list)

## Action Space
- response (string)

## Reward
Based on keyword matching with expected solution.

## Setup
pip install -r requirements.txt  
python inference.py

## Baseline Score
~0.5–1.0 depending on model

## Baseline Inference
Run the baseline agent:
python inference.py
This script follows the required OpenEnv format:
- Uses environment variables (API_BASE_URL, MODEL_NAME, HF_TOKEN)
- Uses OpenAI client
- Outputs structured logs (START / STEP / END)
