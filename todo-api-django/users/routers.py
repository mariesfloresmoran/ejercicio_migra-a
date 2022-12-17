from rest_framework.routers import Route, SimpleRouter

class CustomRouter(SimpleRouter):
    """Vamos a definir un arreglo de rutas"""
    routes = [
        Route(
          url=r"^{prefix}$",
          mapping={'get': 'get'}, #es la función get porq usan generic viewset
          name="{basename}-list",
          detail = False, #esta ruta no muestra nada
          initkwargs={'suffix': 'List'}
        ),
        Route(
          url=r"^{prefix}/{lookup}$",
          mapping={'get': 'retrieve'}, #es la funcipn retrieve
          name="{basename}-detail",
          detail = True, #esta ruta muestra
          initkwargs={'suffix': 'Detail'}
        )
    ]