# Solana Founder Skill

An AI agent skill for Solana builders who need to turn a technical idea into a validated product, credible hackathon or grant submission, and a repeatable path to first users or customers.

Most Solana skill coverage is excellent for code, infra, DeFi integrations, auditing, and protocol APIs. This skill covers the gap that usually kills technically strong projects anyway: unclear ICP, weak positioning, fake validation, vague pricing, low-signal hackathon materials, missing proof, and founder-led acquisition that never starts.

## What It Helps With

| Area | Outcome |
|------|---------|
| Founder-market fit | Convert a broad protocol, dApp, infra, wallet, game, DeFi, AI agent, or devtool idea into a precise Solana ICP and wedge |
| Solana necessity | Pressure-test why the product needs Solana, not just a token or generic app with wallet login |
| Validation | Design fast tests that gather behavioral evidence from builders, users, protocols, traders, creators, DAOs, validators, or teams |
| Offer and pricing | Package pilots, SaaS tiers, open-source support, protocol integrations, audits, data APIs, grants, and paid services |
| First users and customers | Pick one acquisition channel and write practical founder-led outreach for the Solana ecosystem |
| Hackathons and grants | Prepare a crisp narrative, demo script, proof checklist, and reviewer-friendly submission |
| Proof assets | Turn interviews, pilots, and deal notes into case studies, objections, win/loss analysis, and messaging shifts |

## What Makes This Different

- It is Solana-native but not code-only. It understands users, protocols, wallets, validators, DeFi teams, games, creators, DAOs, hackathons, grants, and devtools.
- It is evidence-first. It treats signups, likes, and compliments as weak signal unless they convert into calls, integrations, paid pilots, commits, usage, or repeat behavior.
- It is progressive and token-efficient. `skill/SKILL.md` routes to focused files only when needed.
- It is safe to install. The scripts only copy local Markdown skill files into a selected skills directory.
- It complements core Solana development skills instead of replacing them. For program code, security audits, token mechanics, infra setup, legal, or compliance, it tells the agent to delegate.

## Installation

### Recommended

```bash
git clone https://github.com/fozagtx/solana-founder-skill
cd solana-founder-skill
./install-custom.sh
```

The custom installer lets you choose personal or project skill locations, including `.claude/skills` and `.agents/skills`.

### Standard

```bash
./install.sh
./install.sh -y
```

Standard defaults:

- Skill location: `~/.claude/skills/solana-founder`
- Optional config copied to: `~/.claude/CLAUDE.md`

## Usage Examples

```text
I built a Solana payment routing tool but I do not know who the ICP is. Pressure-test it.
```

```text
Help me validate a wallet analytics devtool before I spend two more weeks building.
```

```text
Turn this hackathon project into a grant-ready submission and 3-minute demo script.
```

```text
Here are 15 lost pilot notes from protocols. Find the real loss patterns and messaging shifts.
```

```text
I need first users for a Solana game. Pick one channel and write the outreach.
```

## Repository Structure

```text
solana-founder-skill/
|-- .gitignore
|-- README.md
|-- LICENSE
|-- CLAUDE.md
|-- install.sh
|-- install-custom.sh
|-- skill/
|   |-- SKILL.md
|   |-- market-positioning.md
|   |-- validation.md
|   |-- offer-pricing.md
|   |-- acquisition.md
|   |-- hackathon-grants.md
|   |-- proof-assets.md
|   |-- objection-map.md
|   |-- win-loss.md
|   `-- resources.md
|-- agents/
|   |-- founder-strategist.md
|   |-- gtm-operator.md
|   |-- grant-submission-coach.md
|   `-- proof-writer.md
|-- commands/
|   |-- founder-sprint.md
|   |-- validate-demand.md
|   |-- grant-submission.md
|   `-- proof-assets.md
|-- rules/
|   `-- founder-evidence.md
`-- tests/
    `-- validate_structure.sh
```

## Skill Routing

`skill/SKILL.md` is the entry point. It classifies the task and routes to the smallest relevant module:

- `market-positioning.md` for ICP, wedge, Solana necessity, and category design
- `validation.md` for smoke tests, pilots, interviews, usage evidence, and MSCs
- `offer-pricing.md` for packaging and monetization
- `acquisition.md` for first users, developer adoption, ecosystem outbound, and partnerships
- `hackathon-grants.md` for submissions, demos, and grant narratives
- `proof-assets.md` for case studies and proof extraction
- `objection-map.md` for objection stacks and defusing copy
- `win-loss.md` for pattern extraction across pilots, deals, and lost users
- `resources.md` for source-of-truth links

## Quality Bar

The skill should make an agent:

- Ask for missing signal instead of writing strategy from vibes
- Refuse to invent traction, quotes, integrations, partners, revenue, or usage
- Treat Solana as an architectural advantage only when it is actually necessary
- Push the builder toward real-world contact within days
- Produce outputs that can be used in a pitch, grant application, launch post, outbound campaign, or founder operating plan

## Validation

Run the structure validator:

```bash
./tests/validate_structure.sh
```

It checks required files, frontmatter, relative skill links, and installer syntax.

## License

MIT. See [LICENSE](LICENSE).
