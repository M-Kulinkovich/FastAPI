from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert

from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix='/operations',
    tags=['Operation']
)


@router.get("")
async def get_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        rows = result.fetchall()
        data = [dict(zip(result.keys(), row)) for row in rows]
        return {
            'status': 'success',
            'data': data,
            'details': None
        }
    except Exception:
        raise HTTPException(status_code=500, detail={
            'status': 'error',
            'data': None,
            'details': None
        })


@router.post('')
async def add_operations(new_operations: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operations.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status': 'success'}
