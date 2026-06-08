# Canon Connections

This document defines the public-safe connection model between the API repository and the broader Design Orchard / DrMarchand ecosystem.

## Core Rule

Design Orchard LLC is the legal and publishing root.

DrMarchand’s Laboratory is the business-facing Lab doorway.

DrMarchand’s Library is the archive, record, proof, and documentation lane.

The API repository exposes public-safe protocol and routing contracts only.

## Engine Compensation Model

The public canonical engine umbrella is:

```txt
DrMarchand’s Continuity Engine™ / DCE
```

The preserved internal or historical execution subsystem is:

```txt
DrMarchand’s Nɛuro-Forge Engine™ / NFE
```

The relationship is:

```txt
DrMarchand’s Continuity Engine™ / DCE
→ public engine umbrella
→ continuity, routing, archive, API, and governance surface

DrMarchand’s Nɛuro-Forge Engine™ / NFE
→ internal, historical, or implementation-specific execution subsystem
→ valid where implemented, versioned, or required for provenance
→ not the standalone public API umbrella
```

This model preserves provenance while preventing older engine naming from overriding the current public canon.

## Repository Routing

```txt
DrMarchand-Library/api
→ public API and protocol surface
→ exposes public-safe routing contracts
→ must not contain private proof records, credentials, confidential material, or raw identity records

DrMarchand-Library/DrMarchand-Laboratory
→ private continuity and implementation documentation layer
→ records current architecture, governance, and implementation evidence
→ source of truth for private Lab continuity records

DrMarchand/Creative.Canvas
→ creative archive and staging lane
→ may reference the ecosystem, but does not publish or govern the system
→ artwork remains artist-aware unless expressly assigned or licensed
```

## Boundary Rule

Public API documentation may describe stable public contracts, names, schemas, endpoints, and safety boundaries.

Private implementation proof, sensitive records, credentials, client-confidential materials, and raw identity records belong outside public repositories.

## Validation Checklist

Before publishing or merging public API documentation, verify that it:

- Uses DCE as the public engine umbrella.
- Uses NFE only as internal, historical, or implementation-specific subsystem language.
- Does not flatten distinct author, operator, and legal identities.
- Does not publish credentials, private proof records, confidential records, or raw identity records.
- Keeps Creative Canvas descriptive and non-governing.
- Keeps Design Orchard LLC as the legal and publishing root.
