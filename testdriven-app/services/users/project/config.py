class BaseConfig:
    """Base Configuraton"""
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Development Configuration"""
    pass


class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass
