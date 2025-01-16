# Import required modules and components
from omagent_core.utils.container import container
from omagent_core.engine.workflow.conductor_workflow import ConductorWorkflow
from omagent_core.engine.workflow.task.simple_task import simple_task
from pathlib import Path
from omagent_core.utils.registry import registry
from omagent_core.clients.devices.cli.client import DefaultClient
from omagent_core.engine.workflow.task.set_variable_task import SetVariableTask
from omagent_core.utils.logger import logging
from omagent_core.engine.workflow.task.do_while_task import DoWhileTask

from agent.input_interface.input_interface import InputInterfaceGot
# from omagent_core.advanced_components.workflow.dnc.workflow import DnCWorkflow
from omagent_core.advanced_components.workflow.general_got.workflow import GoTWorkflow



import os
os.environ['custom_openai_endpoint'] = 'http://121.52.244.250:3000/v1'
os.environ['custom_openai_key'] = 'sk-iytCHBhtNvAhtxeBC8E5A71e473c45C1B9847b6bB2F6461b'
os.environ['bing_api_key'] = '573bfabb7359487b90b8f8d26a4f6fc5'
os.environ['custom_openai_text_encoder_key'] = 'sk-2fpMc0GBGTGG96w62cF7B9621bA34aDa8b2112D26404Ae4e'

# Initialize logging
logging.init_logger("omagent", "omagent", level="INFO")

# Set current working directory path
CURRENT_PATH = Path(__file__).parents[0]

# Import registered modules
registry.import_module(project_path=CURRENT_PATH.joinpath('agent'))

container.register_stm("RedisSTM")
# Load container configuration from YAML file
container.from_config(CURRENT_PATH.joinpath('container.yaml'))



# Initialize Got workflow
workflow = ConductorWorkflow(name='GoT')

# Configure workflow tasks:
client_input_task = simple_task(task_def_name=InputInterfaceGot, task_reference_name='input_task')

got_workflow = GoTWorkflow()
got_workflow.set_input(query=client_input_task.output('query'), task=client_input_task.output('task'), meta=client_input_task.output('meta'))
workflow >> client_input_task >> got_workflow

# Register workflow
workflow.register(True)

# Initialize and start CLI client with workflow configuration
config_path = CURRENT_PATH.joinpath('configs')
cli_client = DefaultClient(interactor=workflow, config_path=config_path, workers=[InputInterfaceGot()])
cli_client.start_interactor()
