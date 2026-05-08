from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_warehouse_db_launch


def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("rover_jorge_martin", package_name="rover_jorge_martin_moveit_config").to_moveit_configs()
    return generate_warehouse_db_launch(moveit_config)
