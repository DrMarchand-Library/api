# DrMarchand’s ⚙︎ Nɛuro-Forge Engine™ API / Public ARM v1

Public `/v1` API, protocol, and Archive Routing Manifest surface for the DrMarchand ecosystem.

```txt
Legal Entity     : Design Orchard LLC
Current DBA      : DrMarchand’s Laboratory
Runtime Surface  : 🔬 DrMarchand’s Lab⚛︎ratory™
Archive Surface  : 📚 DrMarchand’s ⚛︎ Library™
Engine           : DrMarchand’s ⚙︎ Nɛuro-Forge Engine™
OS Layer         : DrMarchand’s ∞ OS™
Protocol         : Marchand Micro-Molecular Services™ / MMS-768™
Public ARM       : /v1 dynamic stable routing lane
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

## Business and Identity Architecture

Design Orchard LLC is the legal owner, operator, publisher, rights-holder, and operational authority for the software and API layers documented here.

DrMarchand’s Laboratory, with the apostrophe, is the current business-facing DBA used by Design Orchard LLC.

DrMarchands Laboratory, without the apostrophe, is the private root for pre-company creative, design, code, and research development before formal company intake.

```txt
Design Orchard LLC owns, publishes, records, and operates.
Design Orchard LLC d/b/a DrMarchand’s Laboratory is the business-facing lab doorway.
🔬 DrMarchand’s Lab⚛︎ratory™ is the stylized runtime/public lab surface.
DrMarchand’s ⚙︎ Nɛuro-Forge Engine™ defines deterministic runtime workflows where implemented.
DrMarchand’s ∞ OS™ provides the operating framework where implemented.
DrMarchand’s ⚛︎ Library™ archives and indexes records where implemented.
KEJ Studio™ is the creative/design lane unless separately filed or authorized.
MMS-768™ verifies where implemented.
```

---

## Code and Artwork Boundary

The API, software, schemas, routing contracts, and implementation records belong to the Design Orchard LLC software layer unless a file-specific notice says otherwise.

Artwork is a separate creative asset layer. Artwork, visual media, UI art, guest-artist work, and showcased assets are licensed media unless expressly assigned in writing or identified by a file-specific notice.

Default rule:

```txt
Code stays with Design Orchard LLC.
Artwork stays artist-aware.
The system may showcase artwork only through documented permission, license, assignment, commission terms, or file-specific notice.
```

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

It must not contain private company records, client-confidential files, raw identity records, tax records, payment records, private medical notes, service-account JSON, API keys, credentials, private server paths, or private cloud paths.

Private proof records belong only in controlled private records or private repositories intentionally designated for sensitive materials.

---

## Naming Canon

Use:

```txt
Joseph “Kyle” Marchand aka DrMarchand
Design Orchard LLC
Design Orchard LLC d/b/a DrMarchand’s Laboratory
DrMarchands Laboratory
🔬 DrMarchand’s Lab⚛︎ratory™
📚 DrMarchand’s ⚛︎ Library™
DrMarchand’s ⚙︎ Nɛuro-Forge Engine™
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
Standalone ∞ OS™ / InfinityOS
® without an actual registration record
```

---

## Footer Rule

```txt
© 2025-2026 Joseph “Kyle” Marchand aka DrMarchand / Design Orchard LLC. All rights reserved unless a repository license states otherwise.
Operated through Design Orchard LLC d/b/a DrMarchand’s Laboratory.
```

---

## Mark Status

The listed marks are in testing, active-use, or reservation status and are not state or federally registered unless a mark-specific record says otherwise. Where actual public use, commerce, services, publication, or source-identifying activity exists, marks may be used under common-law trademark/service-mark principles.

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
