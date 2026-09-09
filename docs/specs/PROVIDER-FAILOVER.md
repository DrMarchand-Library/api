# Provider Failover Specification

**Status:** proposed provider-neutral contract · **Production status:** evidence-gated

## Core principle

```text
artifact identity != storage-provider identity
```

A registered artifact should keep one stable identity even when an authorized copy exists in more than one storage provider or the preferred provider changes.

## Provider model

A provider record may describe fields such as:

```text
provider_id
object_id_or_locator
copy_role
availability_state
last_verified_at
checksum_or_content_proof
visibility_boundary
```

Provider-specific object IDs, account IDs, folder names, and sharing URLs are coordinates. They do not become the artifact identity.

## Example providers

OneDrive, Dropbox, and Google Drive may participate in package or artifact discovery where authorized. Naming a provider in this specification does **not** prove that a specific account, folder, mirror, or synchronization path is currently connected.

Providers should not be permanently assigned semantic roles such as "vault," "canonical," or "public" merely from their brand name. The registered artifact and current policy determine copy role.

## Proposed failover flow

```text
artifact request
-> resolve stable artifact identity
-> read eligible provider locations
-> validate current provider availability
-> validate required content proof
-> choose an authorized usable copy
-> return or route the artifact
-> record evidence where implemented
```

A fallback must never silently widen visibility or substitute an unverified copy simply because the primary provider is unavailable.

## Engine relationship

Where implemented, **DrMarchand’s ⚙︎ Nɛuro-Forge Engine™** may validate or orchestrate provider selection through explicit Bridge interfaces. External storage providers remain external systems.

**DrMarchand’s OS™** may present provider or artifact state; it does not become the storage provider or the execution Engine.

## Validation gate

Do not claim provider failover is active until evidence establishes:

- authorized provider connections;
- stable artifact identifiers;
- deterministic selection rules;
- positive and negative availability tests;
- content-integrity checks appropriate to the artifact;
- visibility boundaries that survive failover;
- receipts or logs for the tested behavior.

```text
proposed failover != verified production failover
```
