"""
Command-line interface for WLM‑Persona‑Engine.

Usage:
    wlm-persona generate persona.json
    wlm-persona generate '{"role": "strategist"}'
"""

import argparse
import json
import sys
from pathlib import Path

from .api import generate_persona


def load_input(input_arg: str):
    """
    Load input either from a JSON file or inline JSON string.
    """
    path = Path(input_arg)
    if path.exists() and path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            raise ValueError(f"File '{input_arg}' is not valid JSON.")
    else:
        try:
            return json.loads(input_arg)
        except json.JSONDecodeError:
            raise ValueError("Input must be a JSON file path or valid JSON string.")


def cmd_generate(args):
    try:
        structure = load_input(args.input)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    persona = generate_persona(structure)

    if args.out:
        Path(args.out).write_text(json.dumps(persona, indent=2), encoding="utf-8")
    else:
        print(json.dumps(persona, indent=2))


def main():
    parser = argparse.ArgumentParser(
        prog="wlm-persona",
        description="WLM‑Persona‑Engine CLI"
    )

    sub = parser.add_subparsers(dest="command")

    # generate
    p_generate = sub.add_parser(
        "generate",
        help="Generate a persona from structural inputs"
    )
    p_generate.add_argument("input", help="JSON file path or inline JSON string")
    p_generate.add_argument("--out", help="Write output to file")
    p_generate.set_defaults(func=cmd_generate)

    args = parser.parse_args()

    if not hasattr(args, "func"):
        parser.print_help()
        sys.exit(1)

    args.func(args)
