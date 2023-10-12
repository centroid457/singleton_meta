# singleton_meta


## Features
1. perfect singleton (maybe thread safe!)
2. collect all instances
3. check correct instantiating singletons in tree project


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

### 1. USAGE
```python
from singleton_meta import *

class MySingleton(SingletonByCallMeta):
    pass

class MySingleton2(SingletonByCallMeta):
    pass

class MySingleton(metaclass=SingletonMetaCallClass):
    pass
```

### 2. access to created instances
```python
from singleton_meta import *

class Victim1(SingletonByCallMeta):
    attr = 1

class Victim2(SingletonByCallMeta):
    attr = 2

assert SingletonByCallMeta._SINGLETONS == []
Victim1()
assert SingletonByCallMeta._SINGLETONS == [Victim1(), ]
assert Victim1._SINGLETONS == [Victim1(), ]
assert Victim1()._SINGLETONS == [Victim1(), ]
Victim2()
assert SingletonByCallMeta._SINGLETONS == [Victim1(), Victim2(), ]
```

### 3. NOTICE: all your Singletons must be only last classes!
don't use nesting from any Your Singletons!
```python
from singleton_meta import *

class MySingleton(SingletonByCallMeta):  # OK
    pass

class MySingleton2(MySingleton):  # WRONG
    pass
```
