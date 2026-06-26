def filter_tokens(dependencies, exclude_pos=['PUNCT']):
    # Removes non-essential POS tags to clean syntactic noise
    return [d for d in dependencies if d['upos'] not in exclude_pos]