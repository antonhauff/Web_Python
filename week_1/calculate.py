def calculate(data, findall):
    matches = findall(r"([abc])([\+\-]?)=([abc]?)([\+\-]?\d*)")  # Если придумать хорошую регулярку, будет просто
    for v1, s, v2, n in matches:
        result = data[v1] if len(s) > 0 else 0
        ni = int(n) if len(n) > 0 else 0
        v2i = data[v2] if len(v2) > 0 else 0
        if s == '+':
            result += v2i + ni
        elif s == '-':
            result -= v2i + ni
        else:
            result = v2i + ni
        data[v1] = result
    return data
