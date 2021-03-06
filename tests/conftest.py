import pytest


@pytest.fixture
def html_content():
    return (
        "<html lang='en'><body><a href='https://www.foo.org'>Lorem Ipsum</a> "
        "is simply dummy text of the printing and typesetting industry."
        "<a href='https://foo.org'>Lorem Ipsum</a> has been the industry's "
        "standard dummy text ever since the 1500s,when an unknown printer took "
        "a galley of type and scrambled it to make a type specimen book."
        "It has survived not only <a href='https://www.bar.com'>five centuries</a>, "
        "but also the leap into electronictypesetting, "
        "<a href='/lorem/ipsum'>remaining essentially</a> unchanged.It was popularised in the 1960s "
        "with the release of <a href='https://www.bar.com?example=true'>Letraset sheets</a>"
        "containing Lorem Ipsum passages, and more recently with desktop "
        "<a href='https://www.foo.org?foo=ipsum'>publishing software</a>like Aldus PageMaker "
        "including versions of Lorem Ipsum.</body></html>"
    )
