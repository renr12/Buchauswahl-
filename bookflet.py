import flet as ft
import threading
import requests
from backend import start_backend

threading.Thread(target=start_backend, daemon=True).start()

index = 0

def main(page: ft.Page):
    page.title = "Book Viewer"
    page.bgcolor = "white"

    header = ft.Text("Buchauswahl", size=24, weight="bold", color="blue")

    icon = ft.Icon("menu_book", size=80, color="blue")

    title = ft.Text("", size=24, weight="bold", color="black")
    info = ft.Text("", size=14, color="black")

    back = ft.IconButton(icon="arrow_back")
    next = ft.ElevatedButton("Weiter")

    def load_book(i):
        global index
        r = requests.get("http://localhost:5000/books/" + str(i))
        if r.status_code == 200:
            b = r.json()
            index = i
            title.value = b["title"]
            info.value = b["author"] + " • " + str(b["year"])
            back.disabled = index == 0
            next.disabled = False
        else:
            next.disabled = True
        page.update()

    def back_click(e):
        load_book(index - 1)

    def next_click(e):
        load_book(index + 1)

    back.on_click = back_click
    next.on_click = next_click

    page.add(
        ft.Column(
            [
                header,
                ft.Container(height=20),
                ft.Container(
                    ft.Row(
                        [
                            back,
                            ft.Row(
                                [
                                    icon,
                                    ft.Column([title, info])
                                ],
                                spacing=20
                            ),
                            next
                        ],
                        alignment="spaceBetween"
                    ),
                    padding=20,
                    bgcolor="#EBEDFF",
                    border_radius=10,
                    width=650
                )
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True
        )
    )

    load_book(0)

ft.app(target=main, view=ft.WEB_BROWSER, port=8550)
