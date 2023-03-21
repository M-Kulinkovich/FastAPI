from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)


@router.get('/')
async def get_operations(operations_type: str, session: AsyncSession = Depends(get_async_session)):
    query = select(operation).where(operation.c.type == operations_type)
    result = await session.execute(query)
    return result.all()


@router.post('/')
async def add_operations(new_operations: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operations.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'Success'}
