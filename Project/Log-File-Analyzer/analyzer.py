def analyze(lines):
    error = 0
    warning = 0
    info = 0

    for line in lines:
        if "ERROR" in line:
            error += 1
        elif "WARNING" in line:
            warning += 1
        elif "INFO" in line:
            info += 1

    total = len(lines)

    return error, warning, info, total