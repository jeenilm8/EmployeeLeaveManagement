"""Validate employee leave balances.

Rules:
- Leave balance must be numeric and non-negative.
- Used leave must not exceed the total allowance.
- Remaining leave must equal allowance minus used leave.
"""

def validate_leave_balance(total_leaves, used_leaves, remaining_leaves):
    values = (total_leaves, used_leaves, remaining_leaves)
    if any(not isinstance(value, (int, float)) for value in values):
        return False
    if total_leaves < 0 or used_leaves < 0 or remaining_leaves < 0:
        return False
    if used_leaves > total_leaves:
        return False
    return remaining_leaves == total_leaves - used_leaves


def main():
    examples = [
        (20, 5, 15, True),
        (12, 12, 0, True),
        (20, 5, 14, False),
        (10, 11, -1, False),
        (-2, 0, -2, False),
    ]
    for total, used, remaining, expected in examples:
        actual = validate_leave_balance(total, used, remaining)
        print(
            f"total={total}, used={used}, remaining={remaining}: "
            f"{'PASS' if actual == expected else 'FAIL'}"
        )
        if actual != expected:
            raise SystemExit(1)
    print("All leave-balance validation checks passed.")


if __name__ == "__main__":
    main()
