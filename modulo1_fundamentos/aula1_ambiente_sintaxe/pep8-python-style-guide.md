# <img src="{{ site.baseurl }}/images/female.png" width="40"> PEP 8 — Python Style Guide 

> The official Python style guide.  
> Keep code **clean, consistent, and readable**.
> Importante para seu future self.

---

## <img src="{{ site.baseurl }}/images/lens.png" width="30"> 1. Code Layout

- **Indentation:** 4 spaces (no tabs).  
<img src="{{ site.baseurl }}/images/nerd.png" width="30"> https://youtu.be/oRva7UxGQDw

- **Line length:** ≤ 79 chars 
- **Blank lines:**
  - 2 blank lines before top-level defs/classes.
  - 1 blank line between class methods.

### Imports
- One import per line.

---

## <img src="{{ site.baseurl }}/images/tick.png" width="30"> 2. Naming Conventions

| Type | Convention | Example |
|------|-------------|----------|
| Variable / Function | `lower_case_with_underscores` | `get_data()` |
| Class | `CamelCase` | `AgentModel` |
| Constant | `ALL_CAPS` | `MAX_SPEED = 10` |
| Module / Package | `short_lowercase` | `tools`, `data_utils` |

---

## <img src="{{ site.baseurl }}/images/do_it.png" width="20"> 3. Whitespace Rules

- No extra spaces inside `()`, `[]`, `{}`  

```python
  x = (1, 2, 3)
```

- One space after commas and around operators

```python
total = a + b
```

- No space before a comma or colon.

## <img src="{{ site.baseurl }}/images/conf.png" width="30"> 4. Strings and Docstrings

- Use `'single'` or `"double"` quotes consistently.
- Prefer triple quotes for multi-line strings and docstrings.

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b
```
## <img src="/images/py_text.png" width="30"> 5. Comments

- Use complete, clear sentences.
- Begin with a capital letter and a single space after `#`.
- For inline comments, leave **two spaces** before `#`.

```python
# Calculate total cost
total = price * quantity  # Apply unit price
```

## Voltem a esses abaixo mais na frente no curso...

## 🧮 6. Functions and Classes

- Keep one statement per line.
- Avoid **mutable default arguments** such as lists or dictionaries.
- Use `None` as the default argument and initialize inside the function.

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

## ⚙️ 7. Comparisons and Conditionals

- Use `is` and `is not` when comparing with `None`.
- Avoid comparing directly to `True` or `False`.
- Keep conditions explicit and readable.

```python
if result is None:
    return

if flag:
    execute_task()
```

## 🧩 8. Line Breaks

- Use parentheses for multi-line expressions.
- Avoid the backslash (`\`) for line continuation.
- Break lines to enhance readability and logical grouping.

```python
total = (
    first_value
    + second_value
    + third_value
)
```
