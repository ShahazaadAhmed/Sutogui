from pywinauto import Desktop


class WindowManager:

    def __init__(self, backend="uia"):
        self.desktop = Desktop(backend=backend)

    def find_window(self, title=None, title_re=None):
        if title_re:
            return self.desktop.window(
                title_re=title_re
            )

        if title:
            return self.desktop.window(
                title=title
            )

        raise ValueError(
            "Either title or title_re must be provided."
        )

    def wait_for_window(
        self,
        title=None,
        title_re=None,
        timeout=10
    ):
        window = self.find_window(
            title=title,
            title_re=title_re
        )

        window.wait(
            "visible",
            timeout=timeout
        )

        return window

    def find_control(
        self,
        window,
        control_type=None,
        title=None,
        title_re=None
    ):
        criteria = {}

        if control_type:
            criteria["control_type"] = control_type

        if title:
            criteria["title"] = title

        if title_re:
            criteria["title_re"] = title_re

        return window.child_window(**criteria)

    def wait_for_control(
        self,
        window,
        timeout=10,
        **criteria
    ):
        control = self.find_control(
            window,
            **criteria
        )

        control.wait(
            "ready",
            timeout=timeout
        )

        return control