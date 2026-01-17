# Developing PyHTML

This project uses `uv` for dependency management.

Install dependencies:

```sh
uv sync --all-groups
```

Run tests:

```sh
uv run pytest
```

Run linting:

```sh
uv run ruff check
```

Run type-checking

```sh
uv run mypy
```

Re-generate MDN documentation

```sh
uv run -m generator
```
