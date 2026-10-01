"""The wrapped component.

This example wraps the HexColorPicker from react-colorful. Replace it with the
React library you want to wrap; the comments mark what each line is for. The
wrapping React guide covers the rest:
https://reflex.dev/docs/wrapping-react/overview/
"""

import reflex as rx


class ColorPicker(rx.Component):
    """A hex color picker."""

    # The npm package to install, pinned to a version.
    library = "react-colorful@5.8.1"

    # The name the package exports the component under. This is a named export
    # (`import { HexColorPicker } from ...`); for a default export, also set
    # `is_default = True`.
    tag = "HexColorPicker"

    # Props. snake_case names are sent to React as camelCase.
    color: rx.Var[str]

    # An event the React component fires. The spec says what reaches the
    # Python handler: here, the picked color as a string.
    on_change: rx.EventHandler[rx.event.passthrough_event_spec(str)]


color_picker = ColorPicker.create
