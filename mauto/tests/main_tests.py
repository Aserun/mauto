import mauto
from nose import with_setup


def setup():
    return mauto.new_macro("testsuite")


def setup_in_memory():
    return mauto.new_macro("testsuite", save=False)


def teardown():
    mauto.remove_macro("testsuite")


@with_setup(setup, teardown)
def test_list_macros():
    return len(mauto.list_macros()) >= 1


@with_setup(setup, teardown)
def test_new_macro():
    mauto.remove_macro("testsuite")
    assert mauto.new_macro("testsuite")


@with_setup(setup, teardown)
def test_get_macro():
    return mauto.get_macro("testsuite")


@with_setup(setup, teardown)
def test_remove_macro():
    mauto.remove_macro("testsuite")


@with_setup(setup, teardown)
def test_save_macro():
    assert mauto.save_macro("testsuite")


def test_show():
    assert mauto.show is not None


@with_setup(setup, teardown)
def test_get_filepath():
    fp = mauto.get_filepath("testsuite")
    print fp
    assert "testsuite.json" in fp


@with_setup(setup_in_memory, teardown)
def test_get_filepath2():
    fp = mauto.get_filepath("testsuite")
    assert fp is None
