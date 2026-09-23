from __future__ import annotations
import numpy as np, pandas as pd

def make_demo_events(n_learners: int=24, sessions_per_learner: int=4, seed: int=7) -> pd.DataFrame:
    rng=np.random.default_rng(seed); rows=[]
    prompts=["Explain why this step works","Give me an outline","Check whether my answer is correct","Help me reflect on my reasoning","Write a possible answer","What source supports this?"]
    for learner in range(n_learners):
        agency=rng.beta(3,2)
        for session in range(sessions_per_learner):
            for turn in range(rng.integers(3,8)):
                rows.append(dict(learner_id=f'L{learner:03d}',session_id=f'L{learner:03d}-S{session:02d}',prompt=rng.choice(prompts),verified=int(rng.random()<0.2+0.6*agency),revised=int(rng.random()<0.15+0.55*agency),adopted=int(rng.random()<0.75-0.45*agency),reflected=int(rng.random()<0.1+0.55*agency),latency_s=float(rng.gamma(2.2,18))))
    return pd.DataFrame(rows)
