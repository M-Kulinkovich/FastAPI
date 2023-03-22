from httpx import AsyncClient


async def test_add_operations(ac: AsyncClient):
    response = await ac.post('/operations', json={
        'id': 1,
        'quantity': '26.5',
        'figi': 'figi',
        'instrument_type': 'bond',
        'data': '2023-03-21T16:24:06.702',
        'type': 'Paying coupons'
    })

    assert response.status_code == 200


async def test_get_operations(ac: AsyncClient):
    response = await ac.get('/operations', params={
        'operation_type': 'Paying coupons',
    })

    assert response.status_code == 200
    assert response.json()['status'] == 'success'
    assert len(response.json()['data']) == 1
