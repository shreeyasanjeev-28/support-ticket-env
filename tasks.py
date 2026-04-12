from grader import grade_easy, grade_medium, grade_hard

tasks = [
    {
        "id": "easy",
        "input": "Where is my order?",
        "grader": grade_easy
    },
    {
        "id": "medium",
        "input": "I received a damaged product",
        "grader": grade_medium
    },
    {
        "id": "hard",
        "input": "I was charged twice for my order",
        "grader": grade_hard
    }
]
