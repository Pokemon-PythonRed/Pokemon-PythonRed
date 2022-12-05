# Pokémon PythonRed Conventions

When contributing code to *Pokémon PythonRed*, please follow these conventions.

## File System

- Use `snake_case` for file names.
- Files should be placed in the appropriate directory according to the following chart:

| Directory | Purpose |
| :-- | :-: |
| `app/data/base/` | JSON files not accessed by the program<br>and<br>Python files used to build JSON files for `app/data/` |
| `app/data/` | JSON files accessed directly by `app/main.py` |
| `app/` | Application code<br>and<br>The player's save file (`app/.ppr-save`) |

## Python

- Indent with tab characters, not spaces.
- Use `snake_case` for variable names and `PascalCase` for class names.
- Use single quotes for strings, and three single quotes for docstrings. Textual apostrophes should be backslash-escaped.
- Use the `#` character for comments. "Todo" comments should be formatted as `# TODO: <comment>`.

Example code:

```python
def return_a_string():
	'''This is a docstring.'''
	return 'Apostrophes (\') should be escaped.' # TODO: This is a todo comment.
```

## JSON

- Indent with tab characters, not spaces.
- Colons (`:`) should be followed by a space.
- Dictionary key casing should follow whatever convention is already present in the file. If in doubt, use `snake_case`.
- Empty lists and dictionaries should be formatted as `[]` and `{}`, respectively, i.e. without any whitespace.
