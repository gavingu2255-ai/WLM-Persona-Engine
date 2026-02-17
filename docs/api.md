# API Specification — WLM‑Persona‑Engine  
**Public API for generating deterministic personas**

This document defines the official API surface for WLM‑Persona‑Engine.

The API is intentionally minimal, deterministic, and stable.

---

# 1. High‑Level API

The primary entry point is:

```python
generate_persona(structure) -> dict
```

### Description
Generate a deterministic persona from structural inputs.

### Signature

```python
def generate_persona(structure: dict) -> dict:
    """
    Generate a deterministic persona from structural inputs.
    """
```

### Parameters

| Name | Type | Description |
|------|------|-------------|
| `structure` | `dict` | Input structure containing role, traits, worldview, etc. |

### Returns

| Type | Description |
|------|-------------|
| `dict` | Persona structure |

---

# 2. Persona Structure

```json
{
  "role": "Strategist",
  "traits": ["analytical", "calm"],
  "invariants": ["calm-decision-making"],
  "tensions": ["uncertainty → analyze"],
  "closures": ["future_conflict → plan"]
}
```

---

# 3. CLI API

The library provides a command‑line interface:

```
wlm-persona generate <input>
```

### Usage

```
wlm-persona generate persona.json
wlm-persona generate '{"role": "healer"}'
wlm-persona generate persona.json --out output.json
```

---

# 4. Error Handling

- deterministic behavior  
- no silent failures  
- clear error messages  
- no partial personas  

---

# 5. Versioning

Semantic versioning:

- `0.x` — experimental  
- `1.x` — stable identity semantics  
- `2.x` — dynamic identity evolution  

---

# 6. Summary

The WLM‑Persona‑Engine exposes a single stable entry point:

```
generate_persona(structure) → Persona
```

This enables structured, deterministic, non‑collapsing identity generation.
