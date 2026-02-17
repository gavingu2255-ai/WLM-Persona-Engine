# WLM‑Persona‑Engine — Overview  
**Structure → Identity → Behavior**

The **WLM‑Persona‑Engine** is the identity and role structure layer of the WLM ecosystem.  
It transforms structural dimensions, tensions, closures, and traits into **stable, consistent, non‑collapsing personas**.

This is the **fourth major layer** of WLM:

1. SLP‑World‑Interpreter — Language → Structure  
2. WLM‑World‑Model‑Interpreter — World Model → Structure  
3. WLM‑Agent‑Behavior — Structure → Behavior  
4. WLM‑Persona‑Engine — Structure → Identity ← *this library*

It provides the missing link between **structured cognition** and **structured identity**.

---

## Why this exists

LLM personas collapse because they rely on:

- prompts  
- heuristics  
- memory hacks  
- style imitation  

None of these are structural.

The WLM‑Persona‑Engine grounds identity in:

- **dimensions** (spatial, temporal, physical, causal)  
- **tensions** (internal & external)  
- **closures** (future identity states)  
- **traits** (structural, not descriptive)  
- **role constraints**  
- **identity invariants**  

This produces personas that are:

- stable  
- consistent  
- expandable  
- logically coherent  
- non‑collapsing  

---

## What this engine does

Given structural inputs, it generates:

- **role** (normalized, structural)  
- **traits** (deterministic, ordered)  
- **invariants** (identity rules that never break)  
- **tensions** (identity pressures)  
- **closures** (future identity states)  

The output is a deterministic **Persona** object.

---

## Architecture

```
Input Structure
    ↓
Role Engine
    ↓
Trait Engine
    ↓
Invariants Engine
    ↓
Tension Engine
    ↓
Closure Engine
    ↓
Persona Generator
```

Each module is isolated, testable, and extensible.

---

## Design principles

- **Deterministic** — same structure → same persona  
- **Interpretable** — explicit identity components  
- **Modular** — each engine evolves independently  
- **Dimension‑aligned** — identity grounded in structure  
- **Expandable** — traits and roles scale cleanly  

---

## Status

MVP architecture complete.  
Identity semantics under development.

See `docs/roadmap.md` for upcoming milestones.
