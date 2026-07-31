# MMLU-Redux Logprob

This variant evaluates MMLU-Redux with the same multiple-choice log-likelihood
protocol as the standard MMLU task. For each question, the harness scores the
continuations `A`, `B`, `C`, and `D`, selects the highest-log-likelihood letter,
and compares its index with the dataset's numeric `answer` field.

Run the full benchmark with:

```bash
lm_eval --model hf --model_args pretrained=<model> --tasks mmlu_redux
```

Following the standard MMLU naming convention, the log-likelihood task is the
unsuffixed default. The existing `mmlu_redux_generative` task remains unchanged
and evaluates generated letter responses with exact match instead.