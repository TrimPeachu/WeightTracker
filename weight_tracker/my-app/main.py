import flet as ft
from flet_route import Routing, path

from views.login import login_page
from views.register import register_page
# from views.home import home_page
from views.homepage import homepage
from views.data import data_page
from views.profile import profile_page


def main(page: ft.Page):

    app_routes = [
        path(url="/", view=login_page, clear=True),
        path(url="/login", view=login_page, clear=True),
        path(url="/register", view=register_page, clear=True),
        path(url="/home/:user_id", view=homepage, clear=True),
        path(url="/data/:user_id", view=data_page, clear=True),
        path(url="/profile/:user_id", view=profile_page, clear=True)
    ]

    Routing(page=page, app_routes=app_routes)

    page.go(page.route)

    page.update()


ft.app(target=main)
