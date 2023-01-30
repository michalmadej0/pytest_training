def  get_triangle_field(base: int, height:int) -> float:
    field = 0.5* base * height
    print(field)

def test_traiangle_area(capsys):
    base = 10
    height = 8

    get_triangle_field(base, height)
    out, err = capsys.readouterr()

    assert out == '40.0\n'