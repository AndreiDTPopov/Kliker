import flet as ft

def main(page: ft.Page):
    click_52 = 0

    click_52 = ft.Text("Клики: 0", size=30)

    def big_button_click(e):
        nonlocal click_52
        click_count += 1
        click_52.text = f"Калики: {click_count}"
        page.update()


    def reset_counter(e):
        nonlocal click_52
        click_52 = 0
        click_52.text = f"Калики: {click_count}"
        page.update()


    click_button = ft.ElevatedButton("Сюда!", on_click=big_button_click)
    reset_button = ft.ElevatedButton("America goodbye", on_click=reset_counter)


    page.add(click_52, click_button, reset_button)


ft.app(target=main)