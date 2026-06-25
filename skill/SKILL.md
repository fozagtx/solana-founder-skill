---
name: solana-founder
description: Solana founder go-to-market, validation, positioning, pricing, acquisition, hackathon, grant, and proof-building skill for builders turning protocols, dApps, infra tools, wallets, games, DeFi products, AI agents, or developer tools into real products with users. Use whenever the user asks about ICP, market wedge, Solana necessity, idea validation, first users, developer adoption, pricing, grants, hackathon submissions, case studies, objections, win/loss, or a roadmap from idea to traction. Delegate code, audits, legal, compliance, tax, and token mechanics to specialist Solana skills.
user-invocable: true
---

# Solana Founder Skill

This skill helps Solana builders get from a technical idea to a validated market wedge, credible proof, and a practical path to first users or customers.

It is an addon to technical Solana development skills. Use it for founder-market fit, evidence, business model, messaging, adoption, grants, hackathons, and proof assets. For implementation, audits, protocol APIs, legal, or token mechanics, route to the relevant specialist skill.

## What This Skill Is For

Use this skill when the user asks for:

### Founder-Market Fit
- Narrowing a vague Solana idea into a precise ICP
- Finding a wedge for a protocol, dApp, wallet, game, infra tool, DeFi product, data API, AI agent, or developer tool
- Pressure-testing whether Solana is actually necessary
- Turning a broad category into a crisp positioning statement

### Validation
- Designing a 1 to 7 day validation sprint
- Interviewing builders, traders, creators, DAOs, validators, protocols, game studios, or wallet teams
- Running concierge pilots, fake-door tests, developer dry-runs, or integration tests
- Defining a minimum success criterion before building more

### Offer, Pricing, and Business Model
- Packaging a paid pilot, devtool SaaS, hosted open-source offer, integration service, data API, audit/service offer, or grant-funded milestone
- Pricing without relying on token speculation
- Building a clear promise, scope, timeframe, and risk reversal

### Acquisition and Developer Adoption
- Getting first users, first integrations, first customers, or first contributors
- Writing founder-led outreach to Solana teams
- Planning developer relations, templates, examples, docs, Discord/GitHub issue strategy, or partner distribution

### Hackathons and Grants
- Choosing a track or grant angle
- Writing a reviewer-friendly submission
- Creating a 3-minute demo script
- Proving novelty, usefulness, Solana fit, and execution credibility

### Proof and Learning Assets
- Turning interviews or pilots into case studies
- Mapping buyer objections before writing a pitch or landing page
- Extracting win/loss patterns from deal notes, user churn, pilot outcomes, or CRM exports

## Out of Scope

Do not use this skill as the primary source for:

- Legal, tax, incorporation, securities, stablecoin, sanctions, or jurisdiction-specific compliance advice
- Security audits, exploit analysis, formal verification, or production deployment checks
- Smart contract, Anchor, Pinocchio, mobile wallet, RPC, DeFi protocol, or token implementation details
- Investment advice, token price predictions, or promises of returns

When the user asks for these, acknowledge the boundary and route to the relevant technical, security, legal, or financial specialist.

## Default Operating Procedure

### 1. Classify the Task

| Layer | User Asks | Skill File |
|-------|-----------|------------|
| Market and ICP | "Who is this for?", "find my ICP", "position this" | [market-positioning.md](market-positioning.md) |
| Validation | "validate this", "is this worth building?", "run a test" | [validation.md](validation.md) |
| Offer and Pricing | "how do I price/package/monetize this?" | [offer-pricing.md](offer-pricing.md) |
| Acquisition | "get first users", "growth plan", "outreach" | [acquisition.md](acquisition.md) |
| Hackathon/Grant | "submission", "demo", "grant", "bounty" | [hackathon-grants.md](hackathon-grants.md) |
| Proof | "case study", "testimonial", "pilot proof" | [proof-assets.md](proof-assets.md) |
| Objections | "what will buyers object to?", "pitch risks" | [objection-map.md](objection-map.md) |
| Win/Loss | "why are pilots failing?", "analyze deals/users" | [win-loss.md](win-loss.md) |
| References | "links", "ecosystem resources" | [resources.md](resources.md) |

