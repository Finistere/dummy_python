# dummy_python

Install package locally with:

```bash
pip install --editable <project directory>
```

The `--editable` flag makes development easier as it any changes to the python 
will be taken into account. Now you can do:

```python
from dummy.utils import hello
hello()
``` 