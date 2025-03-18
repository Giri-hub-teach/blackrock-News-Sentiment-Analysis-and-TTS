def get_comparative_analysis(sentiments):
    positive = sum(1 for s in sentiments if s['sentiment'] == 'POSITIVE')
    negative = sum(1 for s in sentiments if s['sentiment'] == 'NEGATIVE')
    neutral = sum(1 for s in sentiments if s['sentiment'] == 'NEUTRAL')
    
    comparative_result = {
        "positive": positive,
        "negative": negative,
        "neutral": neutral
    }
    return comparative_result
