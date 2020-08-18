def generate_webform(fieldlist):
    """
    builder function to take iterable list of web form elements to generate
    :param fieldlist:
    :return: html element fields
    """
    generated_fields = "\n".join(
        map(
            lambda x: '{0}:<br><input text="text" name="{0}"><br>'.format(x),
            fieldlist
        )
    )
    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html(elements):
    """
    function to generate html fields  based on the fields provided
    :param elements:
    :return: html file
    """
    with open("outputs/gen_html.html", "w") as f:
        f.write("<html><body>{}</body></html>".format(generate_webform(fields)))


if __name__ == "__main__":
    fields = ["name", "age", "country", "gender"]
    build_html(fields)
