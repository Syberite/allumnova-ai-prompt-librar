# Token & Cost Optimization Log (Week 4)

To ensure our LLM API calls remain cost-effective at scale, the following optimizations were applied to the system prompts this week:
1. **Instruction Minification:** Removed redundant conversational instructions (e.g., "Please make sure to...") and replaced them with strict, imperative commands ("Output JSON strictly").
2. **Whitespace Stripping:** Ensure the backend Python script strips unnecessary whitespace and newline characters from the raw user JSON before injecting it into the prompt.
3. **Model Selection:** Validated that `gemini-1.5-flash` provides the necessary reasoning for the CV parsing at a fraction of the cost/token of the Pro models, keeping latency low.
