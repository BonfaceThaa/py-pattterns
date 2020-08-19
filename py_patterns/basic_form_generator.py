def generate_webform(text_fieldlist=[], checkbox_fieldlist=[]):
    """
    builder function to take iterable list of web form elements to generate
    :param text_fieldlist:
    :param checkbox_fieldlist:
    :return: html element fields
    """
    generated_fields = "\n".join(
        map(
            lambda x: '{0}:<br><input type="text" name="{0}"><br>'.format(x),
            text_fieldlist
        )
    )
    generated_fields += "\n".join(
        map(
            lambda x: '{0}:<br><input type="checkbox" name="{0}"><br>'.format(x),
            checkbox_fieldlist
        )
    )

    return "<form>{fields}</form>".format(fields=generated_fields)


def build_html(text_fieldlist=[], checkbox_fieldlist=[]):
    """
    function to generate html fields  based on the fields provided
    :param text_fieldlist:
    :param checkbox_fieldlist:
    :return: html file
    """
    with open("outputs/gen_html.html", "w") as f:
        f.write("<html><body>{}</body></html>".format(generate_webform(text_fieldlist=text_fieldlist,
                                                                       checkbox_fieldlist=checkbox_fieldlist)))


if __name__ == "__main__":
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awesome", "bad"]
    build_html(text_fieldlist=text_fields, checkbox_fieldlist=checkbox_fields)
