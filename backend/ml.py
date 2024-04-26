def ml_pass(messages: list[dict[str, str]]):
    last_message = messages[-1]
    answer = last_message["message"] + "answer"

    messages.append(
        {
            "role": "model",
            "message": answer,
        }
    )
    return messages, answer
