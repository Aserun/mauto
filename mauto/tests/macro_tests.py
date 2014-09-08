import mock
from nose import with_setup
from ..api import macro
from ..api.lib import library


def setup_empty():
    library.new_macro("testsuite")


def setup_fromlog():
    log = """select -r joint1.rotatePivot ;
select -add joint3.rotatePivot ;
ikHandle -sol ikRPsolver ;
// ikHandle1 effector1 //
select -r locator1 ;
select -add joint1 ;
parent;
// locator1 //
setAttr "locator1.rotateZ" 0;
setAttr "locator1.translateX" 0;
setAttr "locator1.translateY" 0;
setAttr "locator1.translateZ" 0;
setAttr "locator1.rotateX" 0;
setAttr "locator1.rotateY" 0;
select -r locator1 ;
parent -w;
// locator1 //
move -r -os -wd 0 0 9.927413 ;
select -tgl ikHandle1 ;
poleVectorConstraint -weight 1;
// ikHandle1_poleVectorConstraint1 //"""
    library.new_macro("testsuite", log)


def teardown():
    n = "testsuite"
    if library.get(n):
        library.remove_macro(n)


def test_valid():
    assert macro.Macro.is_valid("invalid_data") == False


def test_valid1():
    assert macro.Macro.is_valid({"filetype": "mauto_macro"}) == False


@with_setup(setup_empty, teardown)
def test_valid2():
    d = library.get("testsuite").serialize()
    assert macro.Macro.is_valid(d) == True


@with_setup(setup_empty, teardown)
def test_fromfile():
    d = library.get("testsuite").serialize()
    assert macro.Macro.from_data(d) is not None


@with_setup(setup_empty, teardown)
def test_record():
    with mock.patch("mauto.api.macro.cmds", create=True):
        m = library.get("testsuite")
        m.record()
        assert m.recording == True


@with_setup(setup_fromlog, teardown)
def test_fromlog():
    assert library.get("testsuite") is not None


@with_setup(setup_fromlog, teardown)
def test_inputs():
    m = library.get("testsuite")
    print m.actions, m.inputs
    assert m.inputs == ['joint3', 'joint1', 'locator1']


@with_setup(setup_fromlog, teardown)
def test_play():
    with mock.patch("mauto.api.macro.cmds", create=True) as cmds:
        # mock all the things!
        cmds.ikHandle.return_value = ["ikHandle1", "effector1"]
        cmds.poleVectorConstraint.return_value = "ikHandle1_poleVectorConstraint1"
        with mock.patch("mauto.api.macro.mel", create=True) as mel:
            return_values = {
                "ikHandle -sol ikRPsolver ;": ("ikHandle1", "effector1"),
                "poleVectorConstraint -weight 1;": "ikHandle1_poleVectorConstraint1"}
            mel.eval.side_effect = lambda x: return_values.get(x)
            # test
            m = library.get("testsuite")
            assert m.play() == True


@with_setup(setup_empty, teardown)
def test_pause():
    m = library.get("testsuite")
    m.recording = True
    with mock.patch("mauto.api.macro.cmds", create=True) as cmds:
        cmds.scriptEditorInfo.return_value = library.get_filepath("testsuite")
        m.pause()
    assert m.recording == False


@with_setup(setup_empty, teardown)
def test_pause2():
    m = library.get("testsuite")
    m.pause()
    assert m.recording == False
