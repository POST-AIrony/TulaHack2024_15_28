from llama_cpp import Llama
from constant import (
    SYSTEM_PROMPT_FOR_HISTORIES,
    SYSTEM_PROMPT_FOR_MANAGER,
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
    tokens.extend(get_message_tokens(model, **system_message))
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
    model: Any,
    messages: List[Dict[str, str]],
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
    tokens = []
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
        # yield model.detokenize([token]).decode("utf-8", errors="ignore")

    return token_str


def interact_manager(
    model: Any,
    conversation: str,
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
    tokens = []
    system_message = {"role": "system", "content": SYSTEM_PROMPT_FOR_MANAGER}
    tokens.extend(get_message_tokens(model, **system_message))
    # Получение токенов пользовательского сообщения
    message_tokens = get_message_tokens(model=model, role="user", content=conversation)
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

    # Инициализация модели
    model = Llama(
        model_path=MODEL_PATH,
        n_gpu_layers=-1,
        n_batch=512,
        n_ctx=4096,
        n_parts=1,
    )

    # resp = interact_history(
    #     model,
    #     [
    #         {
    #             "role": "user",
    #             "message": "Начальное место истории: Кафе под названием 'Дивный сад'.",
    #         }
    #     ],
    # )
    # for response in resp:
    #     print(response, end="")
        
    
    resp = interact_manager(
        model,"""клиент: здравствуйте я хотел бы заказать букет к дню рождения
сотрудник: здравствуйте конечно с удовольствием помогу вам с выбором есть ли предпочтения по цветам или стилю
клиент: я смотрю у вас на сайте есть раздел с популярными букетами можете рассказать о них
сотрудник: конечно у нас есть букет нежность в нем розы и лилии также популярен букет солнечный день с герберами и тюльпанами
клиент: а какая свежесть у этих цветов сколько они продержатся
сотрудник: все наши цветы поступают утром от местных поставщиков и продержатся свежими семь десять дней и правильном уходе
клиент: отлично
клиент: а можно добавить в букет солнечный день несколько ирисов
сотрудник: конечно можно мы можем модифицировать любой букет по вашему желанию
клиент: хорошо тогда добавьте пожалуйста ирисы и сколько это будет стоить
сотрудник: с добавлением ирисов букет будет стоить три тысячи пятьсот рублей
клиент: прекрасно а когда вы сможете его доставить
сотрудник: мы можем организовать доставку уже завтра в удобное для вас время
клиент: давайте тогда завтра в четырнадцать часов я пришлю адрес в заказ
сотрудник: отлично укажите пожалуйста в номер телефона и полный адрес доставки
сотрудник: и укажите про ирисы я предупрежу флориста
сотрудник: завтра в два ваш букет будет доставлен
клиент: спасибо большое за помощь
сотрудник: не за что всегда рады помочь если у вас возникнут дополнительные вопросы пишите или звоните нам удачного дня
клиент: до свидания
""")
    for response in resp:
        print(response, end="")
