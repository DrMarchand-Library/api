# DrMarchand Library API

Public API and protocol surface for the DrMarchand ecosystem.

```txt
Legal Canopy   : Design Orchard LLC
Runtime Surface: 🔬 DrMarchand’s Lab⚛︎ratory™
Archive Surface: 📚 DrMarchand’s ⚛︎ Library™
Engine         : DrMarchand’s ⚙︎ Nɛuro-Forge Engine™
OS Layer       : DrMarchand’s ♾️ OS™
Protocol       : Marchand Micro-Molecular Services™ / MMS-768™
Public ARM     : /v1 dynamic stable routing lane
```

---

## Public ARM / v1 Rule

`/v1` is the stable public Archive Routing Manifest lane.

It represents the current verified public routing contract and may evolve across internal runtime, documentation, or infrastructure versions unless a breaking public routing change requires a new public lane.

```txt
/v1
→ current verified public routing layer
→ stable external reference surface
→ dynamic public contract
```

Internal versions may advance behind `/v1` without changing the public route.

---

## Branch Architecture

Design Orchard LLC is the legal owner, operator, publisher, rights-holder, and operational authority for the DrMarchand ecosystem.

```txt
Design Orchard LLC owns, publishes, records, and operates.
DrMarchand’s Lab⚛︎ratory™ researches and builds.
KEJ Studio™ designs and produces.
DrMarchand’s ⚛︎ Library™ archives and indexes.
Design Orchard™ publishes and holds.
DrMarchand’s ⚙︎ Nɛuro-Forge Engine™ defines and executes deterministic runtime workflows where implemented.
DrMarchand’s ♾️ OS™ provides the conceptual operating framework where implemented.
MMS-768™ verifies where implemented.
```

The Lab and KEJ Studio™ are operating, publishing, research, software, and creative production branches under Design Orchard LLC unless separately filed or registered.

---

## API Endpoints Draft

Endpoints listed in this document represent draft or planned protocol surfaces unless implementation status is explicitly documented elsewhere.

| Method | Path | Purpose |
|---|---|---|
| `GET` | `/v1/health` | Liveness/readiness probe |
| `GET` | `/v1/manifests/version` | Engine, corpus, manifest, and MMS metadata |
| `POST` | `/v1/forge/compile` | Compile a prompt/spec into a graph |
| `POST` | `/v1/forge/graph` | Execute a graph with inputs |
| `GET` | `/v1/records` | Public records index |
| `GET` | `/v1/records/{id}` | Fetch a specific public record |

---

## Security Headers Draft

```txt
X-API-Key
X-MMS768-Timestamp
X-MMS768-KeyId
X-MMS768-Signature
X-Request-ID
```

Signature pattern:

```txt
X-MMS768-Signature = SHA-512(canonical_request + timestamp + key_id)
```

No real keys, tokens, service-account JSON, or credentials should ever be committed to this repository.

---

## Public Data Boundary

This repository is public.

It must not contain:

```txt
home address records
license-matching address proof
driver license records
banking records
tax records
payroll records
raw legal proof packets
private identity records
private medical/physiology notes
service-account JSON
API keys or credentials
private Dropbox/server paths
confidential client files
```

Private proof records belong only in private company records or private repositories intentionally designated for sensitive materials.

---

## Naming Canon

Use:

```txt
Joseph “Kyle” Marchand aka DrMarchand
Design Orchard LLC
🔬 DrMarchand’s Lab⚛︎ratory™
📚 DrMarchand’s ⚛︎ Library™
DrMarchand’s ⚙︎ Nɛuro-Forge Engine™
DrMarchand’s ♾️ OS™
DrMarchand’s ∞ OS™
Marchand Micro-Molecular Services™ / MMS-768™
KEJ Studio™
DrMarchand’s 🎨 Creative Canvas
```

Do not use:

```txt
Dr. Marchand
Dr. Marchand’s Laboratory
Dr. Marchand’s Library
Creative Guild
Creative Canvas™ / Creative Canvas℠ / Creative Canvas®
MMS = Modular Memory Security as parent name
MMS~768 / MMS—768
Neuro-Forge / Nuɛro-Forge as engine canon
♾️ ∞ OS™
Standalone ∞ OS™ / InfinityOS
® without an actual registration record
```

---

## Footer Rule

```txt
© 2025-2026 Joseph “Kyle” Marchand aka DrMarchand / Design Orchard LLC. All rights reserved unless a repository license states otherwise.
DrMarchand’s ⚙︎ Nɛuro-Forge Engine™ and DrMarchand’s ♾️ OS™ are ecosystem components operating under the Design Orchard LLC publication and infrastructure structure.
```

---

## Mark Status

The listed marks are in testing, active-use, or reservation status and are not state or federally registered unless a mark-specific record says otherwise. Where actual public use, commerce, services, publication, or source-identifying activity exists, the marks are being used under common-law trademark/service-mark principles in Florida.

Creative Canvas is descriptive and is not currently claimed as a trademark or service mark.

---

## Contact Stack

```txt
Company / Sunbiz : kyle@drmarchandslab.com
Legal / IP       : legal@drmarchandslaboratory.com
Copyright / DMCA : dmca@drmarchandslaboratory.com
```

---

## License

This repository is released under the MIT License unless a file-specific notice says otherwise.

© 2025-2026 Joseph “Kyle” Marchand aka DrMarchand / Design Orchard LLC.

DrMarchand’s ⚙︎ Nɛuro-Forge Engine™ API  
📚 DrMarchand’s ⚛︎ Library™ (Protocols & Marks)
