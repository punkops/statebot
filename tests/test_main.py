from statebot.main import aws

__author__ = "Nick Syntychakis"
__copyright__ = "Nick Syntychakis"
__license__ = "Apache-2.0"


def test_aws(capsys):
    # Call the aws function with the desired arguments
    args = []  # Create an empty list to store the arguments
    # Add your desired arguments to the list
    args.append("arg1")
    args.append("arg2")
    aws(args)

    # Capture the stdout and stderr
    captured = capsys.readouterr()

    # Assert the expected output
    assert "AWS Here!" in captured.out
