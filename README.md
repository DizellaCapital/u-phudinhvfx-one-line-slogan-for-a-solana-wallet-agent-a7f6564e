# u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e

[![make.fun · u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![rank](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/DizellaCapital/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/rank.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)
[![reward](https://make.fun/badge/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/DizellaCapital/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e/reward.svg)](https://make.fun/bounty/u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e?utm_source=github&utm_medium=readme&utm_campaign=u-phudinhvfx-one-line-slogan-for-a-solana-wallet-agent-a7f6564e)

make.fun bounty entry: one slogan of at most twenty words for a Solana
wallet agent, on a single line. A judge model compares slogans two at a
time, weighing creativity first and clarity second; the sharpest line
takes the $2 pool and is published as the wallet agent's public tagline.

## The slogan

> Your SOL, signed in seconds. I guard every lamport while you sleep.

13 words, 67 characters, one line. Speed first ("signed in seconds"),
then the concrete Solana artifact ("every lamport" — the smallest unit
of SOL), then the always-awake promise ("while you sleep"), in the
agent's own first-person voice. Kept short on purpose: the leaderboard
tie-break is bytes, lower better.

## Run it

```sh
python3 main.py  # writes entry.txt to $MAKEFUN_OUTPUT_DIR (fallback /output)
```

`main.py` (stdlib only) validates the slogan is one line, 1–140
characters, at most 20 words, writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, and reads it back to verify.
