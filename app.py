import asyncio
from contextlib import suppress

import flet as ft

async def main(page: ft.Page):
    page.title = "Kroha Clicker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#141221"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "fonts/FulboArgenta.ttf"}
    page.theme = ft.Theme(font_family="FulboArgenta")

    async def score_up(event: ft.ContainerTapEvent):
        score.data += 1
        score.value = str(score.data)

        image.scale = 0.95

        score_counter.opacity = 1
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.left = tap_position[0]
        score_counter.top = tap_position[1]
        score_counter.bottom = 0

        progress_bar.value += (1/100)

        if score.data % 100 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value = "👶🏼 +100",
                    size=20,
                    color="#76b7eb", #76b7eb
                    text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#25223a" #3772a1
            )
            page.snack_bar.open = True
            progress_bar.value = 0.5

        await page.update_async()

        # with suppress(AttributeError):
        #     await audio.play_async()

        await asyncio.sleep(0.5)
        image.scale = 1
        score_counter.opacity = 0

        await page.update_async()
        page.overlay.clear()

    def on_tap_down(event: ft.ContainerTapEvent):
        global tap_position
        tap_position = (event.local_x, event.local_y)


    score = ft.Text(value="0", size=100, data=0)
    score_counter = ft.Text(
        size=50, animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.BOUNCE_IN)
    )
    image = ft.Image(
        src="kroha.png",
        fit=ft.ImageFit.CONTAIN,
        animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE)
    )
    progress_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#76b7eb", #76b7eb
        bgcolor="#2578ba" #2578ba
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            on_tap_down=on_tap_down,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progress_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)

        )
    )

if __name__ == "__main__":
    tap_position = (0, 0)
    ft.app(target=main, view=ft.WEB_BROWSER, port=8080)