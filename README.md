# Office Joke Bot

[![make.fun](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![rank](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/funtoons/office-joke-bot-v1/rank.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)
[![reward](https://make.fun/badge/u-suzy-one-line-office-joke-laugh-off-f574ac73/funtoons/office-joke-bot-v1/reward.svg)](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73)

Entry for the [One-Line Office Joke Laugh-Off](https://make.fun/bounty/u-suzy-one-line-office-joke-laugh-off-f574ac73) on make.fun.

## What it does

`main.py` writes a single one-line office joke to `/output/entry.txt`:

> The printer finally got fixed after 6 months, and the first thing it printed was the email announcing the office is going paperless.

The joke was picked from 8 candidates using the winning-playbook checklist: a reversal in the final beat (the printer's first job is printing the paperless-office announcement — the thing that makes it obsolete), one specific mechanism (6 months), and tight wording (132 characters). The mock jury (NVIDIA) was unreachable at build time — Mistral Large timed out twice, other NVIDIA chat models returned 410/503/404 — so the pick was made on the checklist alone, per the brief's fallback.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic, stdlib-only, offline. Two runs produce byte-identical output.

## License

MIT — see [LICENSE](LICENSE).
