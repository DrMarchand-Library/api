# Security Policy

## Public Repository Boundary

This repository is public-facing. Do not commit secrets, credentials, private records, client-confidential materials, regulated records, private infrastructure paths, or private proof records.

## Reporting

Report suspected security issues through the repository owner or the organization’s documented security contact. Do not disclose exploitable details publicly before the issue is reviewed.

## API Header Draft Safety

Security header names may be documented here, but live secrets, signing keys, real identifiers, and operational credentials must remain outside the repository.

## Review Checklist

Before merging security-sensitive changes, verify that:

- No secrets are present.
- No private records are present.
- Public examples are synthetic.
- DCE/NFE terminology follows `docs/canon-connections.md`.
- Implementation claims are backed by code, schema, deployment record, deterministic output, or versioned artifact.
