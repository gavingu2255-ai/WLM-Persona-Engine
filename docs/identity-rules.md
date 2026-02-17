# Identity Rules — WLM‑Persona‑Engine  
**How structural inputs generate stable personas**

This document defines the rules that convert structural inputs  
(role, traits, worldview, dimensions) into **identity components**.

The rules are deterministic, structural, and model‑agnostic.

---

# 1. Role Rules

Roles define the **identity backbone**.

Examples:

- Healer  
- Strategist  
- Guardian  
- Explorer  
- Diplomat  

### Role normalization

```
"strategist" → "Strategist"
"  healer  " → "Healer"
```

### Role determines:

- invariants  
- tensions  
- closures  
- behavioral tendencies  

---

# 2. Trait Rules

Traits define **identity flavor**, not behavior.

Examples:

- calm  
- analytical  
- empathetic  
- cautious  
- ambitious  

### Trait normalization

```
["Calm", " analytical "] → ["analytical", "calm"]
```

### Deterministic ordering

Traits are always sorted alphabetically.

---

# 3. Invariant Rules

Invariants are **identity rules that never break**.

Examples:

```
Healer → non-violence
Strategist → calm-decision-making
Guardian → protect-others
```

Invariants define **identity boundaries**.

---

# 4. Tension Rules

Tensions represent **identity pressures**.

Examples:

```
Healer → harm_detected → protect
Strategist → uncertainty → analyze
Guardian → threat → defend
```

Tensions define **identity reflexes**.

---

# 5. Closure Rules

Closures represent **future identity states**.

Examples:

```
Healer → future_harm → prepare_heal
Strategist → future_conflict → plan
Guardian → future_threat → fortify
```

Closures define **identity anticipation**.

---

# 6. Determinism

Identity generation must be:

- deterministic  
- reproducible  
- structurally grounded  
- role‑consistent  
- trait‑consistent  

Same input → same persona.

---

# 7. Future Extensions

- multi‑role personas  
- dynamic identity evolution  
- narrative arcs  
- structural identity conflicts  
- long‑term persona memory  
