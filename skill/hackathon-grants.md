# Hackathon, Grant, and Bounty Submission Skill

Use this when the user asks for hackathon submissions, grant applications, demo scripts, track selection, bounty entries, ecosystem proposals, or post-hackathon follow-up.

## Core Principle

Judges and grant reviewers are overloaded. They reward projects that make usefulness obvious fast:

- A real user or buyer
- A painful problem
- A working demo
- A clear Solana necessity
- Evidence beyond founder claims
- A credible next milestone

Do not lead with architecture unless the track is explicitly technical. Lead with the user problem and the demo proof.

## Submission Intake

Gather:

1. Project name and one-sentence description
2. Target user or buyer
3. Problem and current workaround
4. Why Solana is necessary
5. What works today
6. Repo, demo, screenshots, or video status
7. Evidence: users, interviews, pilots, commits, integrations, metrics, quotes, grants, or partners
8. Requested track, bounty, or grant
9. Next milestone after submission

If evidence is thin, build a 48-hour proof sprint before polishing copy.

## Reviewer-Friendly Narrative

Use this order:

1. Problem: who hurts and why now
2. Current workaround: what they do today
3. Solution: what the project does
4. Solana necessity: why the chain matters
5. Demo: what is working
6. Proof: user evidence, technical evidence, or ecosystem pull
7. Roadmap: next milestone, not vague world domination
8. Ask: grant, feedback, integration, users, bounty consideration

## Solana Fit Checklist

Score each 0 to 2:

| Criterion | 0 | 1 | 2 |
|-----------|---|---|---|
| Chain necessity | Could be normal SaaS | Some wallet/token value | Solana properties are central |
| User specificity | "crypto users" | broad segment | exact actor and trigger |
| Working demo | slides only | partial flow | end-to-end proof |
| Evidence | none | weak interest | behavioral proof |
| Ecosystem leverage | isolated | plausible integrations | clear composability or partner path |
| Safety and trust | ignored | acknowledged | clear risk controls and next audit path |
| Roadmap | vague | feature list | milestone tied to user adoption |

Interpretation:

- 0 to 5: not ready, run validation
- 6 to 9: promising but needs clearer proof or scope
- 10 to 14: submission-ready with polishing

## 3-Minute Demo Script

Use this structure:

```text
0:00 to 0:20 - The user and pain
"[ICP] lose [cost/risk/time] when [trigger]. Today they use [workaround], which fails because [reason]."

0:20 to 0:45 - The product promise
"We built [product], a [category] that helps [ICP] [outcome] by [mechanism]."

0:45 to 1:45 - Live demo
Show one painful before state, one product action, and one useful result. Avoid clicking through setup unless setup is the product.

1:45 to 2:10 - Why Solana
"This needs Solana because [specific property]. Without it, [what breaks]."

2:10 to 2:35 - Proof
"We tested this with [evidence]. The strongest signal was [behavior]."

2:35 to 3:00 - Next milestone and ask
"Next we will [milestone] by [date]. We are looking for [grant/users/integrations/feedback]."
```

## Grant Milestones

Good milestones are verifiable and user-facing:

- Public repo with reproducible setup
- Demo deployed or testnet flow live
- Docs and quickstart
- 3 design partners
- 5 developer dry-runs
- 2 integrations
- Usage dashboard
- Security checklist and remediation plan
- Case study or public pilot writeup

Weak milestones:

- "Finish backend"
- "Improve UX"
- "Launch token"
- "Grow community"
- "Do marketing"

Rewrite weak milestones into observable deliverables.

## Bounty or Skill Submission Package

When the project is a reusable AI skill, include:

```text
Repo:

Problem solved:

Who reaches for this:

Why it is novel:

Why it belongs in the Solana builder kit:

Structure:
- skill/SKILL.md router
- focused skill modules
- optional agents/commands/rules
- installer
- README and license

Safety:
- no opaque binaries
- no hidden network calls
- no invented claims
- clear delegation boundaries

Demo prompts:
1. [prompt]
2. [prompt]
3. [prompt]

Expected outputs:
[short description]
```

## Track Selection

Choose the least crowded credible track, not the fanciest one.

Decision questions:

- Which track best matches the working demo?
- Which track has judges who understand the user pain?
- Which track values the strongest evidence you have?
- Which track has fewer lookalike submissions?
- Which sponsor or ecosystem partner could adopt this after the event?

## Post-Hackathon Follow-Up

Within 72 hours:

1. Send demo and ask to everyone who showed interest.
2. Convert judge feedback into a public changelog.
3. Contact 10 target users using the demo as the artifact.
4. Ask 3 ecosystem teams for integration feedback.
5. Write one proof post: problem, demo, evidence, next ask.
6. Apply for grants only after tightening the next milestone.

## Submission Output

When asked to prepare a submission, return:

```text
One-line pitch:

Problem:

ICP:

Current workaround:

Solution:

Why Solana:

What works today:

Proof:

Demo script:

Milestones:

Risks and mitigations:

Reviewer-ready README blurb:

Next 72-hour action:
```

## Never Invent

If the user has no users, say "No user proof yet" and propose a proof sprint. If there is no working demo, say "No working demo yet" and scope the smallest demo path. Judges trust honest constraints more than inflated claims.
