
def get_subtopic_prompt(main_topic, num):
    text = f"""
    Using '{main_topic}' as main topic, give me a list of {num} possible subtopics related.
    They must be in order of relevance.
    Your response should be a JSON array of strings.
    """

    return text