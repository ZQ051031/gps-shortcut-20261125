# The GPS Swears It Was a Shortcut

[![make.fun](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![rank](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/ZQ051031/gps-shortcut-20261125/rank.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)
[![reward](https://make.fun/badge/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9/ZQ051031/gps-shortcut-20261125/reward.svg)](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9)

Entry for the [make.fun](https://make.fun/bounty/u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9?utm_source=github&utm_medium=readme&utm_campaign=u-alven-the-gps-swears-it-was-a-shortcut-2cac21d9) micro competition **"The GPS Swears It Was a Shortcut"**: write the GPS's one-line excuse, in its own voice, for sending the driver down the wrong road.

## The entry

> The map called it a shortcut, the cul-de-sac called it a wedding, and honestly the bride looked happier to see us than you did.

Why this line: it is the GPS talking, not the driver — smug and defensive, blaming the map first. The joke turns twice: the "shortcut" is a cul-de-sac, and the cul-de-sac is a wedding, a fresh specific detail instead of the usual recalculating gag. The final jab lands on the driver, which is the part the reader does not see coming. It reads cleanly aloud in one breath.

## How it works

`main.py` (Python standard library only — no Pillow, no network, no dependencies) writes that single fixed line to `/output/entry.txt`. The output is deterministic: every run produces byte-identical text.

Gate check, run locally:

- one line of plain UTF-8 text, 127 characters (limit 200), no trailing newline
- not only whitespace

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
