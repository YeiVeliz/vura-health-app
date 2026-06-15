import flet as ft
from views.welcome_view import WelcomeView
from views.login_view import LoginView
from views.register_view import RegisterView
from views.home_view import HomeView
from views.splash_view import SplashView
import time

class Router:
    def __init__(self, page: ft.Page):
        self.page = page
        self.routes = {
            "/welcome": WelcomeView,
            "/login": LoginView,
            "/register": RegisterView,
            "/home": HomeView,
            "/splash": SplashView
        }

    def navigate_to(self, route):
        self.page.views.clear()
        
        view_class = self.routes.get(route, SplashView)
        view = view_class(self.page, self.navigate_to)

        view.opacity = 0
        view.animate_opacity = 500
        
        self.page.views.append(view)
        self.page.update()

        view.opacity = 1
        self.page.update()
