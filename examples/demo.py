from pathlib import Path
import json
from genai_learning_observatory.synthetic import make_demo_events
from genai_learning_observatory.core import session_features, cohort_summary

root=Path(__file__).resolve().parents[1]
events=make_demo_events(); features=session_features(events); summary=cohort_summary(features)
(root/'results').mkdir(exist_ok=True)
events.to_csv(root/'results'/'synthetic_events.csv',index=False)
features.to_csv(root/'results'/'synthetic_session_features.csv',index=False)
(root/'results'/'demo_metrics.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
