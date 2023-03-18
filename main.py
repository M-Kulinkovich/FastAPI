from enum import Enum
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title='trading app'
)

fake_users = [
    {'id': 1, 'role': 'admin', 'name': 'Max'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Dima'},
    {'id': 4, 'role': 'trader', 'name': 'Ignat', 'degree': [
        {'id': 1, 'type_degree': 'expert'}
    ]},
]


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: str
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: List[Degree] = []


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]


fake_trades = [
    {'id': 1, 'user_id': 1, 'currency': 'ETH', 'price': 1500},
    {'id': 2, 'user_id': 2, 'currency': 'BTC', 'price': 25000},
    {'id': 3, 'user_id': 3, 'currency': 'BNB', 'price': 400},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str
    price: float = Field(ge=0)


@app.post('/trades')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return{'status': 200, 'data': fake_trades}
