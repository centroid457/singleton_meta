class SingletonMeta(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, '__INSTANCE'):
            setattr(cls, '__INSTANCE', None)
            cls.__INSTANCE = super().__call__(*args, **kwargs)
        return cls.__INSTANCE
