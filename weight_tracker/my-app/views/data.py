import flet as ft
from flet import TemplateRoute
import requests

from components.appbar import get_app_bar
from components.navbar import NavBar

table_style = {
    "columns": [
        ft.DataColumn(ft.Text("Date", weight=ft.FontWeight.BOLD)),
        ft.DataColumn(ft.Text("Weight", weight=ft.FontWeight.BOLD), numeric=True),
        ft.DataColumn(ft.Text("Delete", weight=ft.FontWeight.BOLD)),
    ],
    "heading_row_height": 40,
    "width": 500,
    "column_spacing": 100
}


class DataTable(ft.DataTable):
    def __init__(self, user_id):
        self.user_id = user_id
        super().__init__(**table_style)

        self.weights = []

        self.show_checkbox_column = True

        self.get_data()
        self.format_data()
        self.create_table()

    def get_data(self):
        weights = []
        url = f"http://127.0.0.1:8000/weights/{self.user_id}"

        response = requests.get(url)

        if response.status_code == 200:
            for weight in response.json():
                weights.append((weight['id'], weight['created'], weight['weight']))

        self.weights = weights

    def format_data(self):
        new_data = []
        for index, date, weight in self.weights:
            new_date = date.split('T')[0]
            new_data.append((index, new_date, weight))

        self.weights = new_data

    def create_table(self):
        for index, date, weight in self.weights:
            row = ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(date)),
                    ft.DataCell(ft.Text(weight)),
                    ft.DataCell(ft.IconButton(icon=ft.icons.DELETE, data=index, on_click=lambda e: self.delete_weight(e.control.data)))
                ]
            )

            self.rows.append(row)

    def delete_weight(self, weight_id):
        url = f"http://127.0.0.1:8000/weight/{weight_id}/delete/"

        response = requests.delete(url)


def data_page(page: ft.Page, params, basket):
    user_id = params.user_id
    navbar = NavBar(page, user_id).get_navbar()
    navbar.selected_index = 1

    data_table = DataTable(user_id)

    column = ft.Column(
        expand=True,
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(f"Your past weight-ins", size=16, text_align=ft.TextAlign.CENTER)
                ]
            ),
            ft.Column(
                expand=True,
                scroll=ft.ScrollMode.HIDDEN,
                controls=[
                    ft.Container(
                        content=data_table
                    )
                ]

            )

        ]
    )

    return ft.View(
        controls=[
            column,
            get_app_bar(page),
            navbar
        ]
    )
