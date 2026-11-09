# English AI-tell patterns

Three tiers: **strong** (fix on one sighting), **medium** (fix when two or more appear in the same paragraph), **weak** (fix only when the whole text is saturated). The list targets rhetorical moves, not strings: a listed phrase doing real work stays; an unlisted phrase doing the same move (inflating, staging, padding) gets fixed.

Many patterns here follow blader/humanizer (MIT), which draws on Wikipedia's "Signs of AI writing."

## Strong

### 1. Fake contrast
It's not X, it's Y / not just X, but Y / This isn't about X. It's about Y. / X rather than Y / clipped tails ("..., no guessing").
- Fix: "It's not merely a song, it's a statement." → "The heavy beat makes the song feel aggressive."
- Keep a contrast when it corrects an actual misunderstanding or both sides carry information the reader needs.

### 2. One-line closers and dramatic fragments
"That's the real win." / "Let that sink in." / "The message was clear." / "No hype. No fluff. Just results." / every. single. day.
Explaining closer: after a fact or example, one more sentence that names what it showed ("That's the gap this project closes." / "This is why the change matters." / "That tells you everything about the old process.").
- Cut a closer that repeats the point or names an obvious consequence. Keep an inference that adds information next to the facts it depends on. Give it its own sentence when that makes it easier to read.

### 3. Fake depth
At its core / the real question is / what really matters / fundamentally / X is the language of Y / X becomes a trap.
- Fix: state the specific claim.

### 4. Staged run-ups
Let's dive in / Let's break this down / Here's what you need to know / Here's the thing / Honestly? / Look, / Real talk / Without further ado.
- Keep: "honestly" or "look" inside a casual sentence that is not a standalone opener.

### 5. Defensive framing
Preempting an objection no one raised, leading with a disclaimer, or burying a supported observation under layers of hedging. State the observation, judgment, or action directly. Keep uncertainty or a limit where it affects the reader's decision, including an explicit warning or prohibition when needed.
- Fix: "We're not suggesting the coating will hold up everywhere, but it may be fair to say it did reasonably well in the rain test." → "The coating held up in the rain test. Its performance in freezing weather is still unknown." Use the second sentence only when that gap is established and relevant.
- Keep: "Do not restart the pump until the valve is closed." The condition changes what the reader can safely do.

### 6. Inflated significance
Stands as a testament / marks a pivotal moment / plays a key role / reflects a broader / enduring legacy / setting the stage for / evolving landscape / indelible mark / the future looks bright / exciting times ahead / a step in the right direction / "Despite these challenges, X continues to thrive."
- Fix: keep the fact, drop the significance. End on the last concrete fact.

### 7. Summary endings
In conclusion / Ultimately / In summary / At the end of the day / All in all / "So, what are you waiting for?"
- Keep: a real conclusion that adds a decision or next step.

### 8. Chatbot residue
Great question! / Certainly! / Of course! / I hope this helps / Let me know if you'd like / Feel free to reach out / Here is a... / Would you like me to...
- Keep: greetings and sign-offs in actual letters and emails.

### 9. Overused AI words
delve, tapestry, testament, pivotal, crucial, intricate, meticulous, vibrant, showcase, underscore (verb), highlight (verb), foster, garner, bolster, enhance, landscape (abstract), realm, navigate (figurative), embark, journey (figurative), seamless, robust (figurative), leverage (verb), elevate, unlock, empower, game-changer, cutting-edge, ever-evolving, in today's fast-paced world.
- These are tells wherever they cluster. A single formal word elsewhere is not.

### 10. Shallow -ing riders
..., highlighting / underscoring / emphasizing / reflecting / symbolizing / ensuring / fostering / showcasing / contributing to...
- Fix: "The temple uses blue and gold, reflecting the community's deep connection to the land." → "The temple is painted blue and gold, colors meant to evoke bluebonnets and the Gulf."

### 11. Avoiding is / are / has
serves as, stands as, functions as, acts as, boasts, features, offers, represents.
- Fix: "The gallery boasts over 3,000 square feet." → "The gallery has 3,000 square feet."

### 12. Borrowed authority
Experts say / studies show / observers note / industry reports suggest, with no named source.
- Writing: don't use them without a source. Editing: keep the attribution and flag the gap after the text; don't turn it into a bare fact.

### 13. Decorative formatting
Bold label on every bullet ("**Performance:** ..."), emoji in headings, Title Case Headings, horizontal rules between sections, headings on a 200-word email.

### 14. Sales language
Nestled, in the heart of, breathtaking, must-visit, stunning, rich (figurative), renowned, groundbreaking, world-class, unparalleled, effortless, blazing-fast.

### 15. Wrong reader
A reply that restates the problem, the diagnosis, and the evidence before reaching the decision. Lead with the decision; keep only what the reader lacks.

## Medium

### 16. Forced triads
"innovation, inspiration, and insights" / three parallel examples where one would do / three short facts then a moral.
- Keep: three real, distinct items.

### 17. Rhetorical Q&A
"The result? A 40% drop." / "Why does this matter? Because..." / "What makes this unique is..."
- One is fine. One per paragraph is a habit.

### 18. Repeated openings
Several sentences in a row starting with the same subject ("She noted... She noted... She filed...").

### 19. Vague association
associated with, linked to, connected to, tied to, when the source knows the actual relationship.

### 20. Signposting transitions
Additionally, Furthermore, Moreover, Notably, Importantly, It's worth noting that, That said.
- Keep the ones that carry a real turn or addition.

## Weak

### 21. Dashes
One em dash is normal. A text full of them is a tell. Replace most with commas, periods, colons, or parentheses. Match a user's sample if it uses dashes.

### 22. Stacked hedges
could potentially, might arguably, it's possible that perhaps. Keep one hedge when the doubt is real.

### 23. Passive voice and missing subjects
Use active voice when it names the actor more clearly. Keep passive when the actor is unknown or irrelevant, or in academic register.

### 24. Curly quotes, title case, hyphen habits
Weak on their own; follow the target format.

## Technical text (STE-style precision)

For procedures, error messages, tool descriptions, and READMEs, also:
- One name for one thing. Do not rotate "user / customer / client" for the same entity.
- Verbs, not nominalizations: "analyze the log," not "perform an analysis of the log."
- One instruction per sentence. Number sequences of three or more steps.
- Plain verbs over soft phrasal verbs: start (not spin up), contact (not reach out), read (not dive into).
- Keep modality: "may have failed" never becomes "failed."
- Shorten until the sentence is unambiguous, not until it is shortest.
