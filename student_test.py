import pytest
import student 



def test_simple_even():
    input_values=['2']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "even" in output[1].lower()

def test_negative_even():
    input_values=['-2']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "even" in output[1].lower()

def test_simple_odd():
    input_values=['5']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "odd" in output[1].lower()

def test_negative_odd():
    input_values=['-9']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "odd" in output[1].lower()

def test_zero_case():
    input_values=['0']
    output=[]

    def mock_input(s=None):
        if s is not None:
            output.append(s)
            return input_values.pop(0)
        else:
            output.append("")
            return input_values.pop(0)
    
    student.input = mock_input
    student.print = lambda s : output.append(s)

    student.main()

    assert "even" in output[1].lower()

def test_multi_odd_case():
    for i in [-9, -3, -31, -41, -99, -19, 87, 19, 3]:
        input_values=[str(i)]
        output=[]

        def mock_input(s=None):
            if s is not None:
                output.append(s)
                return input_values.pop(0)
            else:
                output.append("")
                return input_values.pop(0)
        
        student.input = mock_input
        student.print = lambda s : output.append(s)

        student.main()

        assert "odd" in output[1].lower()