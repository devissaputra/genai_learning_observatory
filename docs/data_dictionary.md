# Data dictionary

The baseline code documents its expected columns directly in `src/genai_learning_observatory/core.py` and `src/genai_learning_observatory/synthetic.py`. This keeps the schema close to the executable logic.

## Principles

- Use the minimum data needed for the research question.
- Separate identifiers from analytic features.
- Record provenance for derived variables.
- Treat missingness as information about the measurement process, not merely a nuisance.
- Never convert a research proxy into a high-stakes label without validation.
