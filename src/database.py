from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from config import USER_DB, PASS_DB, HOST_DB, NAME_DB, PORT_DB


DATABASE_URL = f'postgresql+asyncpg://{USER_DB}:{PASS_DB}@{HOST_DB}:{PORT_DB}/{NAME_DB}'


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


    