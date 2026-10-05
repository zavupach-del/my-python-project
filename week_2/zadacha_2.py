def describe_order_status(status_code: int) -> str:
    match status_code:
        case 100:
            return "pending"
        case 200:
            return "confirmed"
        case x if 300 <= x <= 399:
            return "shipped"
        case _:
            return "unknown"

if __name__ == "__main__":
    tests = [100, 200, 300, 350, 399, 400, -1]
    for t in tests:
        print(t, "->", describe_order_status(t))