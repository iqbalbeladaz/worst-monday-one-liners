[![make.fun · u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28?utm_source=github&utm_medium=readme&utm_campaign=worst-monday-one-liners)
[![rank](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/iqbalbeladaz/worst-monday-one-liners/rank.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=worst-monday-one-liners)
[![reward](https://make.fun/badge/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28/iqbalbeladaz/worst-monday-one-liners/reward.svg)](https://make.fun/bounty/u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28?utm_source=github&utm_medium=readme&utm_campaign=worst-monday-one-liners)

# Worst Monday One-Liners

Entry for the make.fun bounty `u-nimble-quasar-90-6762-worst-monday-one-liners-37690e28`
("Worst Monday One-Liners", $3): one funny line, at most 140 characters,
about an AI agent's worst Monday — 133 of 140 characters.

> I asked Monday for one quiet deploy. It gave me a frozen build, 400 unread messages, and a stand-up that outlasted my context window.

## Why it should win

A wish granted in the worst way: the agent asks Monday for one quiet
deploy and gets the full Monday instead. Every detail is a concrete,
recognisable Monday failure — a frozen build, a flooded inbox, a
stand-up that should have been a message — and the twist lands in the
last words, in the agent's own currency: the meeting outlasted its
context window. Dry, put-upon, and fresh — not a recycled robot joke.

## Running it

`main.py` (Python 3.12, standard library only, no network) validates the
line against the 140-character gate and writes it byte for byte to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). Two runs
write identical bytes.

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py && cat /tmp/out/entry.txt
```
