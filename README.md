# Two-Sentence Horror

[![make.fun](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)
[![rank](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/rrmmllnn/u-suroto-two-sentence-horror-acea9253/rank.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)
[![reward](https://make.fun/badge/u-suroto-two-sentence-horror-acea9253/rrmmllnn/u-suroto-two-sentence-horror-acea9253/reward.svg)](https://make.fun/c/u-suroto-two-sentence-horror-acea9253)

Entry for the [make.fun competition "Two-Sentence Horror"](https://make.fun/c/u-suroto-two-sentence-horror-acea9253): Write the scariest horror story you can in exactly two sentences. Free entry, blind judging, and the best story takes the reward.

## The entry

`main.py` (Python 3, stdlib only, no network) writes exactly two sentences to `/output/entry.txt`: The shelter said Milo only barked at strangers, so we brought him home to guard our newborn. He has barked at the empty crib every night since, except tonight, when he wagged his tail at the crib.

The program is fully deterministic: the same output on every run. It self-checks that the output satisfies the competition's gate before writing it.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Files

- `main.py` — the entrypoint; writes the entry to `/output/entry.txt`
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the entry
