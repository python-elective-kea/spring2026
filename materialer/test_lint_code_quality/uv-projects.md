# `UV` init flags
Here is a list of the main options/flags you can use when initializing a project with `uv init`:

## Project Type Flags (mutually exclusive)
- `--app`: Creates a project structure for an application (flat layout).
- `--lib`: Creates a project structure for a library (src layout, includes a `py.typed` marker for type checkers).
- `--package`: Creates a project structure for a package (src layout, suitable for distributable packages).
- `--no-package`: Creates a project structure without a package (flat layout, similar to `--app`).
- `--bare`: Creates a minimal project with only a `pyproject.toml` file, skipping source directories, README, and version control setup.

## Additional Options
- `--python <version>`: Specifies the Python version for the project (e.g., `--python 3.12`).
- `--build-backend <backend>`: Specifies the build backend (e.g., `uv_build`, `hatchling`, `flit-core`, `setuptools`).
- `--description <text>`: Sets the project description.
- `--author-from git`: Uses the author information from your git config.
- `--vcs <git|none>`: Initializes a version control system (default is `git`).
- `--python-pin`: Pins the Python version in `.python-version` and `pyproject.toml`.

## Example Usage
- `uv init --lib numbers`: Initializes a library project named "numbers" with a src layout and type checker support.
- `uv init --app myapp`: Initializes an application project named "myapp" with a flat layout.
- `uv init --bare`: Creates a minimal project with only a `pyproject.toml` file.
- `uv init --lib --python 3.12 mylib`: Initializes a library project with Python 3.12 as the minimum version.

You can combine some of these flags (e.g., `--lib --python 3.12 --build-backend hatchling`).

