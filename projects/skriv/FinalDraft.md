# Final Draft Sync Problems

Short answer: no — not somewhere else in the tree. The evidence points at the same object holding different content.

Why it's not a location problem

The journal entry for that upload names its target:

remoteId = 65b40f6a-a1f0-4045-adfd-12f6fd61c4e0

That's the identical remoteId the DB has always carried for Så ska du gråta.fdx. The client is writing to the same cloud object it created on the first down-sync, not minting a new one somewhere stray.

And the enumeration counts back that up. Across every poll for hours — ROOT stays at 2 items, Project stays at 1 item. If uploads were landing as duplicates or orphans elsewhere in the Vault, those counts would be climbing. They're flat.

What's actually happening

This line is the real find:

[ERROR] INTEGRITY: Upload hash mismatch
