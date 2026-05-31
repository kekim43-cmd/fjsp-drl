from gym.envs.registration import register

# Registrar for the gym environment
# https://www.gymlibrary.ml/content/environment_creation/ for reference
try:
    register(
        id='fjsp-v0',  # Environment name (including version number)
        entry_point='env.fjsp_env:FJSPEnv',
        order_enforce=False,
        disable_env_checker=True,
    )
except TypeError:
    register(
        id='fjsp-v0',
        entry_point='env.fjsp_env:FJSPEnv',
    )
