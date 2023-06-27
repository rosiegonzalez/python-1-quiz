def replace_spaces(sentence, punct):
    new_sentence = sentence.replace(" ", punct)
    return new_sentence





sentence = "Test  This is a test   Testing "
sentence2 = replace_spaces(sentence, "_")
print(sentence2)
# -> Test__This_is_a_test__Testing_