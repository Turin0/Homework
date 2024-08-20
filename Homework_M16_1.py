from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def get_main_page():
    return 'Главная страница'


@app.get('/user/admin')
async def get_admin_panel():
    return 'Вы вошли как администратор'


@app.get('/user/{user_id}')
async def get_id_user(user_id):
    return f'Вы вошли как пользователь №{user_id}'


@app.get('/user')
async def get_user_info(username: str, age: int):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'

