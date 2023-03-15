from controller.home_controller import home
from controller.users_controller import user
from controller.assets_controller import asset
from controller.threats_controller import threat

registerable_controllers = [
    home,
    user,
    asset,
    threat,
]