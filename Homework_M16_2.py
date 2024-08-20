from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get('/')
async def get_main_page():
    return 'Главная страница'


@app.get('/user/admin')
async def get_admin_panel():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def get_id_user(user_id: int = Path(ge=1, le=100, description='Enter your id', example='1')):
    return f'Вы вошли как пользователь №{user_id}'


@app.get('/user/{username}/{age}')
async def get_user_info(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter your name',
                                                      example='UrbanUser')],
                        age: int = Path(ge=18, le=120, description='Enter your age', example=20)):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

