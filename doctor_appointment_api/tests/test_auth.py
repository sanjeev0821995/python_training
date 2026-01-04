import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        res = await ac.post("/auth/register", json={
            "email":"test@test.com","password":"123456","role":"patient","name":"Test User"
        })
        assert res.status_code in (200, 400)
