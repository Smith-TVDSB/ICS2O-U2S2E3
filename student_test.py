import pytest
import student 



def test_simple_later():
    input_values=['Zorp']
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

    assert "is in the last half of the alphabet" in output[1].lower()

def test_simple_first():
    input_values=['Alice']
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

    assert "is in the first half of the alphabet" in output[1].lower()

def test_M_name():
    input_values=['Munich']
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

    assert "is in the first half of the alphabet" in output[1].lower()

def test_multi_first_half():
    for i in ["Ally","Alexander","Bruce","Lisa","Elizabeth","Kevin","Hector","Luke"]:
        input_values=[i]
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

        assert "is in the first half of the alphabet" in output[1].lower()

def test_multi_last_half():
    for i in ["Naury","Nickey","Zoey","Octavia","Prince","Queen","Rick","Steve", "Trevor", "Tristan", "Utopia", "Walter","Yussef","Xandria"]:
        input_values=[i]
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

        assert "is in the last half of the alphabet" in output[1].lower()

def test_multi_M_names():
    for i in ["M", "Maury","Mickey","Money","Mona-Lisa","Mini","Mohammed","Morty","Mzzzzzzzzzz"]:
        input_values=[i]
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

        assert "is in the first half of the alphabet" in output[1].lower()