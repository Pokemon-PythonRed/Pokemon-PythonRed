# `app/events/`

Each file in this folder corresponds to an in-game event. Names are formatted as follows:

* Event names: `<location>_<event>`
* Filenames: `app/events/<eventname>.py`

When writing an event file, start by importing basic in/out functions, as well as the `SaveFile` class. Write the file as a function. In most cases, it should take a parameter called `save` of type `SaveFile`, and return `save`.

Example function:

```python
from input import get
from output import sp
from saving import SaveFile

def example(save: SaveFile) -> SaveFile:
	sp([
		('Event reached!', False),
		('Press any key to continue.', True)
	])
	save['flag']['example'] = True
	return save
```
