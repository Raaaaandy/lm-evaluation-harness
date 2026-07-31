def _sort_choices_by_length(doc, *, reverse):
    choices = doc["choices"]
    answer = int(doc["answer"])
    indexed_choices = list(enumerate(choices))
    indexed_choices.sort(key=lambda item: len(item[1]), reverse=reverse)

    return {
        **doc,
        "choices": [choice for _, choice in indexed_choices],
        "answer": next(
            new_index
            for new_index, (old_index, _) in enumerate(indexed_choices)
            if old_index == answer
        ),
    }


def process_docs_ascending(dataset):
    return dataset.map(
        lambda doc: _sort_choices_by_length(doc, reverse=False),
        desc="Sorting MMLU choices by ascending length",
    )


def process_docs_descending(dataset):
    return dataset.map(
        lambda doc: _sort_choices_by_length(doc, reverse=True),
        desc="Sorting MMLU choices by descending length",
    )