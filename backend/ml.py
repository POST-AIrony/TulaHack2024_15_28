from llama_cpp import Llama
from constant import (
    SYSTEM_PROMPT_FOR_HISTORIES,
    BOT_TOKEN,
    LINEBREAK_TOKEN,
    ROLE_TOKENS,
    MODEL_PATH,
)
from typing import List, Any, Dict


def get_message_tokens(model: Any, role: str, content: str) -> List[int]:
    """
    Создает токены для сообщения с учетом роли и содержания.

    Параметры:
    - model (Any): Модель токенизатора.
    - role (str): Роль сообщения.
    - content (str): Содержание сообщения.

    Возвращает:
    List[int]: Список токенов сообщения.

    Пример использования:
    ```python
    model = SomeTokenizer()
    role = "user"
    content = "Hello, world!"
    message_tokens = get_message_tokens(model, role, content)
    ```

    Подробности:
    - Функция токенизирует содержание сообщения с учетом роли и вставляет соответствующие токены.
    - В конце сообщения добавляется токен окончания строки.
    """
    message_tokens = model.tokenize(content.encode("utf-8"))
    message_tokens.insert(1, ROLE_TOKENS[role])
    message_tokens.insert(2, LINEBREAK_TOKEN)
    message_tokens.append(model.token_eos())
    return message_tokens


def convert_to_tokens(messages: List[Dict[str, str]], model: Any) -> List[int]:
    """
    Преобразует список сообщений в токены.

    Параметры:
    - messages (List[Dict[str, str]]): Список сообщений в формате JSON.
    - model (Any): Модель токенизатора.

    Возвращает:
    List[int]: Список токенов всех сообщений.
    """
    tokens = []
    system_message = {"role": "system", "content": SYSTEM_PROMPT_FOR_HISTORIES}
    tokens.extend(get_message_tokens(model, **system_message))
    for message in messages:
        role = message["role"]
        content = message["message"]
        message_tokens = get_message_tokens(model, role, content)
        tokens.extend(message_tokens)
    return tokens


def get_system_tokens(model: Any) -> List[int]:
    """
    Создает токены для системного сообщения.

    Параметры:
    - model (Any): Модель токенизатора.

    Возвращает:
    List[int]: Список токенов системного сообщения.

    Пример использования:
    ```python
    model = SomeTokenizer()
    system_tokens = get_system_tokens(model)
    ```

    Подробности:
    - Функция создает токены для системного сообщения, добавляя соответствующие маркеры.
    """
    system_message = {"role": "system", "content": SYSTEM_PROMPT_FOR_HISTORIES}
    return get_message_tokens(model, **system_message)


def interact_history(
    model_path: str,
    messages: List[Dict[str, str]],
    n_ctx: int = 4096,
    top_k: int = 30,
    top_p: float = 0.9,
    temperature: float = 0.2,
    repeat_penalty: float = 1.1,
):
    """
    Взаимодействие с моделью на основе LLAMA для генерации ответов на пользовательские запросы.

    Параметры:
    - model_path (str): Путь к предварительно обученной модели LLAMA.
    - user_prompt (str): Пользовательский запрос для генерации ответа.
    - n_ctx (int): Максимальная длина контекста.
    - top_k (int): Количество наиболее вероятных токенов для рассмотрения в генерации.
    - top_p (float): Порог отсечения для выбора токенов в генерации на основе вероятностей.
    - temperature (float): Параметр температуры для разнообразия в генерации.
    - repeat_penalty (float): Штраф за повторение токенов в генерации.

    Возвращает:
    str: Сгенерированный ответ на основе пользовательского запроса.

    Пример использования:
    ```python
    model_path = "path/to/model"
    user_prompt = "Привет, как дела?"
    response = interact(model_path, user_prompt)
    ```

    Подробности:
    - Функция использует модель LLAMA для генерации ответов на пользовательские запросы.
    - Задает параметры генерации, такие как ограничения токенов, температура и штраф за повторения.
    - Генерирует ответ на основе пользовательского запроса и возвращает его в виде строки.
    """
    # Инициализация модели
    model = Llama(
        model_path=model_path,
        n_gpu_layers=-1,
        n_batch=512,
        n_ctx=n_ctx,
        n_parts=1,
    )

    # Получение токенов системного сообщения
    system_tokens = get_system_tokens(model)
    tokens = system_tokens
    model.eval(tokens)

    # Получение токенов пользовательского сообщения
    message_tokens = convert_to_tokens(messages=messages, model=model)
    token_str = ""
    role_tokens = [model.token_bos(), BOT_TOKEN, LINEBREAK_TOKEN]
    tokens += message_tokens + role_tokens

    # Генерация ответа на основе токенов
    generator = model.generate(
        tokens,
        top_k=top_k,
        top_p=top_p,
        temp=temperature,
        repeat_penalty=repeat_penalty,
    )

    # Преобразование токенов в строку
    for token in generator:
        token_str += model.detokenize([token]).decode("utf-8", errors="ignore")
        tokens.append(token)
        
        if token == model.token_eos():
            break
        yield model.detokenize([token]).decode("utf-8", errors="ignore")

    # return token_str


if __name__ == "__main__":
    resp = interact_history(
            MODEL_PATH,
            [
                {
                    "role": "user",
                    "message": "Начальное место истории: Кафе под названием 'alleleo na hue'.",
                }
            ],
        )
    for response in resp:
        print(response, end="")
