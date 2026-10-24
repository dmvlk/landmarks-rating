from django.http import HttpResponse


def page(title: str, content: str) -> str:
    return f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{title}</title>
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css"
            rel="stylesheet">
        <style>
            body {{ background-color: #f4f4f6; }}
            .navbar-custom {{ background-color: #2b2b36; }}
            .btn-custom {{
                background-color: #6d597a;
                color: white;
                border: none;
            }}
            .btn-custom:hover {{
                background-color: #5a4865;
                color: white;
            }}
            .btn-outline-custom {{
                border-color: #6d597a;
                color: #6d597a;
            }}
            .btn-outline-custom:hover {{
                background-color: #6d597a;
                color: white;
            }}
        </style>
    </head>
    <body>
        <nav
            class="navbar navbar-expand-lg
            navbar-dark navbar-custom mb-4 shadow-sm">
            <div class="container">
                <a class="navbar-brand fw-bold" href="/">
                    Отзывы о городских местах
                </a>
                <div class="navbar-nav">
                    <a class="nav-link" href="/">Главная</a>
                    <a class="nav-link" href="/places/">Места</a>
                    <a class="nav-link" href="/reviews/">Отзывы</a>
                </div>
            </div>
        </nav>
        <main class="container">
            {content}
        </main>
    </body>
    </html>
    """


def index(request):
    content = """
    <div
        class="p-5 mb-4 bg-white rounded-3 shadow-sm border-top border-4"
        style="border-color: #6d597a !important;">
        <h1 class="display-5 fw-bold text-dark">Добро пожаловать!</h1>
        <p class="lead text-muted">
            Здесь вы можете делиться впечатлениями о парках, музеях, ресторанах
            и других интересных местах нашего города.
        </p>
        <hr class="my-4">
        <div class="d-flex gap-3">
            <a href="/places/" class="btn btn-custom btn-lg px-4">
                Посмотреть места
            </a>
            <a href="/reviews/" class="btn btn-outline-custom btn-lg px-4">
                Читать отзывы
            </a>
        </div>
    </div>
    """
    return HttpResponse(page("Главная", content))


def page_not_found(request, exception):
    content = """
    <div class="text-center mt-5">
        <h1 class="display-1 fw-bold" style="color: #6d597a;">404</h1>
        <p class="lead">Такой страницы не существует.</p>
        <a href="/" class="btn btn-custom mt-3">Вернуться на главную</a>
    </div>
    """
    return HttpResponse(page("404 - Не найдено", content), status=404)
