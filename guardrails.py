"""
Conversation-aware guardrails for the Shopping Assistant.
"""


SHOPPING_KEYWORDS = {
    "buy",
    "purchase",
    "order",
    "shopping",
    "shop",
    "product",
    "products",
    "item",
    "items",
    "price",
    "cost",
    "cheap",
    "expensive",
    "organic",
    "rating",
    "review",
    "reviews",
    "honey",
    "oil",
    "tea",
    "coffee",
    "nuts",
    "almonds",
    "granola",
    "oats",
    "rice",
    "history",
    "orders",
    "summary",
    "spent",
    "delivery",
    "reorder",
}

FOLLOW_UP_WORDS = {
    "yes",
    "no",
    "sure",
    "ok",
    "okay",
    "go ahead",
    "please",
    "1",
    "2",
    "3",
    "first",
    "second",
    "third",
    "that one",
    "this one",
    "buy it",
    "order it",
    "compare them",
    "compare",
    "which one",
    "which is better",
    "tell me more",
    "show more",
}


def is_shopping_related(text: str) -> bool:
    """
    Returns True if the message contains shopping-related keywords.
    """
    text = text.lower()

    return any(keyword in text for keyword in SHOPPING_KEYWORDS)


def should_run_agent(messages: list[dict]) -> bool:
    """
    Allow:
    - Shopping requests
    - Follow-up confirmations
    - Follow-up questions after product recommendations
    """

    latest = messages[-1]["content"].lower().strip()

    # New shopping request
    if is_shopping_related(latest):
        return True

    # No previous conversation
    if len(messages) < 2:
        return False

    previous_assistant = ""

    # Find the most recent assistant message
    for msg in reversed(messages[:-1]):
        if msg["role"] == "assistant":
            previous_assistant = msg["content"].lower()
            break

    confirmation_words = {
        "yes",
        "no",
        "1",
        "2",
        "3",
        "4",
        "5",
        "first",
        "second",
        "third",
        "that one",
        "this one",
        "go ahead",
        "buy it",
        "order it",
    }

    if latest in confirmation_words:

        ordering_context = [
            "would you like to order",
            "just say yes",
            "give me the number",
            "let me know which one",
            "which one you'd like",
            "id:",
        ]

        if any(text in previous_assistant for text in ordering_context):
            return True

    return False