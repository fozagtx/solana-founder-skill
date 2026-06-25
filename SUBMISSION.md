# Submission Notes

## Project

Solana Founder Skill

## Problem

Solana builders often have strong technical execution but weak founder-market fit. They struggle to define a precise user, prove Solana necessity, validate demand, price early pilots, acquire first users, write grant or hackathon submissions, and turn early feedback into credible proof.

## Who Uses It

- Hackathon builders
- Solana devtool founders
- Protocol teams
- Wallet and consumer app teams
- Infra and data API teams
- Game teams
- DeFi and DAO product builders
- AI agent builders serving Solana workflows

## Novelty

Most Solana skills focus on implementation, protocol APIs, security, infra, or ecosystem research. This skill focuses on the founder operating layer after "I can build it": ICP, validation, pricing, acquisition, proof, objections, win/loss, and grant/hackathon readiness.

## Kit Fit

The repo follows the Solana AI Kit addon pattern:

- `skill/SKILL.md` entry point
- focused progressive-disclosure modules
- optional `agents/`
- optional `commands/`
- optional `rules/`
- installer scripts
- README
- MIT license
- local structure validator

## Safety

- No binaries
- No network calls in install scripts
- No opaque runtime behavior
- Installers copy local Markdown files only
- Clear boundaries for legal, financial, security, deployment, and implementation work

## Demo Prompts

```text
I built a Solana payment routing devtool. Help me find the ICP and validate it this week.
```

```text
Turn this hackathon project into a grant-ready submission and 3-minute demo script.
```

```text
Here are 12 lost pilot notes for our Solana wallet analytics tool. Find the real loss reasons and messaging shifts.
```

## Expected Outputs

- ICP and Solana necessity verdict
- Validation plan with minimum success criteria
- Offer and pricing recommendation
- First-user acquisition script
- Hackathon/grant submission package
- Case study or proof asset
- Objection map
- Win/loss report
