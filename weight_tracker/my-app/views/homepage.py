import flet as ft
from flet import TemplateRoute
from logging import getLogger
import requests

from components.appbar import get_app_bar
from components.navbar import NavBar

logger = getLogger(__name__)


class PersonalInfo:
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id
        self.name = None
        self.weight_goal = None
        self.height = None
        self.age = None
        self.passcode = None
        self.weights = []

        self.get_info()
        self.get_weights()

    def get_info(self):
        url = f"http://127.0.0.1:8000/user/{self.user_id}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            self.name = data['username']
            self.weight_goal = data['weight_goal']
            self.height = data['height']
            self.age = data['age']
            self.passcode = data['password']

    def get_weights(self):
        url = f"http://127.0.0.1:8000/weights/{self.user_id}"

        response = requests.get(url)

        if response.status_code == 200:
            for weight in response.json():
                self.weights.append(weight['weight'])

    def update_user(self):
        url = f"http://127.0.0.1:8000/user/{self.user_id}/update/"

        body = {
            "username": self.name,
            "password": self.passcode,
            "weight_goal": self.weight_goal,
            "height": self.height,
            "age": self.age
        }

        response = requests.put(url, json=body)

        if response.status_code == 200:
            print("User updated successfully")
        else:
            print("User update failed")


dashboard_style: dict = {
    "main": {
        "expand": True,
        # "bgcolor": "white",
        "border_radius": 10,
    },
}

base_chart_style: dict = {
    "expand": True,
    "left_axis": ft.ChartAxis(labels_size=50),
    "bottom_axis": ft.ChartAxis(labels_size=40, labels_interval=1),

}


class BaseChart(ft.LineChart):
    def __init__(self, user_id):
        super().__init__(**base_chart_style)

        self.user = PersonalInfo(user_id)

        self.points: list = []

        self.line = ft.LineChartData(
            curved=True,
            stroke_cap_round=True,
            stroke_width=2,
        )

        self.initial_data_points()

        self.line.data_points = self.points
        self.data_series = [self.line]

    def create_data_points(self, x, y):
        self.points.append(
            ft.LineChartDataPoint(x, y))

    def initial_data_points(self):
        for x, y in enumerate(self.user.weights):
            self.create_data_points(x, y)


graph_style: dict = {
    "expand": 1,
    "border_radius": 10,
    "padding": 30
}


class Graph(ft.Container):
    def __init__(self, user_id) -> None:
        super().__init__(**graph_style)
        self.chart = BaseChart(user_id)
        self.content = self.chart


class Dashboard(ft.Container):
    def __init__(self, graph: object, user_id) -> None:
        super().__init__(**dashboard_style.get("main"))
        self.graph: object = graph
        self.user = PersonalInfo(user_id)

        self.current_weight = self.user.weights[-1] if self.user.weights else None
        if self.current_weight:
            self.progress = self.current_weight - self.user.weight_goal if self.current_weight > self.user.weight_goal else self.user.weight_goal - self.current_weight

            if self.progress == 0:
                self.progress_display = ft.Text(
                    f"Congratulations! You have reached your goal!", size=16, weight="bold")
            else:
                print(f"Progress: {self.progress}, Goal: {self.user.weight_goal}")
                self.progress_display = ft.Text(
                f"Only {self.progress}kg to go!", size=16, weight="bold")
        else:
            self.progress_display = ft.Text("We'll start tracking your progress once you are ready!", size=16, weight="bold")

        self.curr_weight_display = ft.Text(
            f"Your current weight is {self.current_weight} kg",
            size=16,
            weight="bold") if self.current_weight else ft.Text(
            f"Please enter your first weight!", size=16, weight="bold")



        self.input = ft.TextField(width=200, label="Enter weight", keyboard_type=ft.KeyboardType.NUMBER)
        self.add_weight_button = ft.FloatingActionButton(
            icon=ft.icons.ADD,
            on_click=lambda e: self.update_weigh(),
        )

        self.content = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(
                            scale=ft.Scale(4),
                            name='scale',
                            animate_scale=ft.Animation(900, "decelerate"),
                        )
                    ]
                ),
                ft.Divider(height=40, color="transparent"),
                ft.Text(f"Hi {self.user.name}!", size=20, weight="bold"),
                self.curr_weight_display,
                self.progress_display,
                ft.Divider(height=15, color="transparent"),
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        self.input,
                        self.add_weight_button
                    ]
                )
            ]
        )

    def update_weigh(self) -> None:
        if self.input.value != "":
            self.display_weight_update()
            self.add_weight_to_db()

            self.graph.chart.create_data_points(
                len(self.graph.chart.points), self.current_weight)

            self.graph.chart.update()

    def display_weight_update(self):
        self.current_weight = float(self.input.value)
        self.progress = self.current_weight - self.user.weight_goal if self.current_weight > self.user.weight_goal else self.user.weight_goal - self.current_weight

        self.curr_weight_display.value = f"Your current weight is {self.current_weight} kg"
        self.curr_weight_display.update()

        if self.progress == 0 or self.progress == 0.0:
            self.progress_display.value = f"Congratulations! You have reached your goal!"
        else:
            self.progress_display.value = f"Only {self.progress}kg to go!"

        self.progress_display.update()

        self.input.value = ""
        self.input.update()

    def add_weight_to_db(self):
        weight = self.current_weight
        logger.info(f"Adding weight {weight} for user {self.user.user_id}")

        url = "http://127.0.0.1:8000/weight/add/"

        body = {
            "user": self.user.user_id,
            "weight": weight
        }

        response = requests.post(url, data=body)

        if response.status_code == 200:
            logger.info("Weight added")
        else:
            logger.error("Error")


def homepage(page: ft.Page, params, basket):
    user_id = params.user_id

    graph: ft.Container = Graph(user_id)
    dashboard: ft.Container = Dashboard(graph, user_id)

    navbar = NavBar(page, user_id).get_navbar()

    column = ft.Column(
        expand=True,
        controls=[
            dashboard,
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(f"Your weight progress", size=16, text_align=ft.TextAlign.CENTER),
                ]
            ),
            graph,
        ]
    )

    return ft.View(
        controls=[
            column,
            get_app_bar(page),
            navbar
        ],
    )

