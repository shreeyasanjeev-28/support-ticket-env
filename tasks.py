from grader import grade_easy, grade_medium, grade_hard

tasks = [
    {
        "type": "easy",
        "ticket": "Where is my order?",
        "grader": grade_easy
    },
    {
        "type": "medium",
        "ticket": "I received a damaged product",
        "grader": grade_medium
    },
    {
        "type": "hard",
        "ticket": "I was charged twice for my order",
        "grader": grade_hard
    }
]
