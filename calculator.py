import argparse
from calculator_engine import evaluate


def calculate_expression(expression, angle_mode="DEG"):
    """Evaluate one expression using the shared safe calculation engine."""
    return evaluate(expression, angle_mode)


def format_result(result):
    if isinstance(result, float):
        if result.is_integer():
            return str(int(result))
        return f"{result:.10g}"
    return str(result)


def interactive_calculator(angle_mode="DEG"):
    print("Scientific Calculator - CLI mode")
    print("Enter a mathematical expression, or type 'exit' to quit.")
    while True:
        try:
            expression = input(">>> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if expression.lower() in {"exit", "quit"}:
            break
        if not expression:
            continue
        try:
            print(format_result(calculate_expression(expression, angle_mode)))
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
        except (ValueError, SyntaxError, OverflowError) as error:
            print(f"Error: {error}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Scientific calculator for headless/terminal environments."
    )
    parser.add_argument(
        "-e", "--expression",
        help="Evaluate one expression and exit (for example: 'sqrt(25) + 2')."
    )
    parser.add_argument(
        "--angle-mode",
        choices=("DEG", "RAD"),
        default="DEG",
        help="Angle mode used by trigonometric functions (default: DEG)."
    )
    args = parser.parse_args(argv)
    if args.expression is not None:
        try:
            print(format_result(calculate_expression(args.expression, args.angle_mode)))
            return 0
        except ZeroDivisionError:
            print("Error: Cannot divide by zero")
            return 1
        except (ValueError, SyntaxError, OverflowError) as error:
            print(f"Error: {error}")
            return 1
    interactive_calculator(args.angle_mode)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
