# Provider Failover Specification

## Classification

This document defines the provider-resilient storage and routing model for the DrMarchand ecosystem.

The purpose of the failover model is to preserve artifact continuity independently of storage provider availability.

---

## Core Principle

```txt
Artifact identity must not depend on storage provider identity.
```

Artifacts should remain addressable and verifiable even if:

- providers fail
- providers change
- providers migrate
- public links rotate
- infrastructure moves
- storage lanes are replaced

---

## Storage Lane Model

### OneDrive

Operational role:

```txt
business vault
private records
legal continuity
accounting and contracts
protected originals
```

### Google Drive

Operational role:

```txt
active workbench
live collaboration
core workspace
runtime drafting
continuity workspace
```

### Dropbox

Operational role:

```txt
public gallery
Creative Canvas display shelf
public releases
public artwork distribution
```

### GitHub

Operational role:

```txt
manifest truth
protocol truth
configuration truth
documentation truth
```

---

## Runtime Routing Concept

Conceptual runtime flow:

```txt
user request
→ artifact manifest lookup
→ active provider check
→ provider availability validation
→ route to first verified active provider
→ deliver artifact
```

Example:

```txt
Google Drive unavailable
→ fallback to OneDrive mirror
→ fallback to Dropbox public mirror
→ artifact identity remains unchanged
```

---

## Artifact Identity Model

Artifacts should preserve:

```txt
artifact_id
manifest identity
cryptographic hash
lineage references
metadata continuity
```

independently of:

```txt
provider URLs
provider account IDs
folder locations
public links
```

---

## Example Manifest Structure

```json
{
  "artifact_id": "creative-canvas-0001",
  "title": "Poster Release 001",
  "hash": "sha512-example",
  "providers": [
    {
      "name": "google_drive",
      "status": "primary"
    },
    {
      "name": "onedrive",
      "status": "vault_mirror"
    },
    {
      "name": "dropbox",
      "status": "public_gallery"
    }
  ]
}
```

---

## Nɛuro-Forge Engine™ Relationship

Where implemented, ⚙︎ Nɛuro-Forge Engine™ may function as:

```txt
provider router
manifest validator
artifact continuity layer
storage abstraction layer
```

This behavior should not be documented as active runtime functionality until:

- executable routing exists
- provider integrations exist
- failover behavior is tested
- deterministic results are verified
- logs confirm operational continuity

---

## DrMarchand’s ♾️ OS™ Relationship

DrMarchand’s ♾️ OS™ represents the orchestration and continuity environment target responsible for coordinating:

```txt
provider awareness
runtime continuity
artifact routing
workbench persistence
archive continuity
```

unless future implementation records define otherwise.

---

## FACT RULE

Provider failover behavior should only be documented as active if:

- providers are connected
- failover logic exists
- routing behavior is reproducible
- manifests validate correctly
- artifact continuity survives provider loss

Until then:

```txt
conceptual failover
≠
verified production infrastructure
```
