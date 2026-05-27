# Public ARM

ARM means **Archive Routing Manifest** in this repository context.

This document defines the public-facing routing layer for DrMarchand ecosystem records, releases, and platform surfaces attached to GitHub.

---

## Version Routing Rule

`v1` is the stable public routing lane for the current public ARM contract.

It should remain dynamic across future internal versions unless a breaking public routing change requires a new public lane.

```txt
/v1
→ current public ARM contract
→ latest verified public routing docs
→ stable external reference lane
```

Internal versions may advance independently behind the public `v1` route.

Examples:

```txt
internal build: v0.1
internal runtime: v0.2
internal docs: v0.3
public ARM: /v1
```

The public `v1` route should not be treated as a frozen historical version. It is the living stable public interface for verified current routing.

---

## Public Canonical GitHub Surface

```txt
Repository: DrMarchand-Library/api
Visibility: public
Role: public API, protocol, and routing documentation surface
Public Lane: /v1
```

This repository is the public documentation boundary for:

- API drafts
- public protocol descriptions
- public data boundaries
- naming canon
- public routing manifests
- verified public contact lanes

It must not contain private records, credentials, legal proof packets, private filesystem paths, or confidential client data.

---

## Current Public Routing Arms

| ARM | Status | Role |
|---|---|---|
| GitHub | verified | canonical public code/spec documentation surface |
| Website | planned/pending verification | public doorway and publication surface |
| Dropbox | planned/pending verification | Creative Canvas public gallery/display shelf |

Additional social platforms should not be listed as public ARMs unless the user explicitly chooses to use them and account ownership/control is verified.

---

## Naming Canon

Use:

```txt
Design Orchard LLC
KEJ Studio™
🔬 DrMarchand’s Lab⚛︎ratory™
📚 DrMarchand’s ⚛︎ Library™
DrMarchand’s ⚙︎ Nɛuro-Forge Engine™
DrMarchand’s ♾️ OS™
DrMarchand’s ∞ OS™
Marchand Micro-Molecular Services™ / MMS-768™
DrMarchand’s 🎨 Creative Canvas
```

Do not use:

```txt
♾️ ∞ OS™
Standalone ∞ OS™
InfinityOS
Creative Canvas™
Creative Canvas℠
Creative Canvas®
```

---

## Publication Relationship

```txt
KEJ Studio™ creates.
Design Orchard publishes.
```

Design Orchard LLC is the legal and publishing authority.

KEJ Studio™ is the creative release and visual publication imprint.

---

## Public Boundary Rule

Public ARMs may route people to information, releases, public artwork, and public documentation.

Public ARMs are not runtime authority.

GitHub remains the canonical public implementation documentation surface until another surface is verified and documented.
