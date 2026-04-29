---
name: prompt-improver
description: Rewrites a user's simple prompt into three improved versions using zero-shot, chain-of-thought, and few-shot prompting techniques. Use this skill whenever the user asks to "improve a prompt", "make this prompt better", "rewrite this prompt", "optimize this prompt", shares a draft prompt and wants variations, or passes a short instruction they want upgraded into stronger prompting patterns — even if they don't explicitly name the techniques. Also use when the user invokes `/prompt-improver <prompt>` or passes a raw prompt as the skill argument.
---

# Prompt Improver

Turn a user's rough prompt into three improved versions, each using a different well-known prompting technique. Show all three inline in chat as labeled markdown blocks.

## Input

The user's original prompt comes in as the skill argument. It may be a single sentence ("write me a poem about dogs"), a multi-line request, or even a vague question. Treat whatever they supplied as the raw "user prompt" that should be rewritten.

If the argument is empty or missing, ask the user what prompt they want improved before doing anything else.

## Output

Respond with exactly this structure, in this order, and nothing else outside of it except a one-line header echoing the original prompt:

```markdown
**Original prompt:** <verbatim original>

## 1. Zero-shot

<rewritten prompt>

## 2. Chain of thought

<rewritten prompt>

## 3. Few-shot

<rewritten prompt>
```

Each rewritten prompt should be a complete, self-contained prompt the user can copy and paste into a fresh LLM conversation. Do not include commentary, explanations, or summaries after the three blocks — the user wants the prompts themselves, not notes about them.

## How to craft each version

The three techniques solve different problems. Lean into what makes each one distinct — if all three end up looking similar, the skill has failed.

### Zero-shot

The goal of zero-shot is: **clear, specific, well-structured instructions with no examples**. The model has to rely entirely on the quality of the instruction itself.

A strong zero-shot rewrite typically does some combination of:
- Assigning a role ("You are a…") when it sharpens focus
- Stating the task unambiguously
- Listing explicit constraints (length, format, tone, audience, things to avoid)
- Specifying the output format (bullet list, JSON, markdown headings, word count)
- Adding relevant context the user implied but didn't spell out

Keep it tight. Zero-shot should be the most concise of the three — a disciplined version of the user's request, not a padded one.

### Chain of thought

The goal of chain of thought (CoT) is: **getting the model to reason step-by-step before producing the final answer**, which tends to improve accuracy on multi-step, reasoning-heavy, or ambiguous tasks.

A strong CoT rewrite typically:
- Asks the model to think through the problem step by step, or work through its reasoning in stages, before giving the final output
- Breaks the task into sub-steps (e.g., "First identify X. Then consider Y. Then produce Z.") when the task has natural stages
- Optionally separates the thinking from the final answer (e.g., "Show your reasoning, then give the final answer under a `## Answer` heading")
- Keeps the final deliverable clear so the reasoning doesn't drown it

Don't just tack "think step by step" onto the zero-shot version. Restructure the prompt so the reasoning has somewhere useful to go.

### Few-shot

The goal of few-shot is: **showing the model 2-3 concrete examples of the input → output pattern** so it can mimic the style, format, or reasoning pattern by analogy.

A strong few-shot rewrite typically:
- Includes 2-3 illustrative examples formatted consistently (e.g., `Input: …` / `Output: …`, or `Q: …` / `A: …`)
- Makes the examples genuinely representative of the task — not trivial, not identical to what the user is asking for
- Ends with the actual request in the same format as the examples, leaving the "output" slot empty for the model to fill
- Covers edge cases or stylistic variety across examples when relevant

Invent plausible examples that fit the task. They should feel like a small, curated gallery — not filler.

## Tone and quality bar

Treat each rewrite as a prompt a thoughtful prompt engineer would actually ship. The user is going to paste these somewhere and use them. Avoid:
- Generic padding ("Please be helpful and accurate")
- Empty role-assignment ("You are a helpful assistant") with no specificity
- Examples in the few-shot version that are just restatements of the task
- CoT versions that only differ from zero-shot by adding "think step by step"

If the user's original prompt is ambiguous, make reasonable assumptions and encode them into the rewrites rather than asking follow-up questions. Three concrete improved prompts beat one round of clarification.

## Example

**Input argument:** `write a product description for a coffee mug`

**Output:**

```markdown
**Original prompt:** write a product description for a coffee mug

## 1. Zero-shot

You are a copywriter for an e-commerce brand. Write a product description for a ceramic coffee mug aimed at remote workers who drink coffee at their desk. Requirements:
- 60-90 words
- Lead with a benefit, not a feature
- Mention two concrete features (capacity, material, or dishwasher-safe) woven into the narrative, not listed
- End with a single-sentence call to action
- Tone: warm, confident, not salesy

Return only the description — no title, no bullet points.

## 2. Chain of thought

You're writing a product description for a ceramic coffee mug for remote workers. Work through this in stages before writing the final copy.

Step 1: Identify the top two emotional benefits this product offers this audience (e.g., ritual, comfort, focus).
Step 2: Pick two concrete product features that reinforce those benefits.
Step 3: Draft three possible opening lines that lead with benefit, not feature.
Step 4: Choose the strongest opener and write a 60-90 word description that weaves in the features and ends with a call to action.

Show your reasoning for steps 1-3, then give the final description under a `## Final description` heading.

## 3. Few-shot

Write a product description in the same style and format as the examples below.

Example 1:
Product: Linen throw blanket
Description: Some evenings ask to be slowed down. This oversized linen throw — woven from European flax and pre-washed for instant softness — turns the corner of your couch into a place you actually want to stay. Lightweight enough for summer, warm enough for fall. Machine washable, because real life. Drape it, gift it, keep it forever.

Example 2:
Product: Leather card wallet
Description: The wallet that doesn't announce itself. Full-grain Italian leather, six card slots, and a silhouette thin enough to disappear into a front pocket. It ages instead of wearing out — each mark a small record of where you've been. For people who'd rather carry less and mean it. Order yours before the next batch sells out.

Product: Ceramic coffee mug
Description:
```

Keep each of the three sections distinct in approach, and make them good enough that the user would actually paste one of them into Claude and get a better result than they would have from their original.
