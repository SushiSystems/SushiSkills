# apply_settings.py
# SushiSkills - https://github.com/SushiSystems/SushiSkills
# Copyright (c) 2026-present Mustafa Garip & Sushi Systems
# Licensed under PolyForm Noncommercial 1.0.0. See LICENSE.
# Commercial use requires a licence from Sushi Systems.
"""Adds the Sushi settings the shared tools read to a repository, and the backlog block to its CLAUDE.md.

Usage: python sushisystems/tooling/apply_settings.py ROOT [--alias ALIAS]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

K_UPSTREAM = Path(__file__).resolve().parents[2]
K_TEMPLATE = Path(__file__).resolve().with_name("CLAUDE_TEMPLATE.md")
K_SHARED_NAMES = (
    "K_TOOLING_PACKAGE", "K_TOOLING_MINIMUM_VERSION", "K_TOOLING_SIBLING_SOURCE",
    "K_LICENSE_HOLDER", "K_LICENSE_COMPANY", "K_LICENSE_SITE", "K_LICENSE_OPEN_LINES",
    "K_LICENSE_CLOSED_LINES", "K_LICENSE_OPEN_BOX_LINES", "K_LICENSE_CLOSED_BOX_LINES",
    "K_LOGGER_MACRO_PREFIX", "K_LOGGER_NAMESPACE", "K_LOGGER_C_PREFIX",
)
K_MODULE_SETTINGS = (
    ("K_MODULE_MANIFEST", "sushi-module.toml"),
    ("K_MODULE_DEPENDENCY_FILE", "cli/sushistack.deps.toml"),
    ("K_MODULE_HEADINGS", ("## Standalone", "## With SushiHub")),
    ("K_MODULE_WORKSPACE_READ",
     r"\bhub (?:install|add|link|doctor|status|pin)\b|SUSHISTACK_HOME|\.sushistack\b|workspace\.toml"),
)
K_BLOCK_HEADING = "## Backlog and design"
K_BLOCK = re.compile(r"```\n(## Backlog and design.*?)```", re.DOTALL)
K_ALIAS = re.compile(r'^alias\s*=\s*"([^"]+)"', re.MULTILINE)
K_EXIT_DONE = 0
K_EXIT_USAGE = 2


def _upstream_values() -> dict[str, object]:
    """Returns the values the SushiSkills settings give to the shared Sushi constants."""
    sys.path.insert(0, str(K_UPSTREAM / "tools"))
    import settings  # noqa: PLC0415

    return {name: getattr(settings, name) for name in K_SHARED_NAMES}


def missing_settings(text: str) -> list[tuple[str, object]]:
    """Returns the Sushi constants a settings file does not define yet, with their values."""
    wanted = [*_upstream_values().items(), *K_MODULE_SETTINGS]
    return [(name, value) for name, value in wanted if not re.search(rf"^{name}\b", text, re.MULTILINE)]


def apply_to_settings(root: Path) -> list[str]:
    """Appends the missing Sushi constants to a repository's settings file and returns their names."""
    path = root / "tools" / "settings.py"
    text = path.read_text(encoding="utf-8")
    added = missing_settings(text)
    if added:
        body = "".join(f"{name} = {value!r}\n" for name, value in added)
        path.write_text(text.rstrip("\n") + "\n" + body, encoding="utf-8", newline="\n")
    return [name for name, _ in added]


def claude_block(alias: str) -> str:
    """Returns the backlog and design block of the template, with the repository's CLI alias."""
    found = K_BLOCK.search(K_TEMPLATE.read_text(encoding="utf-8"))
    if found is None:
        raise ValueError(f"{K_TEMPLATE.name} holds no block")
    return found.group(1).replace("<alias>", alias)


def apply_to_claude(root: Path, alias: str) -> bool:
    """Appends the block to a repository's CLAUDE.md unless it already has one; returns whether it wrote."""
    path = root / "CLAUDE.md"
    text = path.read_text(encoding="utf-8") if path.is_file() else ""
    if K_BLOCK_HEADING in text:
        return False
    path.write_text((text.rstrip("\n") + "\n\n" if text else "") + claude_block(alias), encoding="utf-8", newline="\n")
    return True


def alias_of(root: Path) -> str | None:
    """Returns the CLI alias the module manifest of a repository names, or None."""
    manifest = root / "sushi-module.toml"
    found = K_ALIAS.search(manifest.read_text(encoding="utf-8")) if manifest.is_file() else None
    return found.group(1) if found else None


def main(argv: list[str] | None = None) -> int:
    """Applies the settings and the block to the repository named on the command line."""
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("root", type=Path)
    parser.add_argument("--alias", help="the CLI alias; read from sushi-module.toml when omitted")
    arguments = parser.parse_args(argv)
    if not (arguments.root / "tools" / "settings.py").is_file():
        print("ROOT has no tools/settings.py; copy the shared tools first", file=sys.stderr)
        return K_EXIT_USAGE
    alias = arguments.alias or alias_of(arguments.root)
    if alias is None:
        print("no alias: pass --alias or add one to sushi-module.toml", file=sys.stderr)
        return K_EXIT_USAGE
    print("settings added: " + (", ".join(apply_to_settings(arguments.root)) or "none"))
    print("CLAUDE.md block: " + ("written" if apply_to_claude(arguments.root, alias) else "already there"))
    return K_EXIT_DONE


if __name__ == "__main__":
    sys.exit(main())
