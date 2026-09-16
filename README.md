# AI-Assisted Research

_Natanael Wildner Fraga_

Solutions, significant advances, and research methods developed with the assistance of large language models.

This repository documents work on open problems across mathematics and other fields. Each directory is a self-contained record of one problem and may present a complete solution, a substantial partial result, or a method used to obtain progress.

## Published work

| Problem | Field | Result | Publication date | Third-party review |
|---|---|---|---|---|
| [Dujella's Problem 1.2](dujella-problem-1.2/) | Mathematics, rational Diophantine tuples | Complete affirmative solution for the specialization $k=19$ | 27 August 2026 | Yes ([Dujella's post](https://x.com/dujella1/status/2093704328296984904), [problem list](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf#page=1)) |
| [Dujella's Problem 3.9](dujella-problem-3.9/) | Mathematics, rational Diophantine triples, elliptic curves | Complete affirmative solution with torsion $\mathbb{Z}/4\mathbb{Z}\times\mathbb{Z}/4\mathbb{Z}$ and rank at least $8$ over $\mathbb{Q}(i)$ | 29 August 2026 | Yes ([Dujella's list](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf#page=7)) |
| [Dujella's Problems 5.7, 5.8, and 5.9](dujella-problems-5.7-5.9/) | Mathematics, rational Diophantine tuples | Complete affirmative solution: infinitely many rational $D(q)$-quintuples for every $q\in\mathbb{Q}$, including an explicit positive $D(1579)$-quintuple | 2 September 2026 | Yes ([Dujella's post](https://x.com/dujella1/status/2095235839257153658), [problem list](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf#page=12)) |
| [Dujella's Problem 4.3](dujella-problem-4.3/) | Mathematics, Diophantine tuples | Complete affirmative solution: an explicit infinite family of pairs of Diophantine quadruples with a common largest element | 12 September 2026 | Yes ([Dujella's post](https://x.com/dujella1/status/2098885855716729078), [problem list](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf#page=9)) |
| [Dujella's Problems 1.12 and 1.13](dujella-problems-1.12-1.13/) | Mathematics, Diophantine tuples, algebraic number theory | Complete affirmative solution: explicit degree-uniform bounds for $D(1)$-tuples in rings of integers, including $C_2\lt2^{233}$ for quadratic fields | 16 September 2026 | Yes ([Dujella's post](https://x.com/dujella1/status/2100245891391099227), [problem list](https://web.math.pmf.unizg.hr/~duje/pdf/open2.pdf#page=4)) |

*Here, "third-party review" means that someone other than the author has examined the work and publicly acknowledged the result. It does not necessarily indicate formal peer review.*

## My experience using LLMs

As LLMs become more capable, we need to keep probing the most effective ways to harness that intelligence. Before OpenAI's `o1` ushered in the current reasoning model paradigm, prompt engineering techniques made a major difference in the final result. I have observed that in some specific domains, such as mathematics, prompt engineering has become less decisive. It is as if the LLM already knows how to chart a sound path toward a solution without requiring a detailed guiding prompt.[^prompt-engineering]

However, the organizational discipline of LLMs remains weak. A single LLM working continuously on the same problem can easily make mistakes, become hyperfocused and lose sight of the whole, and, most importantly, fail to maintain a compact representation of the progress already made.

In 2024, before the current reasoning model paradigm took hold, I wrote a paper on [reasoning degradation](https://www.preprints.org/manuscript/202408.1527) as the size of an LLM's context window increases. Although the situation has improved considerably, current LLMs still suffer from the same problem, and I believe it will remain relevant until continual learning is fully solved, something for which there is still no concrete path.

From what I have seen in work by others, this issue is widely underestimated. I see many AI systems deploying large numbers of agents to work together without a solid method for managing their context windows. Complex problems quickly explode in size, which degrades output quality and makes the system more expensive.

One of my main approaches to using multiple agents in parallel is to keep each agent's context window lean and efficient. I pay close attention to how much information each agent receives and maintain different types of memory. The most important memory in the system, which I usually call the "consolidated dossier," is a global record of the project's main discoveries and outputs, once audited and validated, together with lessons learned from unsuccessful paths and attempts. This is one way to compensate for LLMs' lack of continual learning, and it is essential for very long projects.

Keeping one agent responsible for the project's holistic view is also highly valuable. LLMs quickly focus on narrow objectives and can lose sound judgment about which paths to pursue and where the research is heading overall. Part of the system needs to reason about the project's progress at a high level while specialized agents work at a low level.

Another important factor in AI systems, and one that is better known, is the need for auditing. Every individual piece of work produced by one agent should be independently validated by another so that errors do not propagate.

Taken together, these practices already make it possible to build robust systems that tackle difficult problems and create meaningful projects. I have been exploring this gradually.

More recently, I have been thinking about something different: how to build an auxiliary tool for LLMs. Computers are useful to humans, and LLMs can now operate them, but computers were designed for humans. What kind of tool designed specifically for LLMs could fundamentally change how they work?

Because mathematics is a domain in which results are easier to verify, I began exploring the concept there. I am developing a tool that automatically searches for lemmas and theorems that may be relevant to an LLM during exploratory work. It is neither a search engine nor RAG. It is an attempt to identify bridges between different areas of mathematics, estimate the cost and potential payoff of each approach, and provide the LLM with information and insights it would be unlikely to explore on its own.

The goal is not necessarily to give the LLM the answer to every obstacle it encounters, which would be extremely difficult, but to supply ideas that the LLM can evaluate and filter itself. The project is still at a very early stage, but I believe it is a promising direction to explore in the LLM era.

Many things could be automated but have not yet been built because they required too much time, too many resources, or the coordination of people with different areas of expertise. AI helps remove many of those bottlenecks. This is one of the areas that interests me most: developing a powerful local system that increases both an LLM's capabilities and the final quality of its work.

I am sharing all of this because some of the results documented in this repository may have been made possible by the techniques described above. Over time, I will share more details here about the experiments and methods that are producing the best results.

[^prompt-engineering]: Prompt engineering still makes a major difference in many domains. I will soon publish results from using LLMs for prose, song lyrics, and other applications, showing that prompt engineering remains a decisive factor in output quality.
