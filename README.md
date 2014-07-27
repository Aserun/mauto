mauto - as in Maya Automation
=============================
`mauto` is a generic macro tool for Autodesk Maya.

`mauto` implements a simple (but efficient) static analysis algorithm
which solves the external and internal dependencies at runtime, 
giving you te ability to automate repetitive tasks without write a single
line of code.


## Dependencies

- [Autodesk Maya](http://www.autodesk.com/products/autodesk-maya/overview)
- [PySide](http://qt-project.org/wiki/PySide) (included with Maya 2014+)

> `mauto` has been tested on Maya 2014+ but it should run in older
versions, please let me know if you find any issues.

### Testing:
- [Nose](https://nose.readthedocs.org/en/latest/)


## Installation

Copy the `mauto` directory somewhere in your `PYTHONPATH` (maya scripts
directory should do the trick) or clone the repo and install the project
through its `setup.py` script (_highly recommended!_).

    mayapy setup.py install

## Ussage

    import mauto
    
    #  Launch the Maya GUI...
    mauto.show()

    # ... or use it through the python api.

    # create a new macro
    m = mauto.new("my_macro")
    m.record()
    m.stop()
    m.save("path/to/my/macro.json")

    # load an existing macro
    m = mauto.load("path/to/my/macro.json")
    m.play()
    
    # redefine external inputs
    refs = m.inputs #  dict of external references
    refs["locator1"] = "pCube"
    m.play(refs)


## Contributing

- [Check for open issues] (https://github.com/csaez/mauto/issues) or open
a fresh issue to start a discussion around a feature idea or a bug.
- Fork the [mauto repository on Github](https://github.com/csaez/mauto)
to start making your changes (make sure to isolate your changes in a local branch when possible).
- Write a test which shows that the bug was fixed or that the feature works
as expected.
- Send a pull request and bug the maintainer until it gets merged and
published. :)

Make sure to add yourself to `CONTRIBUTORS.md`

## Notes

For more info, refer to the [documentation](http://github.com/csaez/mauto/wiki).