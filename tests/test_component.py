"""Tests for the wrapped component: what it imports and how it renders."""

import reflex as rx

from reflex_component_template import ColorPicker, color_picker


def test_imports_the_pinned_library_as_a_named_export():
    imports = color_picker()._get_all_imports()

    assert "react-colorful@5.8.1" in imports
    (lib_import,) = imports["react-colorful@5.8.1"]
    assert lib_import.tag == "HexColorPicker"
    assert not lib_import.is_default


def test_the_color_prop_is_sent_to_react():
    rendered = str(color_picker(color="#ff0000")).replace(" ", "")

    assert 'color:"#ff0000"' in rendered


def test_on_change_passes_the_color_to_the_handler():
    class State(rx.State):
        color: str = "#000000"

        @rx.event
        def set_color(self, color: str):
            self.color = color

    component = color_picker(color=State.color, on_change=State.set_color)

    assert "on_change" in component.get_event_triggers()
    assert "onChange" in str(component)


def test_create_returns_the_component():
    assert isinstance(color_picker(), ColorPicker)
