# Example: Persona From Traits  
**Traits → Identity Flavor**

This example shows how traits influence persona structure.

---

## Input

```json
{
  "role": "strategist",
  "traits": ["Calm", " analytical ", "Brave"]
}
```

---

## Code

```python
from wlm_persona_engine import generate_persona

persona = generate_persona({
    "role": "strategist",
    "traits": ["Calm", " analytical ", "Brave"]
})

print(persona)
```

---

## Output (MVP)

```
{
  "role": "Strategist",
  "traits": ["analytical", "brave", "calm"],
  "invariants": ["calm-decision-making"],
  "tensions": ["uncertainty → analyze"],
  "closures": ["future_conflict → plan"]
}
```

---

## Explanation

Traits are:

- normalized  
- lowercased  
- sorted deterministically  

This ensures **identity stability** across runs.

The role **Strategist** adds:

- invariant: calm‑decision‑making  
- tension: uncertainty → analyze  
- closure: future_conflict → plan  
