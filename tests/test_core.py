import pandas as pd
from genai_learning_observatory.core import classify_intent, session_features

def test_intent():
    assert classify_intent('Can you verify this with a source?')=='verification'
    assert classify_intent('Help me reflect on my reasoning')=='reflection'

def test_features_bounds():
    df=pd.DataFrame([dict(learner_id='L1',session_id='S1',prompt='explain this',verified=1,revised=1,adopted=0,reflected=1,latency_s=12),dict(learner_id='L1',session_id='S1',prompt='check this',verified=1,revised=0,adopted=0,reflected=0,latency_s=18)])
    out=session_features(df)
    assert 0 <= out.loc[0,'agency_index'] <= 1
    assert out.loc[0,'prompt_count']==2
