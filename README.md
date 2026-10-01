# reflex-component-template

A template for publishing a React library as a [Reflex](https://reflex.dev)
component on PyPI. It comes set up with:

- [uv](https://docs.astral.sh/uv/) for dependencies and builds
- `.pyi` stubs generated at build time, so editors autocomplete every prop
- pre-commit with ruff and pyright
- a pytest suite and a demo app that CI compiles
- publishing to PyPI through trusted publishing when you push a tag
- an `AGENTS.md` for coding agents

The example wraps the `HexColorPicker` from
[react-colorful](https://www.npmjs.com/package/react-colorful).

## Start a new component

1. Click **Use this template** on GitHub and clone your new repository.
2. Rename the package:

   ```bash
   uv run scripts/rename.py reflex-my-widget --repo your-org/reflex-my-widget
   ```

3. Fill in `authors` and `description` in `pyproject.toml`.
4. Replace the example in `src/<package>/color_picker.py` with the library you are
   wrapping (rename the file too, but not to `component.py`, which the stub
   generator skips), and update `tests/` and `demo/` to match. The
   [wrapping React guide](https://reflex.dev/docs/wrapping-react/overview/)
   covers props, events and imports.
5. Install the git hooks: `uv run pre-commit install`.

## Develop

```bash
uv sync
uv run pytest
cd demo && uv run reflex run
```

## Publish

1. On PyPI, add a [trusted publisher](https://docs.pypi.org/trusted-publishers/adding-a-publisher/)
   for your repository with workflow `publish.yml` and environment `pypi`.
2. In your repository settings, create an environment named `pypi`.
3. Tag a release and push it:

   ```bash
   git tag v0.1.0
   git push origin v0.1.0
   ```

The version is taken from the tag.

## License

Apache-2.0
