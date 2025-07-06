# Notion и AI — Telegram Web3 Бот и Одностраничный сайт

## Описание

Это приложение для Telegram-группы "Notion и AI". Оно включает:
- Telegram-бота (администратор группы)
- Одностраничный сайт-меню с красивыми ссылками на чаты и ресурсы

## Запуск

### 1. Клонируйте репозиторий и перейдите в папку
```
cd ~/Downloads/Notion\ and\ AI/notion-ai-web3-bot
```

### 2. Активируйте виртуальное окружение
```
source venv/bin/activate
```

### 3. Установите зависимости (если не установлены)
```
pip install -r requirements.txt
```

### 4. Укажите токен Telegram-бота
В файле `.env` или через переменную окружения:
```
export TELEGRAM_TOKEN=ваш_токен_бота
```

### 5. Запустите Telegram-бота
```
python bot.py
```

### 6. Запустите сайт
```
uvicorn main:app --reload
```

Сайт будет доступен по адресу: http://127.0.0.1:8000/

---

## Структура
- `bot.py` — Telegram-бот
- `main.py` — FastAPI сервер для сайта
- `templates/index.html` — HTML шаблон сайта
- `static/style.css` — стили сайта

## Запуск через Docker

1. Соберите образ:
   ```bash
   docker build -t notion-ai-web3-bot .
   ```
2. Запустите контейнер:
   ```bash
   docker run -d -p 8000:8000 --env TELEGRAM_TOKEN=8129671831:AAHrBUIwhcymD-racDu9RIYx5S_XQ05VLcw notion-ai-web3-bot
   ```

## Публикация на GitHub

1. Инициализируйте git-репозиторий (если ещё не инициализирован):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Notion & AI web and bot"
   ```
2. Создайте репозиторий на GitHub и следуйте инструкциям для push:
   ```bash
   git remote add origin https://github.com/shy3ony/notionandai.git
   git branch -M main
   git push -u origin main
   ```

3. Переименуйте ветку в main (если ещё не сделали):
   ```bash
   git branch -M main
   ```

4. Добавьте или обновите remote origin:
   Если уже есть origin, обновите его:
   ```bash
   git remote set-url origin https://github.com/shy3ony/notionandai.git
   ```
   Если нет — добавьте:
   ```bash
   git remote add origin https://github.com/shy3ony/notionandai.git
   ```

5. Отправьте файлы на GitHub:
   ```bash
   git push -u origin main
   ```

## После этого

- На GitHub в репозитории **notionandai** должны появиться все ваши файлы из папки `notion-ai-web3-bot`.
- Теперь вы сможете импортировать этот репозиторий на Vercel.

---

**Если появятся ошибки при пуше — скопируйте их сюда, я помогу разобраться!**  
Если всё получилось — переходите к деплою на Vercel. # notionandai
