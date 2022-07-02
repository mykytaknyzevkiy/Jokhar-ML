def getOr(json, key, default):
    if json.get(key) is None:
        return default
    else:
        return json.get(key)