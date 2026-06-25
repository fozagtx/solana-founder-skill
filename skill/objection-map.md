# Objection Mapping for Solana Products

Use this before writing a pitch, landing page, grant narrative, sales page, launch post, investor memo, or outbound sequence. Also use it when copy is underperforming and the user needs to diagnose missing trust.

## Core Principle

Buyers and users rarely say the deepest objection out loud. Solana products carry extra trust, UX, security, compliance, and reputation concerns. Surface those concerns before the user raises them.

## Required Inputs

Ask for:

1. Product or offer
2. ICP
3. Promise
4. Price or commitment
5. Delivery or integration mechanism
6. Proof available
7. Main alternatives, including doing nothing
8. Context: hackathon, grant, B2B sale, consumer launch, developer adoption, or partnership

Do not generate a full map from a vague brief. Ask for missing pieces first.

## Objection Layers

### Layer 1: Logical

The buyer is checking fit and ROI.

Common Solana objections:

- Is this actually useful or just another crypto tool?
- Why this over existing dashboards, RPC tools, wallets, or scripts?
- Is the integration effort worth it?
- Is pricing clear?
- Does it work with our stack?
- Does it support mainnet/devnet/test environments?
- How long until first value?

### Layer 2: Technical and Security

The buyer is checking downside risk.

Common objections:

- Will this put funds, keys, or users at risk?
- Does this require custody or privileged access?
- What happens if RPC fails or transactions are delayed?
- Can it handle high-throughput Solana workloads?
- Does it understand account model, token accounts, priority fees, and transaction failure modes?
- Has it been tested beyond a demo?
- What is the audit or review path?

### Layer 3: Economic

The buyer is checking costs, incentives, and sustainability.

Common objections:

- Is the business model sustainable without token speculation?
- Will usage costs explode?
- Are fees predictable?
- Does this add another vendor cost?
- Will grants disappear before the product is maintained?
- Is this a nice-to-have in a down market?

### Layer 4: Social and Governance

The buyer is not deciding alone.

Common objections:

- Will my team think this is too risky?
- Will governance approve this?
- Will our community see this as extractive?
- Will users trust another wallet-connected app?
- Will integration make us look less neutral?
- Will we be blamed if the partner product breaks?

### Layer 5: Identity and Reputation

The buyer is protecting status.

Common objections:

- Does using this imply our current system is broken?
- Will this make us look amateur?
- Are we backing an unproven team?
- Will this look like chasing hype?
- Are we choosing Solana-native quality, or a hackathon demo?

### Layer 6: Status Quo

Doing nothing feels safer.

Common objections:

- We can keep using spreadsheets/scripts/manual support.
- We can wait until the product is more mature.
- We can build this internally later.
- This problem is annoying but not urgent.
- No one owns this problem clearly.

## Output Format

For each objection:

```text
[Layer] [Number]
Surface form:
Root form:
Evidence needed:
Defusing copy:
Best placement:
```

Placement options:

- Hero/pitch opening
- Problem section
- Technical architecture section
- Security/trust section
- Demo narration
- Pricing section
- FAQ
- Grant risk section
- Follow-up email
- Partner proposal
- Final close

## Solana-Specific Defusing Patterns

### "Why Solana?"

Bad:

```text
Because Solana is fast and cheap.
```

Better:

```text
This workflow needs low-cost, high-frequency settlement because [specific user action] happens [frequency]. A normal SaaS database can track it, but it cannot make [ownership/composability/settlement] available to [ecosystem actors] without permission.
```

### "Is this safe?"

Bad:

```text
It is secure.
```

Better:

```text
The first version is non-custodial and read-only. It does not request signing authority. The only wallet action in the demo is [specific action]. Before production write-paths, the next milestone is [audit/review/test plan].
```

### "Will anyone pay?"

Bad:

```text
The market is huge.
```

Better:

```text
The first buyer is [ICP] after [trigger]. We are testing willingness to pay through [pilot/LOI/commitment] by [date]. The current evidence is [specific], and the weakest assumption is [specific].
```

### "Why not build internally?"

Bad:

```text
We can do it faster.
```

Better:

```text
Internal teams can build this, but it competes with roadmap work. Our wedge is [specialized data/workflow/ecosystem integration] that gets them [outcome] in [timeframe] without pulling engineers off [core priority].
```

## Placement Map

After listing objections, group them:

```text
Pitch opening:
- [objection IDs]

Demo narration:
- [objection IDs]

Security/trust:
- [objection IDs]

Pricing/commitment:
- [objection IDs]

Follow-up:
- [objection IDs]
```

## Quality Bar

The objection map is complete when:

- It includes at least one Solana necessity objection.
- It includes at least one trust/security objection.
- It includes at least one status quo objection.
- It names the evidence needed, not just copy.
- The defusing copy sounds like recognition, not pressure.
