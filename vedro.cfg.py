import vedro
import vedro_valera_validator as valera_validator


class Config(vedro.Config):
    class Plugins(vedro.Config.Plugins):
        class ValeraValidator(valera_validator.ValeraValidator):
            enabled = True
