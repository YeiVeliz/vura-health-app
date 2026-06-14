import flet as ft
from views.welcome_view import WelcomeView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.home_view import HomeView

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            "/": WelcomeView,
            "/login": LoginView,
            "/register": RegisterView,
            "/home": HomeView,
        }

    def navigate_to(self, route):
        self.page.views.clear()
        
        view_class = self.routes.get(route, WelcomeView)
        
        view = view_class(self.page, self.navigate_to)
        
        self.page.views.append(view)
        self.page.update()