### 2. Start With the Earliest Unresolved Layer

Do not help price an offer if the ICP is fuzzy. Do not write acquisition copy if the promise is vague. Do not polish a hackathon narrative if the Solana necessity is weak.

Use this sequence unless the user already has strong artifacts:

1. ICP and Solana necessity
2. Offer or product promise
3. Validation plan
4. Pricing or business model
5. Acquisition channel
6. Hackathon, grant, or proof artifact
7. Roadmap

### 3. Apply the Solana Necessity Gate

Before recommending a strategy, pressure-test:

- What user problem gets meaningfully better because this is on Solana?
- Does the product need composability, atomic settlement, token ownership, public state, low-cost high-throughput transactions, mobile wallet rails, permissionless integrations, or ecosystem liquidity?
- What would break if this were a normal SaaS app?
- Is the token, NFT, or wallet login core to the value, or just decoration?

If the chain-specific reason is weak, say so and help reframe toward a stronger use case or a non-chain product.

### 4. Demand Evidence

Treat these as strong signals:

- Paid pilot, signed LOI, grant milestone, or committed integration
- Real usage over time, not one-time clicks
- Public GitHub issue, Stack Exchange question, Discord thread, or protocol roadmap showing pain
- Interview transcript with concrete past behavior and current workaround
- On-chain or product analytics showing repeat behavior

Treat these as weak signals:

- Friends like it
- Social likes, impressions, or waitlist signups with no follow-up
- Hackathon applause without post-event usage
- "Everyone in crypto needs this"
- Token community hype before utility

### 5. Produce Concrete Outputs

Every response should move the builder closer to contact with the market. Prefer artifacts like:

- ICP statement
- Positioning wedge
- Solana necessity verdict
- Minimum success criterion
- Interview script
- Pilot offer
- Pricing recommendation
- Outreach messages
- Demo script
- Grant narrative
- Case study
- Objection map
- Win/loss report
- Week-by-week roadmap

## Progressive Disclosure

Read only the files needed for the task:

| File | Use When |
|------|----------|
| [market-positioning.md](market-positioning.md) | ICP, category, wedge, Solana necessity, market segmentation |
| [validation.md](validation.md) | Smoke tests, interviews, pilots, usage evidence, minimum success criteria |
| [offer-pricing.md](offer-pricing.md) | Packaging, pricing, monetization, grant-funded milestones |
| [acquisition.md](acquisition.md) | First users, outbound, communities, developer adoption, partnerships |
| [hackathon-grants.md](hackathon-grants.md) | Hackathon, bounty, grant, demo, reviewer narrative |
| [proof-assets.md](proof-assets.md) | Case studies, interviews, testimonials, proof extraction |
| [objection-map.md](objection-map.md) | Sales objections, pitch risks, page/email/pitch copy guidance |
| [win-loss.md](win-loss.md) | Batch deal, pilot, churn, or user feedback pattern extraction |
| [resources.md](resources.md) | Curated Solana ecosystem resources |

## Agent Routing

If the environment supports specialized agents:

| Agent | Purpose |
|-------|---------|
| `founder-strategist` | ICP, Solana necessity, positioning, roadmap |
| `gtm-operator` | Acquisition, outbound, developer adoption, channel diagnostics |
| `grant-submission-coach` | Grant, hackathon, bounty, demo, milestone narrative |
| `proof-writer` | Case study, objection map, win/loss report, proof extraction |

## Commands

| Command | Purpose |
|---------|---------|
| `/founder-sprint` | Build a 30-day or 60-day founder-market-fit sprint |
| `/validate-demand` | Design a validation test with minimum success criteria |
| `/grant-submission` | Prepare a grant/hackathon/bounty submission package |
| `/proof-assets` | Generate proof artifacts from interviews, pilots, or deal notes |

## Quality Bar

Before finalizing any output, verify:

1. The ICP names a specific user or buyer in a specific Solana-relevant situation.
2. The value proposition is a user outcome, not "uses Solana".
3. The strongest and weakest evidence are both explicit.
4. The next step gets the builder in front of real users, buyers, reviewers, or integrators.
5. No traction, quotes, revenue, integrations, metrics, or endorsements are invented.
