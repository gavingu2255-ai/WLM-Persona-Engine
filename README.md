# WLM‑Persona‑Engine  
**Use structural dimensions to generate stable, consistent, non‑collapsing AI personas.**

The **WLM‑Persona‑Engine** is the **identity and role structure layer** of the WLM ecosystem.  
It transforms WLM structural dimensions into **stable, reproducible, logically consistent personas**  
for agents, NPCs, virtual humans, and role‑based AI systems.

This is the **fourth major layer** of WLM:

1. **SLP‑World‑Interpreter** — Language → Structure  
2. **WLM‑World‑Model‑Interpreter** — World Model → Structure  
3. **WLM‑Agent‑Behavior** — Structure → Behavior  
4. **WLM‑Persona‑Engine** — Structure → Identity / Role / Personality ← *this repo*

It provides the missing link between **structured cognition** and **structured identity**:

> **Structure → Identity → Behavior → World**

---

## ✨ Why this exists

LLM personas collapse.  
NPCs collapse.  
Virtual characters collapse.  
Role consistency collapses.

Why?

Because they rely on:
- prompts  
- heuristics  
- memory hacks  
- style imitation  
- “vibes”  

None of these are **structural**.

The WLM‑Persona‑Engine solves this by grounding identity in:

- **dimensions** (spatial / temporal / physical / causal)  
- **tensions** (internal & external)  
- **closures** (future identity states)  
- **traits** (structural, not descriptive)  
- **role constraints**  
- **identity invariants**  

This produces personas that are:

- stable  
- consistent  
- expandable  
- non‑collapsing  
- logically coherent  
- structurally grounded  

This is the **Character OS**.

---

## ✨ Features

### **1. Structural Persona Model**
Personas are defined by:

- identity dimensions  
- core tensions  
- role constraints  
- worldview closures  
- behavioral invariants  
- trait vectors  
- narrative anchors  

### **2. Deterministic Identity**
Same structure → same persona.  
No drift.  
No collapse.  
No “forgetting who they are.”

### **3. Role‑Consistent Reasoning**
Roles are structural:

- mentor  
- antagonist  
- healer  
- strategist  
- explorer  
- scientist  
- diplomat  

Each role has:

- allowed actions  
- forbidden actions  
- tension responses  
- closure patterns  

### **4. Expandable Personality Architecture**
Add traits without breaking identity:

- courage  
- curiosity  
- restraint  
- empathy  
- ambition  
- precision  

Traits interact with dimensions to produce consistent reactions.

### **5. NPC / Virtual Human Ready**
Perfect for:

- games  
- simulations  
- agents  
- virtual worlds  
- interactive narratives  
- multi‑agent systems  

---

## 🚀 Quickstart

### **Install**

```bash
pip install wlm-persona-engine
```

### **Use**

```python
from wlm_persona_engine import generate_persona

persona = generate_persona({
    "role": "strategist",
    "traits": ["calm", "analytical"],
    "worldview": {"causal": "deterministic"},
})

print(persona)
```

### **Output (MVP)**

```
Persona {
  role: Strategist
  traits: [calm, analytical]
  invariants: []
  tensions: []
  closures: []
}
```

---

## 🧠 How it works

The engine uses **WLM structural dimensions** to generate identity:

### **Spatial**
- territory  
- boundaries  
- comfort zones  
- movement patterns  

### **Temporal**
- patience  
- impulsiveness  
- long‑term vs short‑term identity  

### **Physical**
- resilience  
- fragility  
- embodiment style  

### **Causal**
- worldview  
- belief structure  
- decision logic  

Identity becomes a **stable structural object**, not a prompt.

---

## 📦 API

### `generate_persona(structure: dict) → dict`

```python
def generate_persona(structure: dict) -> dict:
    """
    Generate a deterministic persona from structural inputs.
    """
```

### Persona structure (MVP)

```json
{
  "role": "Strategist",
  "traits": ["calm", "analytical"],
  "invariants": [],
  "tensions": [],
  "closures": []
}
```

---

## 📘 Examples

### Example: NPC Persona

**Input**

```
role: healer
traits: [empathetic, cautious]
worldview: causal: restorative
```

**Output**

```
Persona {
  role: Healer
  traits: [empathetic, cautious]
  invariants: [non-violence]
  tensions: [harm_detected → protect]
  closures: [future_harm → prepare_heal]
}
```

---

## 🏗 Repository Structure

```
wlm-persona-engine/
│
├── LICENSE
├── README.md
├── pyproject.toml
├── setup.cfg
│
├── src/
│   └── wlm_persona_engine/
│       ├── __init__.py
│       ├── api.py
│       ├── persona_generator.py
│       ├── trait_engine.py
│       ├── role_engine.py
│       ├── tension_engine.py
│       ├── closure_engine.py
│       ├── invariants_engine.py
│       └── cli.py
│
├── examples/
│   ├── persona_from_role.md
│   ├── persona_from_traits.md
│   └── persona_worldview.md
│
├── tests/
│   ├── test_persona_generator.py
│   ├── test_role_engine.py
│   ├── test_trait_engine.py
│   └── test_end_to_end.py
│
└── docs/
    ├── overview.md
    ├── identity-rules.md
    ├── api.md
    └── roadmap.md
```

---

## 📄 License

MIT License  
Copyright (c) 2026  
**Wujie Gu**

---

## 🧩 Summary

The **WLM‑Persona‑Engine** is the structural identity layer of the WLM ecosystem.  
It turns dimensions, tensions, closures, and traits into **stable, consistent personas**.

It enables:

- NPCs that don’t collapse  
- agents with real identity  
- virtual humans with consistent logic  
- role‑based systems that scale  
- characters that feel alive  

A foundational component of the **WLM identity stack**.
