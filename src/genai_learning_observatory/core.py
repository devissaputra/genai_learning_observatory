from __future__ import annotations
import re
import pandas as pd

INTENT_PATTERNS = {
    "verification": [r"check", r"verify", r"is this correct", r"source"],
    "reflection": [r"why did", r"what did i miss", r"reflect", r"my reasoning"],
    "planning": [r"plan", r"outline", r"steps", r"strategy"],
    "explanation": [r"explain", r"why", r"how does", r"help me understand"],
    "generation": [r"write", r"answer", r"solve", r"give me the final"],
}

def classify_intent(text: str) -> str:
    t=(text or "").lower()
    for label, pats in INTENT_PATTERNS.items():
        if any(re.search(p,t) for p in pats): return label
    return "other"

def add_intent_labels(events: pd.DataFrame) -> pd.DataFrame:
    out=events.copy(); out['intent']=out['prompt'].map(classify_intent); return out

def session_features(events: pd.DataFrame) -> pd.DataFrame:
    required={'learner_id','session_id','prompt','verified','revised','adopted','reflected','latency_s'}
    missing=required-set(events.columns)
    if missing: raise ValueError(f"missing columns: {sorted(missing)}")
    df=add_intent_labels(events)
    g=df.groupby(['learner_id','session_id'],as_index=False)
    out=g.agg(prompt_count=('prompt','size'),verification_rate=('verified','mean'),revision_rate=('revised','mean'),reflection_rate=('reflected','mean'),answer_adoption_rate=('adopted','mean'),median_latency_s=('latency_s','median'),intent_diversity=('intent','nunique'))
    out['agency_index']=(0.30*out.verification_rate+0.25*out.revision_rate+0.25*out.reflection_rate+0.20*(1-out.answer_adoption_rate)).clip(0,1)
    return out

def cohort_summary(features: pd.DataFrame) -> dict:
    cols=['verification_rate','revision_rate','reflection_rate','answer_adoption_rate','intent_diversity','agency_index']
    return {c: round(float(features[c].mean()),3) for c in cols}
