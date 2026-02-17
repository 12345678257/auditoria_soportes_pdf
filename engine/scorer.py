def decide(hits, review_threshold=40):

    reject_hits = [h for h in hits if h["severity"] == "REJECT"]
    review_hits = [h for h in hits if h["severity"] == "REVIEW"]

    if reject_hits:
        return "RECHAZADO"

    review_score = sum(h["weight"] for h in review_hits)

    if review_score >= review_threshold:
        return "REVISION"

    return "APROBADO"
