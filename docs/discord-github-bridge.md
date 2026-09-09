# API Discord / GitHub Bridge

> Public bridge documentation for repository-event routing. Live invites, guild IDs, webhook URLs, bot tokens, and private routing credentials are intentionally excluded.

**Status:** working integration specification · **Repository:** `DrMarchand-Library/api`

## Purpose

This document describes the boundary between public GitHub repository events and an authorized Discord coordination surface.

```text
DrMarchand-Library/api
        -> explicit integration / webhook
authorized Discord coordination surface
        -> human review
```

The Bridge routes notifications. It does not grant publishing, legal, trademark, archival, runtime, or organizational authority.

## Public route description

```yaml
api_bridge:
  repository: "DrMarchand-Library/api"
  operating_context: "🔬 DrMarchand’s Lab⚛︎ratory™"
  direction: "GitHub repository events -> authorized Discord coordination"
  credentials: "platform-managed; not stored in repository"
  human_review_required: true
```

Actual Discord server IDs, channel IDs, invitations, webhook URLs, and credentials belong in platform settings or an approved private registry, not in this public repository.

## System boundary

- **Design Orchard LLC** is the legal and operating company.
- **DrMarchand’s ⚙︎ Nɛuro-Forge Engine™** remains a separate execution system.
- **DrMarchand’s OS™** may present or route state but does not become Discord or GitHub.
- **📚 DrMarchand’s ⚛︎ Library™** receives eligible records only after the applicable validation and human gate.

External platforms remain external even when connected by a Bridge.

## Repository-event policy

A public integration may emit release-safe repository events such as commits, pull requests, issues, or documented status changes when configured. It should not relay secrets, private files, personal data, or unpublished operating detail.

## Secret boundary

Do not commit:

- Discord invite URLs;
- guild or channel IDs that are intended to remain private;
- webhook URLs;
- bot tokens;
- GitHub personal access tokens;
- private storage coordinates;
- local-production markers.

## Evidence boundary

This document proves the intended integration contract only. A live webhook, successful event delivery, or production integration requires separate configuration and direct runtime evidence.
