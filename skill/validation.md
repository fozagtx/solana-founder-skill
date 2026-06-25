# Solana Market Validation

Use this when the user asks whether an idea is worth building, how to validate, how to interview users, how to run a pilot, or how to define minimum evidence.

## Core Principle

Validation is behavioral evidence, not encouragement. In Solana, the best signal usually comes from one of these:

- A builder integrates or tries the tool in a real project
- A protocol, wallet, or infra team books a follow-up
- A user repeats the action without hand-holding
- A team commits to a paid pilot, grant milestone, LOI, or intro
- A community asks for the next version after seeing a working artifact

Compliments, likes, retweets, hackathon applause, and Discord enthusiasm are useful only if they convert into behavior.

## Minimum Success Criterion

Before any test, define:

```text
Hypothesis:
[What must be true]

Target user:
[Exact ICP]

Test:
[What you will show or ask them to do]

Minimum success criterion:
[Concrete count and timeframe]

Failure rule:
[What you will change or kill if the test misses]
```

Examples:

- "Within 72 hours, 5 of 20 Solana wallet PMs reply, and 2 agree to show us recent failed-support tickets."
- "Within 7 days, 3 hackathon teams use the SDK template to complete a devnet transaction without live help."
- "Within 5 days, 2 DeFi protocols agree to a paid pilot or named design partnership."

## Validation Methods

### 1. Problem Thread Mining

Use when the pain may already be public.

Where to look:

- GitHub issues and discussions for relevant Solana tools
- Solana Stack Exchange questions
- Protocol Discords, Telegrams, and governance forums
- X search for exact error phrases, "how do I", "any tool for", "alternative to"
- Support channels for wallets, RPC providers, SDKs, and marketplaces

Process:

1. Write 10 to 15 phrases the ICP would use when stuck.
2. Capture at least 20 live examples.
3. Tag each example by root cause, urgency, workaround, and buyer/user type.
4. Count repeated patterns.
5. Promote only repeated pains into an ICP or offer hypothesis.

Output:

```text
Pain cluster:
Frequency:
Representative quote:
Current workaround:
Likely buyer/user:
Validation next step:
```

### 2. Concierge Pilot

Use when the user can manually deliver the outcome before building automation.

Best for:

- Analytics reports
- Wallet support tooling
- Compliance or risk workflows
- Protocol onboarding
- Integration support
- Data extraction or monitoring

Steps:

1. Pick 3 to 5 exact teams.
2. Offer to manually produce the result once.
3. Ask for one concrete artifact: logs, screenshots, GitHub issue, transaction signature, support tickets, dashboard export, or workflow recording.
4. Deliver the result in 48 to 72 hours.
5. Ask: "Should this exist as a product? What would make you use it weekly?"

Strong signal:

- They ask for a second run
- They invite another teammate
- They ask about price, integration, API, or timeline
- They give access to real workflow data

### 3. Developer Dry-Run

Use for SDKs, APIs, CLIs, templates, and devtools.

Test the "time to first value":

1. Give 3 to 5 target developers the repo, docs, or template.
2. Ask them to complete one exact task.
3. Watch where they stall.
4. Measure time, errors, unsupported assumptions, and questions.
5. Do not explain unless they are fully blocked. The confusion is the data.

Minimum evidence examples:

- 3 of 5 developers complete setup in under 15 minutes
- 2 teams ask to use it in a real project
- 1 external contributor opens a useful issue or PR
- The same missing docs problem appears in 3 sessions

### 4. Fake-Door or Waitlist Test

Use when the user can state the promise clearly but the product is not ready.

Avoid vanity metrics by requiring a second action:

- Email signup plus booked call
- Wallet address plus usage intent
- Discord join plus completed form
- Waitlist plus uploaded workflow artifact
- Button click plus reply to "what are you trying to solve?"

Minimum success should include commitment, not just conversion rate.

### 5. Paid Pilot Test

Use when the product has obvious B2B value.

Offer structure:

```text
In [timeframe], we will help [ICP] achieve [outcome] by [manual or semi-automated mechanism].
You get [2 to 3 deliverables].
Pilot price: [$X] or grant-funded milestone.
Success metric: [specific result].
```

If the buyer will not pay, ask what commitment they will make instead: design partner quote, data access, public case study, technical integration, or intro to a similar team.

### 6. Hackathon Proof Sprint

Use for pre-submission projects.

In 7 days:

1. Day 1: Pick one ICP and one painful demo scenario.
2. Day 2: Interview 5 target users or collect 15 public pain examples.
3. Day 3 to 4: Build only the demo path that proves the pain-to-outcome loop.
4. Day 5: Run 3 user dry-runs.
5. Day 6: tighten the demo, docs, and submission narrative.
6. Day 7: produce proof: screenshots, quotes, usage clips, GitHub issues, test results, or integration evidence.

## Interview Rules

Use past behavior questions:

- "Walk me through the last time this happened."
- "What did you do next?"
- "What did it cost you in time, money, risk, or support load?"
- "What have you already tried?"
- "Who else had to approve or help?"
- "What would make you switch?"

Avoid:

- "Would you use this?"
- "Would you pay for this?"
- "Do you like the idea?"
- "Is this cool?"

## Validation Output

When asked to design a validation plan, return:

```text
Hypothesis:

ICP:

Weakest assumption:

Test method:

48-hour setup:

Minimum success criterion:

Script or artifact:

What to measure:

Pass action:

Fail action:
```

## Diagnose Failed Validation

If a test fails, inspect in order:

1. Wrong ICP: the person does not feel the pain urgently.
2. Weak trigger: the problem is real but not now.
3. Weak promise: they do not understand the outcome.
4. Wrong channel: they did not see or trust the message.
5. Ask too big: the next step required too much commitment.
6. Solana necessity weak: the chain aspect adds friction without enough benefit.
7. Build quality too low: the artifact could not create confidence.

Change one variable at a time. Do not rewrite the whole strategy after one miss.
