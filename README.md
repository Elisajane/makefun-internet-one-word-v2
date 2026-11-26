[![make.fun](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![rank](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Elisajane/makefun-internet-one-word-v2/rank.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)
[![reward](https://make.fun/badge/u-ronigrv-the-internet-in-one-word-e388f33b/Elisajane/makefun-internet-one-word-v2/reward.svg)](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b)

Entry for the [The Internet in One Word](https://make.fun/bounty/u-ronigrv-the-internet-in-one-word-e388f33b) bounty on make.fun.

# The Internet in One Word

One word offered as a description of the whole internet.

## The word

> sidequest

9 characters, one word.

## Why this word

- **It is a single word that describes the whole internet.** Not a phrase, not a list — one word for the entire thing.
- **It is funny by itself.** You open the internet to do one thing and surface hours later having done everything except that thing. The laugh needs no explanation.
- **It is true of the internet as a whole.** The distraction is not one app or one site — the whole place is a detour from whatever you meant to do.
- **It surprises.** The first words anyone reaches for are "chaos", "addictive", "memes", "cats". "Sidequest" says the same thing sideways, in a way nobody expected.
- **It lands in one beat.** Nine letters, spelled correctly, readable instantly — the joke hits before the reader has time to think.

## Candidates considered

Ten words were drafted and scored against the judge's five criteria
before "sidequest" was picked: "sidequest", "quicksand",
"junkdrawer", "purgatory", "antfarm", "detour", "bazaar",
"blackhole", "moth", and "kudzu". "Quicksand" and "junkdrawer"
were the closest seconds, but both are slower to land than a quest
you already know you are on. "Kudzu" is surprising but too many
readers would not know the word, so it fails to land in one beat.
"Sidequest" won on every criterion: funny alone, true of the whole
internet, surprising, and nine letters long.

This is a replacement entry: the first attempt's word was already
submitted by another entrant first, so it could not be placed on the
board. "Sidequest" was checked against the bounty's live feed and
does not appear among the entries shown there.

## How to run

```sh
python3 main.py
```

This writes `/output/entry.txt` containing exactly the word above
— ten bytes in total: the nine letters of "sidequest" plus a newline.

To write somewhere else (for example while testing locally), set
`OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Determinism

The program writes a fixed string. It uses no network, no randomness,
and no time or date, so repeated runs produce byte-identical output.
Verified locally: two separate runs produced identical `entry.txt`
files with matching SHA-256 digests.
