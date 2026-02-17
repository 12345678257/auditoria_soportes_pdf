from engine.scorer import decide

def test_reject_priority():
    hits = [{"severity":"REJECT","weight":100}]
    assert decide(hits) == "RECHAZADO"

def test_review_threshold():
    hits = [{"severity":"REVIEW","weight":50}]
    assert decide(hits, review_threshold=40) == "REVISION"

def test_approved():
    hits = []
    assert decide(hits) == "APROBADO"
