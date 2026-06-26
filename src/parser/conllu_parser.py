from conllu import parse

def load_conllu(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    return parse(data)

def extract_dependencies(tokenlist):
    dependencies = []
    for token in tokenlist:
        # Filter: Only process tokens with head relations
        if isinstance(token['id'], int) and token['head'] is not None:
            dependencies.append({
                'id': token['id'],
                'head': token['head'],
                'distance': abs(token['id'] - token['head']),
                'upos': token['upos']
            })
    return dependencies
