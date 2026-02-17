# Example: Persona With Worldview  
**Worldview → Identity Logic**

This example shows how worldview can be included in the persona structure, even though the MVP does not yet use it for deep semantics.

---

## Input

```json
{
  "role": "guardian",
  "traits": ["loyal", "brave"],
  "worldview": {
    "causal": "protective",
    "temporal": "long-term"
  }
}
```

---

## Code

```python
from wlm_persona_engine import generate_persona

persona = generate_persona({
    "role": "guardian",
    "traits": ["loyal", "brave"],
    "worldview": {
        "causal": "protective",
        "temporal": "long-term"
    }
})

print(persona)
```

---

## Output (MVP)

```
{
  "role": "Guardian",
  "traits": ["brave", "loyal"],
  "invariants": ["protect-others"],
  "tensions": ["threat → defend"],
  "closures": ["future_threat → fortify"]
}
```

---

## Explanation

Even though worldview is not yet used in MVP semantics,  
the persona remains:

- deterministic  
- role‑consistent  
- trait‑normalized  
- structurally grounded  

Future versions will integrate worldview into:

- identity invariants  
- tension responses  
- closure patterns  
- long‑term persona evolution  
