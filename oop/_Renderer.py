class Renderer:
    def __init__(self, data: bytes):
        self.data = data
        ...

    def render(self) -> bytes:
        raise NotImplementedError


class RasterRenderer(Renderer):
    def _pixelize(self) -> bytes:
        ...

    def render(self) -> bytes:
        return self._pixelize()


class VectorRenderer(Renderer):
    def _analyze(self) -> bytes:
        ...

    @staticmethod
    def _scale(data: bytes, coeff: float) -> bytes:
        ...

    def render(self) -> bytes:
        obj = self._analyze()
        obj = self._scale(obj, ...)
        return obj

