"""A small app for trying the component while you develop it."""

import reflex as rx

from reflex_component_template import color_picker


class State(rx.State):
    color: str = "#8b5cf6"

    @rx.event
    def set_color(self, color: str):
        self.color = color


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            color_picker(color=State.color, on_change=State.set_color),
            rx.box(width="200px", height="50px", background_color=State.color),
            rx.text(State.color),
            align="center",
        ),
        height="100vh",
    )


app = rx.App()
app.add_page(index)
