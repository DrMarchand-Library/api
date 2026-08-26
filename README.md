# Library API and Protocol Records

> Public documentation, specifications, and safety tooling for the `DrMarchand-Library/api` repository.

**Repository identifier:** `DrMarchand-Library/api`  
**Legal and operating company:** Design Orchard LLC  
**Status:** Working documentation and specification repository; runtime claims require execution evidence

## What it contains

| Surface | Purpose | Boundary |
|---|---|---|
| [`docs/specs/`](docs/specs/) | Interface and protocol specifications | Each specification must state implementation status |
| [`PUBLIC_DATA_BOUNDARY.md`](PUBLIC_DATA_BOUNDARY.md) | Public/private data rule | Current repository safety policy |
| [`scripts/public_privacy_lint.py`](scripts/public_privacy_lint.py) | Static privacy and credential-pattern scan | Does not replace secret scanning or review |
| [`discord.manifest.json`](discord.manifest.json) | Connection manifest | Machine-readable working record |
| [`MASTER_BRAND_STATEMENT.md`](MASTER_BRAND_STATEMENT.md) | Identity and naming boundary | Not a registration or ownership instrument |

## Public data boundary

Public files may contain source code, schemas, non-sensitive examples, evidence-gated documentation, and redacted templates. They must not contain credentials, live invitation URLs, private infrastructure, customer data, payment records, identity proof, or unsupported authority and runtime claims.

The `creative_guild` string is an internal compatibility identifier. It has no independent legal, organizational, public, trademark, publishing, or archival authority.

## Naming boundary

Public trademark and service-mark claims are paused as of August 26, 2026. Active public copy uses unmarked functional names. The private execution system’s public product name is unresolved.

Repository names, commands, routes, schemas, and file paths remain exact machine identifiers. Historical evidence remains intact and must be labeled historical or superseded.

## Validation

Run the repository privacy lint from a checkout:

```bash
python scripts/public_privacy_lint.py --root .
```

A passing result proves only that the configured patterns found no match in the scanned text files. It does not prove complete privacy, legal clearance, deployment, or production health.

## Authority and rights

- **Legal and operating company:** Design Orchard LLC
- **Author and default copyright owner:** Joseph Kyle Marchand, subject to work-specific records
- **Publisher:** Not established absent a work-specific publication record

The MIT License applies within its stated scope. File-specific and third-party notices remain controlling.

