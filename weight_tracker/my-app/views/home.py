import flet as ft
from flet import TemplateRoute
import requests


def get_weights(page):
    weights = []
    troute = TemplateRoute(page.route)

    if troute.match("/home/:id"):
        id = troute.id

    url = f"http://127.0.0.1:8000/weights/{id}"

    print(f"Getting weights for user {id}")

    response = requests.get(url)

    if response.status_code == 200:
        for weight in response.json():
            weights.append((weight['created'], weight['weight']))
        print(f'Weights: {weights}')

    return weights


def get_info(page):
    personal_info = {
        'name': '',
        'weight_goal': 0,
        'height': 0,
        'age': 0
    }

    troute = TemplateRoute(page.route)

    if troute.match("/home/:id"):
        id = troute.id

    url = f"http://127.0.0.1:8000/user/{id}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        personal_info['id'] = id
        personal_info['name'] = data['username']
        personal_info['weight_goal'] = data['weight_goal']
        personal_info['height'] = data['height']

    return personal_info


def add_weight(page, id, weight):
    print(f"Adding weight {weight} for user {id}")

    url = "http://127.0.0.1:8000/weight/add/"

    body = {
        "user": id,
        "weight": weight
    }

    response = requests.post(url, data=body)

    if response.status_code == 200:

        print("Weight added")
        page.go(f"/home/{id}")
    else:
        print("Error")


def get_chart_data(weights):
    data_points = [ft.LineChartDataPoint(i, weights[i][1]) for i in range(len(weights))]

    return [ft.LineChartData(
        data_points=data_points,
        color=ft.colors.CYAN,
        curved=True,
        stroke_width=3
    )]


def draw_chart(weight_data, weights):
    return ft.LineChart(
        data_series=get_chart_data(weight_data),
        expand=True,
        min_y=round((int(min(weights)) - 20) / 10) * 10 if len(weights) > 0 else 0,
        max_y=round((int(max(weights)) + 20) / 10) * 10 if len(weights) > 0 else 100,
        min_x=0,
        max_x=len(weights) - 1 if len(weights) > 0 else 10,
        left_axis=ft.ChartAxis(labels_size=50),
        bottom_axis=ft.ChartAxis(labels_size=40, labels_interval=1),
        interactive=True,
    )


def get_dashboard_info(page):
    weight_data = get_weights(page)
    weights = [weight for date, weight in weight_data]
    last_weight = weights[-1] if len(weights) > 0 else 0
    personal_info = get_info(page)
    goal = personal_info['weight_goal'] if personal_info['weight_goal'] else 0
    progress = last_weight - goal if last_weight > goal else goal - last_weight

    return weight_data, weights, last_weight, personal_info, goal, progress


def home_page(page: ft.Page, params, basket):
    icon = 'scale'
    image = ft.Icon(
        scale=ft.Scale(4),
        name=icon,
        animate_scale=ft.Animation(900, "decelerate"),
    )

    weight_data, weights, last_weight, personal_info, goal, progress = get_dashboard_info(page)

    greeting = f"Hi {personal_info['name']}!"
    current_weight = f"Your current weight is {last_weight}kg"
    goal_progress = f"Just {progress}kg to go!"

    new_weight = ft.TextField(width=200, label="Enter weight", keyboard_type=ft.KeyboardType.NUMBER)

    chart_c = WeightChart()

    return ft.View(
        controls=[
            ft.SafeArea(
                minimum=5,
                content=ft.Column(
                    controls=[
                        ft.Row(
                            controls=[
                                ft.IconButton(ft.icons.REFRESH, on_click=chart_c.chart.create_data_points(1,1))
                            ],
                        ),
                        ft.Row(
                            alignment="center",
                            controls=[
                                image
                            ],
                            height=100,
                        ),
                        ft.Divider(height=20, color='transparent'),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Text(
                                    greeting,
                                    size=20,
                                    weight='bold',
                                )
                            ],
                        ),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Text(
                                    current_weight,
                                    size=16,
                                    weight='bold',
                                )
                            ],
                        ),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Text(
                                    goal_progress,
                                    size=16,
                                    weight='bold',
                                )
                            ],
                        ),
                        ft.Divider(height=20, color='transparent'),
                        ft.Row(
                            alignment="center",
                            controls=[
                                new_weight,
                                ft.FloatingActionButton(
                                    icon=ft.icons.ADD,
                                    on_click=lambda e: add_weight(page, personal_info['id'], new_weight.value),
                                ),
                            ]

                        ),
                        ft.Divider(height=40, color='transparent'),
                        ft.Row(
                            alignment="center",
                            controls=[
                                ft.Text("Your weight history:")
                            ]
                        ),
                        ft.Row(
                            alignment="center",
                            controls=[
                                chart_c.chart
                            ]
                        )

                    ]
                )
            )
        ]
    )
