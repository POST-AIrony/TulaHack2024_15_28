SYSTEM_PROMPT_FOR_HISTORIES = "Ты — Сайга, русскоязычный автоматический ассистент, генерирующий интерактивные текстовые истории. Твоя задача — описать текущую ситуацию и предложить несколько вариантов действий для пользователя. Предлагай от 3 до 5 вариантов развития событий, исходя из запроса пользователя."

MODEL_PATH = "model-q8_0.gguf"

SYSTEM_TOKEN = 1587
USER_TOKEN = 2188
BOT_TOKEN = 12435
LINEBREAK_TOKEN = 13

ROLE_TOKENS = {
    "user": USER_TOKEN,
    "bot": BOT_TOKEN,
    "system": SYSTEM_TOKEN
}