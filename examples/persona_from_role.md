# Example: Persona From Role  
**Role → Identity Structure**

This example shows how a persona is generated when only a **role** is provided.

---

## Input

```json
{
  "role": "healer"
}
```

---

## Code

```python
from wlm_persona_engine import generate_persona

persona = generate_persona({"role": "healer"})
print(persona)
```

---

## Output (MVP)

```
{
  "role": "Healer",
  "traits": [],
  "invariants": ["non-violence"],
  "tensions": ["harm_detected → protect"],
  "closures": ["future_harm → prepare_heal"]
}
```

---

## Explanation

The role **Healer** automatically generates:

- **Invariant:** non‑violence  
- **Tension:** harm_detected → protect  
- **Closure:** future_harm → prepare_heal  

This produces a **stable, non‑collapsing identity** even with no traits provided.
