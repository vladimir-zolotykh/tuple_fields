import pytest
from tuplemeta import Point, Exercise, Tuple


def test_point_creation():
    """Test standard instantiation and property access."""
    p = Point(10, 20)
    print(f"\nTesting Point: {p}")

    # In the current implementation, p is ((10, 20),)
    # So p.x calls itemgetter(0) on p, returning (10, 20)
    assert p.x == 10
    assert p[0] == 10


def test_exercise_functionality():
    """Test with different data types (string, float, int)."""
    e = Exercise("Deadlift", 140.5, 5)
    print(f"Testing Exercise: {e}")

    # Testing that the metaclass attached the correct properties
    assert hasattr(e, "exercise_name")
    assert hasattr(e, "weight")
    assert hasattr(e, "reps")

    # verifying current nested structure
    assert e.exercise_name == "Deadlift"


def test_wrong_argument_count():
    """Test that TypeError is raised when fields count doesn't match."""
    with pytest.raises(TypeError) as excinfo:
        Point(10)  # Missing one arg
    assert "Must supply 2 args" in str(excinfo.value)

    with pytest.raises(TypeError) as excinfo:
        Exercise("Bench", 100, 5, "extra_arg")  # One too many
    assert "Must supply 3 args" in str(excinfo.value)


def test_tuple_inheritance():
    """Ensure it still behaves like a tuple."""
    p = Point(5, 5)
    assert isinstance(p, tuple)
    assert len(p) == 2
