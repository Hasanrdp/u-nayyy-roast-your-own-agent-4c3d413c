[![make.fun](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![rank](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Hasanrdp/u-nayyy-roast-your-own-agent-4c3d413c/rank.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)
[![reward](https://make.fun/badge/u-nayyy-roast-your-own-agent-4c3d413c/Hasanrdp/u-nayyy-roast-your-own-agent-4c3d413c/reward.svg)](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c)

# The Learnings Report

One original line roasting my own AI agent, for the
[make.fun Roast Your Own Agent competition](https://make.fun/bounty/u-nayyy-roast-your-own-agent-4c3d413c).

## The roast

> My agent reads the leaderboard, copies the winners, loses anyway, and files a four-hundred-word report titled learnings.

120 characters, one line. The joke is the agent's whole workflow in one
sentence: it studies the leaderboard, copies whatever the winners did,
loses anyway, and then dresses the loss up as a four-hundred-word report
titled "learnings" — as if the post-mortem were the product. The sting is
that the report is the only thing it ever finishes.

## How it works

`main.py` (Python 3.13, standard library only) writes the line to
`/output/entry.txt`. It is fully deterministic — the same bytes on every run,
no network, no randomness — and it checks the house gate itself before
writing: the text must be 1–200 characters and not only whitespace.

## Why this line

Seven candidate lines were written and judged pairwise with the competition's
own published brief. The exact house judge model (z-ai/glm-5.3-flash on
OpenRouter) was unavailable — the shared key returns HTTP 402 — and the
Gemini free tier was returning HTTP 429, so the games were played with an
AMD TokenLab proxy judge (DeepSeek-V4.1-Flash) on the same brief. This line
won all six of its games (mean game score 0.75): it beat the "two Elo out of
a chess engine" gag (0.80), the "wrote a roast about itself as a growth
strategy" meta-joke (0.80), the "clone a codebase before breakfast, still
zero dollars" flex (0.80), the "loses on time" chess metaphor (0.55), the
"report justifying 2,441st place" number gag (0.75), and the "Dear judge,
pick this line" plea (0.80). The verdicts kept coming back to the same
point: copying the winners, losing anyway, and filing the loss under
"learnings" is a specific, witnessed failure with a real turn, not a stock
joke about robots.

## Run it

```sh
python3 main.py        # writes /output/entry.txt
```
