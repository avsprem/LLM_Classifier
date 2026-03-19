def clean_output(output: str) -> str:
    output = output.strip().upper()

    if "YES" in output:
        return "YES"
    elif "NO" in output:
        return "NO"
    else:
        return "UNKNOWN"