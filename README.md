# OpenSecOps AI Platform

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

A modular AI-driven orchestration framework that accelerates security operations with GenAI-enhanced enrichment, threat scoring, and automated incident promotion.

## Why This Matters

This project mirrors AppSec automation pipelines used at scale to improve MTTR, reduce false positives, and support secure launch workflows — directly aligning with Amazon's focus on scalable tooling and security review enablement.

## Key Features
- AI-powered threat scoring via contextual LLM prompts (OpenAI + LangChain)
- Real-time log correlation from multi-source feeds
- Incident promotion logic and scoring thresholds
- Timeline generation for rapid analyst triage

##  Tech Stack
- Python, FastAPI
- LangChain, OpenAI API
- Redis, MongoDB
- GitHub Actions

## Setup

```bash
git clone https://github.com/jeevana-muninarayana/OpenSecOps-AI
cd OpenSecOps-AI
pip install -r requirements.txt
