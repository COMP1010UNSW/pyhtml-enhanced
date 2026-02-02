# Developing PyHTML

This project uses [`uv`](https://docs.astral.sh/uv/) for dependency management.

Install dependencies:

```sh
uv sync --all-groups
```

## Code quality

Run tests:

```sh
uv run pytest
```

Measure code coverage:

```sh
uv run coverage run -m pytest && uv run coverage html
```

Run linting:

```sh
uv run ruff check
```

Run type-checking:

```sh
uv run mypy
```

## Documentation

Re-generate MDN documentation:

```sh
uv run -m generator
```

Preview documentation site:

```sh
uv run mkdocs serve
```

Build documentation site:

```sh
uv run mkdocs build
```
