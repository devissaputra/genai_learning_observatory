# Research design

## Project aim

Most dashboards reduce GenAI use to counts or time-on-task. This project treats learner–AI interaction as a process: what the learner asked for, whether they checked the answer, whether they revised it, and whether the interaction ended in reflection or simple adoption.

## Research questions

1. How can we distinguish productive help-seeking from passive answer adoption?
2. Which interaction patterns signal learner agency, verification, and reflection?
3. How should an observability layer represent uncertainty without turning exploratory analytics into high-stakes labels?

## Baseline analytic pipeline

1. Event ingestion
2. Intent tagging
3. Behavioral feature extraction
4. Session aggregation
5. Agency-oriented reporting

## Construct-to-measure discipline

The repository intentionally distinguishes **constructs** from **proxies**. A behavioral feature may be consistent with a construct without proving that construct exists. A real study should establish content validity, reliability, sensitivity to context, and convergent/discriminant evidence before attaching strong interpretations.

## Minimum empirical extension

1. Pre-register the main research question and analysis plan.
2. Recruit a context-appropriate sample with consent and a documented data-governance plan.
3. Establish annotation reliability or measurement reliability before model comparison.
4. Split exploratory analysis from confirmatory evaluation.
5. Report uncertainty, subgroup performance, missing-data patterns, and negative findings.
6. Evaluate whether the output is understandable and useful to the people expected to act on it.

## Threats to validity

- Intent tagging is deliberately transparent and lightweight; it is not a validated psychological classifier.
- The included data are synthetic and cannot support claims about real learners.
- Agency-related features are descriptive research signals, not diagnostic labels or grading criteria.

## Next experiments

- Replace rule-based intent tagging with a validated transformer classifier and report calibration.
- Add sequence models for interaction trajectories rather than only session aggregates.
- Run a learner/teacher co-design study to test whether the dashboard supports useful reflection.
