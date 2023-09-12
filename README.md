# singleton_meta


## Features

1. perfect singleton (maybe thread safe!)


## License

See the [LICENSE](LICENSE) file for license rights and limitations (MIT).


## Release history

See the [HISTORY.md](HISTORY.md) file for release history.


## Installation

```commandline
pip install singleton-meta
```

## Import

```python
from singleton_meta import *
```


## GUIDE

See tests and source for other examples.


### 1. Use simple nesting (common)

```python
from singleton_meta import *

class MySingleton(Singleton):
    pass

class MySingleton2(Singleton):
    pass
```

### 2. Use meta

```python
from singleton_meta import *

class MySingleton(metaclass=SingletonMeta):
    pass
```

### 3. NOTICE: all your Singletons must be only last classes!

don't use nesting from any Your Singletons!

```python
from singleton_meta import *

class MySingleton(Singleton):   # OK
    pass

class MySingleton2(MySingleton):    # WRONG
    pass
```