import cabina


class Config(cabina.Config, cabina.Section):
    GOLDEN_API_URL = cabina.env.str('GOLDEN_API_URL')
    TESTING_API_URL = cabina.env.str('TESTING_API_URL')


Config.prefetch()
