from controller.home_controller import home
from controller.users_controller import user
from controller.assets_controller import asset
from controller.threats_controller import threat
from controller.risks_controller import risk
from controller.report_controller import report

registerable_controllers = [
    home,
    user,
    asset,
    threat,
    risk,
    report
]