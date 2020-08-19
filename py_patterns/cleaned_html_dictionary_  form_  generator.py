def generate_webform(field_dict_list):
    """
    function to generate web forms
    :param field_dict_list: list of html elements and attributes
    :return:
    """
    generated_field_list = []
    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            field_html = generate_textfield(field_dict)
        elif field_dict["type"] == "checkbox":
            field_html = generate_checkboxfield(field_dict)

        generated_field_list.append(field_html)

    generated_fields = "\n".join(generated_field_list)

    return "<form>{fields}</form>".format(fields=generated_fields)


def generate_textfield(text_field_dict):
    """
    function to generate text input fields
    :param text_field_dict:
    :return:
    """
    return '{0}: <br><input type="text" name="{1}"><br>'.format(
        text_field_dict["label"],
        text_field_dict["name"]
    )


def generate_checkboxfield(checkbox_field_dict):
    """
    function to generate text checkbox fields
    :param checkbox_field_dict:
    :return:
    """
    return '<label><input type="checkbox" id="{0}" value="{1}">{2}<br>'.format(
        checkbox_field_dict["id"],
        checkbox_field_dict["value"],
        checkbox_field_dict["label"]
    )


def build_html(field_list):
    """
    function to generate html fields  based on the fields provided
    :param field_list:
    :return: html file
    """
    with open("../outputs/gen_html.html", "w") as f:
        f.write("<html><body>{}</body></html>".format(
            generate_webform(
                field_list
            )
        )
        )


if __name__ == "__main__":
    field_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text"
        },
        {
            "type": "checkbox",
            "id": "check_it",
            "value": "1",
            "label": "Check for one",
        },
        {
            "type": "text_field",
            "label": "Another Text field",
            "name": "text_field2"
        }
    ]
    build_html(field_list)
