from cdesf2.data_structures.activity import Activity
from datetime import datetime
import pytest


def test_initial_value():
    activity = Activity('activity1', datetime.strptime('2015/05/10 08:22:53.000', '%Y/%m/%d %H:%M:%S.%f'))
    assert isinstance(activity.name, str)
    assert isinstance(activity.timestamp, datetime)
    assert isinstance(activity, Activity)
    assert activity.name == 'activity1'
    assert activity.timestamp == datetime(2015, 5, 10, 8, 22, 53)


def test_no_value():
    with pytest.raises(Exception):
        assert Activity()
