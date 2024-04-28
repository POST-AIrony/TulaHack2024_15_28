from case15 import case15
from case28 import case28
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise


async def init():
    """
    Инициализирует подключение к базе данных и генерирует схемы.

    Returns:
    - None
    """
    await Tortoise.init(
        db_url="sqlite://db.sqlite3",  # Подставьте путь к файлу SQLite
        modules={
            "models": ["models.models"]
        },  # Подставьте имя модуля, где определены ваши модели
    )
    await Tortoise.generate_schemas()


async def lifespan(app: FastAPI):
    """
    Функция жизненного цикла FastAPI.

    Parameters:
    - app (FastAPI): Экземпляр FastAPI приложения.

    Yields:
    - None
    """
    await init()

    yield


app = FastAPI(title="TulaHack", lifespan=lifespan)

app.include_router(case15, tags=["case15"])
app.include_router(case28, tags=["case28"])


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# if __name__ == "__main__":
#     uvicorn.run(app)