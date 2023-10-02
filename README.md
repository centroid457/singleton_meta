# singleton_meta


## Features
1. perfect singleton (maybe thread safe!)
2. collect all instances 


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

### 2. access to created instances
```python
from singleton_meta import *

    class Victim1(Singleton):
        attr = 1

    class Victim2(Singleton):
        attr = 2

    assert Singleton._SINGLETONS == []
    Victim1()
    assert Singleton._SINGLETONS == [Victim1(), ]
    Victim2()
    assert Singleton._SINGLETONS == [Victim1(), Victim2(), ]
```

### 3. Use meta
```python
from singleton_meta import *

class MySingleton(metaclass=SingletonMeta):
    pass
```

### 4. NOTICE: all your Singletons must be only last classes!
don't use nesting from any Your Singletons!
```python
from singleton_meta import *

class MySingleton(Singleton):   # OK
    pass

class MySingleton2(MySingleton):    # WRONG
    pass
```