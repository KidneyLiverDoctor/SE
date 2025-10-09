"""
CLI Interface for Calculator Module
"""

import sys
import click
from src import calculator


@click.command(context_settings=dict(ignore_unknown_options=True))
@click.argument("operation")
@click.argument("operands", nargs=-1, type=float)
def calculate(operation, operands):
    """CLI entry point for calculator functions"""
    try:
        # Match operation names dynamically
        if not hasattr(calculator, operation):
            click.echo("Unknown operation")
            sys.exit(1)

        func = getattr(calculator, operation)

        # handle operand count
        if operation in ("add", "subtract", "multiply", "divide", "power"):
            if len(operands) != 2:
                raise TypeError("Two operands required")
            result = func(operands[0], operands[1])
        elif operation in ("sqrt", "square_root"):
            if len(operands) != 1:
                raise TypeError("One operand required")
            result = func(operands[0])
        else:
            click.echo("Unknown operation")
            sys.exit(1)

        # capture printed lines (like "Multiplying ..." etc.)
        # only print the final numeric result
        # since your calculator prints, stdout may already contain stuff
        # so we ensure last printed line or float value is shown
        if isinstance(result, float):
            click.echo(str(round(result, 2)).rstrip("0").rstrip(".") if "." in str(round(result, 2)) else str(int(result)))
        else:
            click.echo(str(result))
        sys.exit(0)

    except ValueError as e:
        if "divide" in str(e).lower():
            click.echo("Cannot divide by zero")
        else:
            click.echo(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        click.echo(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    calculate()
