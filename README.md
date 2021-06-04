# Swiping Hell
As of 2021, the largest dating apps by user count all use a "swiping" mechanic where you decide whether someone is 👍 or 👎. If you both 👍 each other, then you "match" and can actually message each other.

Heterosexual men get an extremely low match rate on these apps, which is seems to lead to a positive feedback loop wherein men 👍 nearly everyone as quickly as possible, which lowers their match rate further, to which men respond by 👍ing even more profligately. Instead of carefully choosing whom to 👍, a man instead defers all the real "choosing" work to the post-match phase, spending mental effort only on the tiny fraction of women who have 👍'd him back.

But that raises a question: is this *optimal* behavior, or is it a counterproductive reaction to the frustration of getting almost no matches?

This model attempts to answer that.

# Understanding the model

Look at the `find_a_date` function in [dates.py](dates.py) to understand the "core" of the model, and hopefully that will equip you to understand the details by reading the rest of the code.
