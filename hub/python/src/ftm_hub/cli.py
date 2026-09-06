from __future__ import annotations

import argparse
from decimal import Decimal
import json

from .audit import ResearchTree
from .calculators import eclipse_umbra_radius, radial_weight


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(prog="ftm-hub")
    commands = root.add_subparsers(dest="command", required=True)
    validate = commands.add_parser("validate")
    validate.add_argument("tree")
    eclipse = commands.add_parser("eclipse")
    eclipse.add_argument("--moon-distance", type=Decimal, required=True)
    radial = commands.add_parser("radial")
    radial.add_argument("--delta", type=Decimal, required=True)
    radial.add_argument("--gamma", type=Decimal, required=True)
    return root


def main() -> None:
    args = parser().parse_args()
    if args.command == "validate":
        tree = ResearchTree.from_path(args.tree)
        print(json.dumps({"nodes": len(tree.nodes), "status": tree.summary()}, indent=2, sort_keys=True))
    elif args.command == "eclipse":
        radius = eclipse_umbra_radius(args.moon_distance)
        print(json.dumps({"normalPlaneUmbraRadiusKm": str(radius), "surfacePathWidth": "not inferred"}, indent=2))
    elif args.command == "radial":
        print(json.dumps({"weight": str(radial_weight(args.delta, args.gamma))}, indent=2))


if __name__ == "__main__":
    main()
