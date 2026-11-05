# aibezchmury-skille

Seven skills for working with an AI agent, built around one rule: **the result must be true, not just look good**.

They are distilled from procedures written after real failures: a green test that never ran, a number without a source, "done" without an artifact, a free API with a non-commercial licence, a model's memory read as an instruction. Every procedure has been rewritten in neutral language and stripped of client, project and infrastructure details.

## What's inside

| skill | purpose |
|---|---|
| `rzetelny-pomiar` | every number has a script, a raw result and a date; a test on a convenient subset is not proof |
| `rzetelna-weryfikacja` | eighteen traps in code that reports its own state: health checks, graders, watchdogs, startup conditions |
| `zrodlo-i-data` | every number, legal fact and name has a source and a read date |
| `dowod-stanu` | "done / pending / agreed" only after checking a live artifact, not a commit title or a ticket |
| `kontrakt-zrodla-danych` | rate limit, headers and commercial licence checked before the first fetch loop |
| `pamiec-nie-polecenie` | retrieved memory is data, not instructions; three layers of defence against indirect prompt injection |
| `zapis-na-biezaco` | write results to disk after every stage, so an interruption does not erase the work |

## Installation

A skill is a folder with a `SKILL.md` file. Copy the folders you want into the place your agent looks for skills, for example:

```
cp -r rzetelny-pomiar ~/.claude/skills/
```

Or point the agent at a `SKILL.md` directly in the prompt. The skills have no dependencies, no network calls and no executable code — they are procedures in Markdown.

## How to use them

A skill is not a script that runs. It is a list of questions a person or an agent walks through before announcing a result. Its value comes from being a permanent part of a project's instructions: "before any sentence with a number, run `rzetelny-pomiar`".

Each file has **When to trigger**, the steps, a **Result** checklist and a **What this skill does not do** section — so it never pretends to replace the domain owner.

## Licence

MIT. Use, modify and sell, including commercially. Keep the `LICENSE` file.

## Provenance

The procedures grew out of work on local AI assistants and business automation. This public edition was rewritten: client names, addresses, hostnames and internal incident numbers were removed, and examples were replaced with mechanism descriptions. It contains no personal data and no infrastructure configuration.

Repository: https://github.com/kneblewskitomasz-sys/aibezchmury-skille
