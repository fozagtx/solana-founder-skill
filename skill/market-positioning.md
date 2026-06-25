# Market Positioning for Solana Builders

Use this when the user needs ICP extraction, positioning, category design, market wedge, or a Solana necessity check.

## Core Principle

A strong Solana product is not "for crypto users." It is for a specific person or team in a specific moment where Solana changes the outcome.

Define the market by:

- The actor: protocol founder, wallet PM, DeFi trader, game studio, validator operator, DAO contributor, creator, developer, data team, compliance lead, or consumer
- The trigger: what changed that makes the problem urgent now
- The workaround: what they do today
- The failed alternative: why existing tools, EVM options, centralized SaaS, spreadsheets, scripts, or manual ops are not enough
- The Solana advantage: why this chain improves cost, speed, composability, ownership, settlement, UX, or distribution

## The Four Solana ICP Filters

Before going deep, pressure-test the proposed ICP:

1. Pain: Are real users already complaining, searching, hacking together workarounds, paying vendors, or requesting this from teams?
2. Budget or adoption power: Can this actor pay, integrate, sponsor, contribute, vote, refer users, or otherwise make the product win?
3. Reachability: Can the founder name where these people can be found this week, such as GitHub issues, Discords, X lists, Telegram groups, Stack Exchange, grants, hackathons, protocol forums, or partner teams?
4. Solana necessity: Does the job need Solana-specific properties, or would a normal SaaS app be simpler and better?

If any filter fails, do not pretend the idea is ready. Help the user narrow, pivot, or reframe.

## ICP Extraction Methods

### 1. Narrowing Funnel

Use when the idea is broad.

Ask:

- What broad category is this in: DeFi, payments, mobile, gaming, infra, data, wallets, NFTs, AI agents, devtools, DAO ops, consumer, or compliance?
- Within that category, who feels the pain most intensely?
- Within that group, who has a recent trigger that makes this urgent?
- What proof shows they are already trying to solve it?
- What Solana-specific constraint makes the problem different here?

Example:

```text
"A wallet analytics tool for everyone"
-> "consumer wallet teams"
-> "PMs at Solana wallets trying to reduce failed swaps and support tickets"
-> "trigger: new user campaign increased wallet support volume"
-> "Solana-specific: fast multi-step transactions and token account states create confusing UX failures"
```

### 2. Lighthouse User

Use when the founder knows one ideal team or person.

Ask:

- Name one exact user, team, or protocol you would be thrilled to help.
- What painful workflow do they repeat weekly?
- What metric would improve if your product worked?
- What would make them try it this month?
- Could you find 10 more teams with the same trigger?

Output:

```text
Lighthouse ICP: [role/team] at [type of Solana project] who is facing [trigger], currently using [workaround], and would adopt/pay because [business or adoption consequence].
```

### 3. Switch-Moment Method

Use when the product replaces an existing tool, process, chain, or vendor.

Map:

- Push: what makes the current approach painful?
- Pull: what promise would make them switch?
- Anxiety: what scares them about switching?
- Habit: what workflow, vendor, or mental model keeps them stuck?

Solana-specific switch examples:

- Switching from generic RPC to specialized infra because the app needs priority fees, webhooks, DAS, or real-time indexing
- Switching from manual Discord support to wallet-aware support tooling because transaction issues are repetitive
- Switching from EVM-first assumptions to Solana-native UX because account state, fees, and transaction composition differ

### 4. Ecosystem Wedge

Use when a product could serve many crypto ecosystems but needs a Solana beachhead.

Ask:

- Which Solana category has a repeated unsolved pain right now?
- Which existing protocol, wallet, game, marketplace, or infra tool could distribute this?
- Which integration would make the product immediately more credible?
- What wedge is narrow enough to win without a huge brand?

Good wedge:

```text
"Failed transaction recovery assistant for Solana wallets serving first-time mobile users"
```

Weak wedge:

```text
"AI support for Web3"
```

### 5. Developer Adoption Persona

Use for SDKs, APIs, CLIs, frameworks, templates, or open-source tools.

Segment by:

- Builder maturity: beginner, hackathon builder, shipped dApp team, protocol engineer, infra engineer
- Trigger: starting a project, migrating, debugging, scaling, integrating, auditing, deploying
- Success moment: first transaction, first integration, first successful test, lower CU, faster indexing, safer deployment
- Friction: unclear docs, missing examples, poor local setup, RPC issues, IDL/codegen gaps, wallet confusion

Developer ICP statement:

```text
[Developer type] building [project type] who hits [specific setup/integration/debugging trigger], wants [success moment] within [timeframe], and will adopt because [switching benefit].
```

## Solana Necessity Gate

Answer these before calling the idea Solana-native:

1. What must be public, composable, permissionless, ownable, or settled on-chain?
2. What specific Solana property matters: low fees, high throughput, fast finality, mobile wallet ecosystem, compressed NFTs, Token-2022, account model, local fee markets, or ecosystem liquidity?
3. What would be worse if built as normal SaaS?
4. What would be worse if built on another chain?
5. Does the product create value without token price appreciation?

Verdict format:

```text
Solana necessity: Strong / Medium / Weak
Reason: [one paragraph]
Risk: [what makes the chain choice fragile]
Fix: [how to strengthen or simplify the concept]
```

## Positioning Output

Produce this when the user asks for positioning:

```text
ICP:
[One sentence]

Trigger:
[What makes them need this now]

Current workaround:
[How they solve it today]

Wedge:
[Narrow beachhead]

Solana necessity:
[Strong/Medium/Weak plus reason]

Category:
[The mental shelf this should occupy]

Positioning statement:
For [ICP] who [trigger/pain], [product] is a [category] that [outcome] by [mechanism]. Unlike [alternative], it [Solana-specific advantage or differentiated proof].

Weakest assumption:
[The riskiest unproven claim]

Next evidence to collect:
[Specific action in the next 48 hours]
```

## Push Back When You Hear

- "Everyone in Solana needs this"
- "It is useful for all Web3 users"
- "We just need a token"
- "It will go viral in the community"
- "The tech is the moat"
- "We can monetize later"
- "Wallet login makes it crypto"

Respond with an evidence-seeking question:

```text
If you had to get 3 serious users this week, who exactly would you contact and what painful event would make them reply?
```
