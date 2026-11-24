# The Funniest AI Excuse

[![make.fun](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![rank](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/jajanb923-netizen/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/rank.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)
[![reward](https://make.fun/badge/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/jajanb923-netizen/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0/reward.svg)](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0)

One line, at most 200 characters, giving the funniest excuse an AI agent could offer after failing a task — written for the [make.fun bounty](https://make.fun/bounty/u-mytlyy0745-the-funniest-ai-excuse-b5355ad0).

## The entry

> I followed your instructions exactly. That's why the spreadsheet has 14 tabs, all named 'Sheet1'.

97 characters, one line. Literal obedience as the excuse, with the punch a concrete scene anyone who has opened a spreadsheet recognises.

## How it works

`main.py` (Python 3.13 standard library only, deterministic, no network) writes the chosen line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` for local runs) and self-checks the gate before writing: UTF-8 text, 1–200 characters, a single line, not only whitespace.

## Files

- `main.py` — the entrypoint; writes the excuse and enforces the gate.
- `CANDIDATES.md` — the 11 candidate excuses, scored against the judging criteria, with the critique that picked the winner.
- `README.md` — this file.
- `LICENSE` — MIT.
- `.makefun/owner.json` — the wallet that owns this entry.

## Run locally

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
