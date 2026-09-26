# Calculation guide

## Question and evidence

How do learners check and revise AI assistance?

Synthetic prompt-event records grouped by learner and session.

**Status:** SYNTHETIC / RULE-BASED PROTOTYPE | no educational validity claim.

## Design

Rule-based intent labeling; within-session event rates; equally weighted session summaries.

## Calculation and interpretation

`Agency index = .30V + .25R + .25F + .20(1-A).`

V, R, F and A are verification, revision, reflection and answer-adoption rates. The weights are design choices, not estimated construct loadings. Session averages give each session equal weight; this is not a validated agency instrument.

## Evidence table

Selected recorded values (units and context shown). Full precision below is for traceability, not a claim of measurement precision.

| Quantity | Value | Unit / meaning | JSON path |
|---|---:|---|---|
| verification_rate | 0.524 | unitless | `verification_rate` |
| revision_rate | 0.518 | unitless | `revision_rate` |
| reflection_rate | 0.373 | unitless | `reflection_rate` |
| answer_adoption_rate | 0.49 | unitless | `answer_adoption_rate` |
| intent_diversity | 3.062 | unitless | `intent_diversity` |
| agency_index | 0.482 | unitless | `agency_index` |

Source: [results/demo_metrics.json](results/demo_metrics.json). Values resolve directly from this file when figures are regenerated.

This synthetic-data observatory turns AI interaction logs into inspectable session summaries of verification, revision, reflection, and answer adoption. Its intent labels use explicit lexical rules, and its agency index is a stated weighted heuristic rather than a psychological measure. The repository is useful for testing instrumentation and analysis workflows before collecting consented learner data.

## Verification performed in this review

The existing suite requires unavailable dependencies; no full-suite pass is claimed. The bundled demonstration executed successfully in this review.

The figure-generation check verifies agreement between the selected source values and SVGs. It does not validate the raw dataset, fitted model, identification assumptions, or external generalization.

```bash
python scripts/build_review_figures.py
python scripts/build_review_figures.py --check
```

## Implementation map

Follow these functions to inspect each transformation. Validation helpers and private functions remain visible in the linked modules.

| Function | Purpose / documented behavior |
|---|---|
| [`main`](src/genai_learning_observatory/cli.py#L5) | Inspect the explicit implementation and its callers. |
| [`classify_intent`](src/genai_learning_observatory/core.py#L17) | Inspect the explicit implementation and its callers. |
| [`add_intent_labels`](src/genai_learning_observatory/core.py#L23) | Inspect the explicit implementation and its callers. |
| [`session_features`](src/genai_learning_observatory/core.py#L26) | Inspect the explicit implementation and its callers. |
| [`cohort_summary`](src/genai_learning_observatory/core.py#L36) | Inspect the explicit implementation and its callers. |
| [`make_demo_events`](src/genai_learning_observatory/synthetic.py#L4) | Inspect the explicit implementation and its callers. |

## What remains before a stronger research claim

V, R, F and A are verification, revision, reflection and answer-adoption rates. The weights are design choices, not estimated construct loadings. Session averages give each session equal weight; this is not a validated agency instrument. A successful software test is not validation of a scientific construct. New experiments should state their split unit, comparator, outcome, uncertainty procedure and failure criteria before examining final test results.
