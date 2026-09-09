# Public Archive Routing Manifest (ARM)

**Status:** public routing specification · **Deployment status:** evidence-gated

ARM means **Archive Routing Manifest** in this repository. It describes how release-safe records may identify public destinations without making those destinations authorities over the underlying record.

## Purpose

A public ARM may connect a stable record identity to intentionally published destinations such as a repository, website, release page, or public media surface.

```text
stable record identity
-> approved public destination
-> release-safe representation
```

The manifest describes routing. It does not grant legal authority, prove deployment, or make a public URL the permanent identity of the record.

## Versioning

A public routing contract may use a stable interface version such as `v1` when an implementation actually exposes that lane. Documentation must not imply that a route exists merely because a version label appears in a specification.

Breaking public-contract changes should receive an explicit new version. Internal implementation versions may evolve independently when compatibility is preserved.

## Repository role

`DrMarchand-Library/api` is the current public specification and boundary repository for release-safe API, Bridge, protocol, and routing documentation.

It must not contain private records, credentials, private filesystem paths, local-production markers, private provider locators, or confidential client data.

## Current identity vocabulary

Use current identities appropriate to the artifact, including:

- Design Orchard LLC
- 🌴 Design Orchard™
- 🏝️ Design Orchard℠
- 🔬 DrMarchand’s Lab⚛︎ratory™
- 📚 DrMarchand’s ⚛︎ Library™
- DrMarchand’s ⚙︎ Nɛuro-Forge Engine™
- DrMarchand’s OS™
- 🎥 KEJ Studio℠
- 🎬 KEJ Studio™
- DrMarchand’s 🎨 Creative Canvas

`Infinity OS` and `Infinite OS` are not current system names. The `∞` symbol is infinite-bridge architecture inside DrMarchand’s OS™, not an alternate product identity.

## Publication boundary

A public ARM may route people to intentionally released information or media. It must not expose private storage topology, internal routing coordinates, secret-bearing configuration, or material that has not passed the applicable publication gate.

Publisher status, ownership, licensing, mark status, and custody remain work-specific and must be supported by their own records.

## Validation gate

Treat a public destination as active only when the exact destination is reachable, intentionally published, and supported by current evidence. A manifest entry without that evidence remains proposed or pending.
