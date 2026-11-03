# Learning progress

Last updated: 2026-11-03. Day 1 tutorial checkpoints complete; Day 2 prepared. Day 1 demo and homework skipped by learner request.

## Learner context

- Has coded in C/JavaScript previously and currently uses Java; can write programs but feels rusty.
- Wants practical Python skills and eventually small Gen AI applications.
- Has excluded Django from this curriculum.
- Can dedicate 1–2 hours daily for seven learning days.
- Reports difficulty with error handling, files, and threads.
- Usually inspects terminal errors, then asks AI when stuck.

## Diagnostic evidence

- Correct: basic type names, variable reassignment prediction, arithmetic operators, conditions, basic indexing, loop accumulation, max(a,b), fixing an even-number function.
- Needs practice: input() returns str; adding an integer to it without conversion raises TypeError.
- Range boundaries: initially included stop value; latest range(2,7,2) prediction was correctly 2,4,6. Developing; independent use and delayed recall pending.
- Data modelling: proposed a valid mixed list for student fields; dictionaries still need practice.
- Function tracing: initial double(4) + 1 prediction omitted the final addition. Latest add_bonus example identified intermediate 15 and final 30. Only 30 is printed. Developing.
- String repetition: predicted an error for '12' * 2. It returns '1212'; conversion before multiplication gives 24. Needs practice.
- Positive sum: understands loop/condition/accumulation pattern. Latest submission was pseudocode, not a complete function; omitted initialisation and return and included zero. Exact Python syntax and complete function construction remain unverified.

## Next step

Day 1 tutorial READMEs are prepared in Day 1/tutorials. Start interactively with Lesson 1: types, string repetition and conversion. Collect checkpoint answers before moving to the next lesson. The final tutorial checkpoint is a complete sum_positive(numbers) function. Demo and homework projects must wait until the tutorial is complete, as requested by the learner.

## Daily review log

No completed daily review yet. Record completed work, remaining gaps, changes to curriculum, and the next exercise at each session end.

## Workspace location

Use D:\Tutorials\Python Tutorial for tutorial notes, demos, and homework. The learner works in this folder in VS Code.

## Day 1 review — 2026-11-03

This review supersedes the initial diagnostic's pending assessments above.
- Correct string joining vs integer addition checkpoint; identified invalid integer text. Decimal input implementation still converted to int too early; corrected with feedback. Retain decimal conversion in recall.
- Correct text splitting and independent dictionary update.
- Recognised None in append checkpoint but confused a list with a dictionary and mutation with reassignment. Explained with feedback; retain in Day 2.
- Correct range(1,6,2), independent word-count loop and empty-list explanation.
- Correct function prediction (14) and complete sum_positive implementation, returning after its loop. Two supplied test cases correct by inspection; learner did not include the empty-list test. No local exercise code was executed by the tutor.
- Basic loop and function syntax can leave dedicated instruction for now. Delayed recall and broader independent application remain pending.
- Day 1 demo and homework skipped explicitly by learner; do not claim they were completed.
- Day 2: arguments, scope, mutation/copying and combining functions. Start with recall in Day 2/README.md. Future projects remain possible; only Day 1's project was skipped.
